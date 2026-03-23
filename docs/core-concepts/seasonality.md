# Seasonality --- Modeling Seasonal Patterns in Marketing Data

Sales do not happen in a vacuum. Retail spikes during the holidays. Ice cream sells more in summer. Tax software peaks in April. These predictable, recurring patterns are **seasonal effects**, and failing to account for them is one of the most common sources of error in marketing measurement.

---

## What Are Seasonal Effects?

Seasonal effects are recurring, time-based patterns in your outcome variable that are driven by factors outside your marketing mix. They can include:

- **Calendar seasonality.** Day-of-week patterns (e.g., more purchases on weekends), monthly cycles (e.g., pay-period effects), or annual patterns (e.g., holiday shopping, summer slowdowns).
- **Holiday effects.** Concentrated spikes around specific dates such as Black Friday, Prime Day, Christmas, Back-to-School, or Valentine's Day.
- **Industry-specific cycles.** Tax filing deadlines for financial services, open enrollment periods for insurance, harvest seasons for agriculture-related products.
- **Weather-driven patterns.** Higher demand for seasonal categories (e.g., sunscreen, snow gear) that correlates with climate cycles.
- **Cultural and sporting events.** Super Bowl, World Cup, awards season, or other events that predictably shift consumer behavior.

These patterns exist independently of your marketing activity. They represent changes in consumer demand that would occur whether or not you ran a single ad.

---

## Why Seasonality Matters for Marketing Measurement

If your model does not account for seasonal effects, it will confuse seasonality with marketing effectiveness.

![Why seasonality matters for accurate media attribution](./images/seasonality-attribution.png)
*Left: without seasonality controls, the holiday sales surge is wrongly attributed to media spend, inflating channel effectiveness. Right: with seasonality properly modeled, seasonal demand is separated and media contributions are accurately measured.*

### Error 1: Inflating Channel Contributions

Suppose your brand increases TV spend during the holiday season (a common strategy). Sales also increase during the holiday season --- but much of that increase is seasonal demand that would have occurred without any advertising. A model without seasonality controls will attribute the seasonal sales lift to TV, dramatically overestimating its effectiveness.

### Error 2: Underestimating Channels That Run in Off-Peak Periods

Conversely, if a channel runs primarily during a slow season (e.g., a summer display campaign), a model without seasonality will see lower-than-average sales during the campaign period and may underestimate or even estimate a negative effect for the channel.

In both cases, the root cause is the same: the model cannot distinguish between "sales went up because we spent more" and "sales went up because it is December." Seasonality controls solve this by giving the model an explicit mechanism to absorb time-based demand patterns.

---

## The Model Equation

To understand how seasonality fits into the full model, here is the additive structure Simba uses:

> **outcome = intercept + trend + seasonality + media_contributions + control_variables + event_effects + noise**

Each component is estimated jointly in a single Bayesian model, meaning they are all identified simultaneously rather than sequentially. This avoids the "residual fitting" problems that arise when components are estimated one at a time.

![Additive model decomposition](./images/seasonality-decomposition.png)
*The model decomposes observed sales into additive components: baseline (intercept + trend), seasonal patterns (Fourier series), media contributions, and event effects. Each component is estimated jointly.*

---

## Fourier-Based Seasonality

Simba models seasonal patterns using **Fourier features** --- pairs of sine and cosine functions at different frequencies that, when combined, can represent any periodic pattern.

### How Fourier Features Work

The Fourier basis for seasonality generates **2n features from n terms**:

For each term k = 1, 2, ..., n:
- cos(2pi x k x t / p)
- sin(2pi x k x t / p)

Where **t** is the normalized time variable and **p** is the period (365.25 days for annual seasonality, 7 days for weekly seasonality).

Each Fourier coefficient has an independent **Normal(0, 10)** prior, where 10 is the default `seasonality_prior_scale`. This weakly informative prior allows the model to learn the seasonal pattern from data without imposing a specific shape.

![Seasonal components in Simba](./images/seasonality-components.png)
*Top left: individual Fourier terms (cosine and sine pairs) at different frequencies. Top right: how the number of terms affects the fitted shape --- n=2 captures only broad trends, n=10 (default) can fit sharp holiday spikes. Bottom left: annual and weekly seasonality combined for daily data. Bottom right: event effects are GP-smoothed for realistic temporal spread.*

### Annual Seasonality

Annual seasonality captures patterns that repeat on a yearly cycle. Simba uses:

- **Period:** 365.25 days (accounting for leap years), normalized by the training data span.
- **Default terms:** n = 10, producing 20 features (10 cosine + 10 sine).
- **Always enabled** for all data frequencies.

The number of terms controls the smoothness:

- **Fewer terms (n=2--3)** produce smooth curves that capture broad annual trends (e.g., gradual summer increase).
- **More terms (n=8--10)** allow the model to fit sharper, more localized effects (e.g., a sharp holiday spike).
- **Default (n=10)** is calibrated to capture most important seasonal patterns without overfitting.

### Weekly Seasonality

Weekly seasonality captures day-of-week patterns (e.g., higher sales on weekends). It is **only available for daily data** --- weekly or monthly aggregated data cannot identify within-week patterns.

- **Period:** 7 days, normalized by the training data span.
- **Terms:** Configurable, typically 3--5.
- **Combined:** When both annual and weekly seasonality are enabled (daily data), their effects are summed.

---

## Trend Modeling

In addition to seasonality, Simba models long-term trends --- gradual shifts in the baseline that occur over months or years. Three trend types are available:

![Three trend types available in Simba](./images/seasonality-trend-types.png)
*Left: Gaussian Random Walk tracks irregular shifts but can be noisy. Center: HSGP with Matern52 kernel (default) produces smooth, flexible trends. Right: piecewise linear identifies distinct growth phases separated by changepoints.*

### Smooth HSGP Trend (Default)

The default trend type (`smooth_lltrend`) uses a **Hilbert Space Gaussian Process** with a Matern52 kernel. It produces smooth, flexible trend curves that can capture gradual growth, plateaus, and gentle reversals without overfitting to noise.

Key features:
- Includes a learned mean function with optional weak linear trend component.
- Uses sigmoid scaling with a learned baseline share parameter (kappa = 4.0).
- Estimates the empirical slope from data to inform the trend direction.

This is the recommended trend type for most use cases.

### Gaussian Random Walk Trend

The `lltrend` type models the baseline as a **Gaussian Random Walk** passed through a softplus (log1pexp) transformation to ensure positivity. It is more flexible than the HSGP trend but can also be noisier, potentially absorbing patterns that should be attributed to media or seasonality.

### Piecewise Linear Trend (Changepoint)

The `changepoint` type fits a **piecewise linear trend** with Laplace-distributed changepoint magnitudes (similar to Prophet's approach). It models the trend as a series of linear segments connected at changepoints.

- **Default changepoints:** 8, spread across the first 80% of the data.
- **Changepoint prior scale:** 0.05 (Laplace), encouraging sparse changes.
- Best suited when you expect distinct growth phases or structural breaks.

### When Trend Is Enabled

When trend is enabled, the intercept is set to zero (the trend component absorbs the baseline level). When trend is disabled, the intercept is estimated as a TruncatedNormal centered on the dependent variable mean.

---

## Event and Holiday Effects

For known events with outsized impact (e.g., Black Friday, Prime Day, Christmas), Simba supports **event indicators** that capture sharp, short-duration effects that Fourier terms alone might smooth over.

### How Events Are Modeled

Events are not simply binary dummy variables. Simba uses a more sophisticated approach:

1. **One-hot encoding:** Each event date is encoded as a one-hot vector aligned to the data's time periods.
2. **Hierarchical weights:** Event effects share a hierarchical prior: each event's weight is drawn from Normal(mu_weight, sigma_weight), where mu_weight ~ Normal(0, 1) and sigma_weight ~ HalfNormal(1). This pools information across events while allowing individual variation.
3. **GP smoothing:** The event effects are convolved with a **Matern32 Gaussian Process kernel** to produce realistic temporal spread --- events affect nearby periods, not just the exact date.

The smoothing length depends on data frequency:
- **Weekly data:** Convolution length of approximately 4 periods (lower=1, upper=3).
- **Daily data:** Convolution length of approximately 28 periods (lower=7, upper=21).
- **Monthly data:** Convolution length of approximately 0.8 periods (lower=0.2, upper=1).

### Configuring Events in the UI

Simba's holiday selector provides:

- **Country-based holiday lookup** using ISO 3166-1 country codes (powered by the `date-holidays` library). Select your country and Simba will populate standard holidays.
- **Custom event dates** that you can add manually for business-specific events (e.g., product launches, sales events).
- **Automatic period alignment** --- holidays are "snapped" to the correct period boundary for your data frequency (daily or weekly).

---

## Periodicity Detection

Simba automatically detects the frequency of your data by analyzing the gaps between consecutive dates:

| Detected Periodicity | Typical Gap | Annual Seasonality | Weekly Seasonality |
|---|---|---|---|
| **Daily** | ~1 day | Yes (n=10) | Yes (configurable) |
| **Weekly** | ~7 days | Yes (n=10) | No |
| **Monthly** | ~30 days | Yes (n=10) | No |
| **Irregular** | Variable | Yes (n=10) | No |

Periodicity also affects default effect periods for media channels (45 for daily, 6 for weekly, 2 for monthly) and event smoothing kernel parameters.

---

## Automatic vs. Manual Seasonality Configuration

### Automatic Handling

For most users, Simba's default seasonality configuration is sufficient. The platform automatically:

1. Detects the frequency of your data (daily, weekly, monthly, or irregular).
2. Selects 10 Fourier terms for annual seasonality (and weekly seasonality for daily data).
3. Fits the seasonal component jointly with channel effects, [saturation](./saturation-curves.md), and [adstock](./adstock-effects.md).
4. Uses the default smooth HSGP trend.

### Manual Adjustments

Power users can adjust seasonality settings when needed:

- **Number of Fourier terms.** If the fitted seasonal pattern is too smooth (missing known peaks) or too jagged (fitting noise), you can increase or decrease the number of terms.
- **Event indicators.** Add specific dates for holidays or events that are important to your business, using the country-based holiday selector or custom date entry.
- **Trend type.** Switch between smooth HSGP (default), Gaussian Random Walk, or piecewise linear depending on the nature of your baseline dynamics.
- **Seasonality prior scale.** Adjust the prior standard deviation (default 10) to control how much the seasonal component can vary. Smaller values produce more conservative seasonal patterns.

---

## Interaction with Other Model Components

Seasonality does not operate in isolation. It interacts with other model components in important ways:

### Seasonality and Incrementality

Proper seasonality modeling is essential for accurate [incrementality](./incrementality.md) estimates. If seasonal demand is not absorbed by the seasonal component, it leaks into channel contribution estimates, inflating the apparent incrementality of channels that correlate with seasonal peaks.

### Seasonality and Saturation

Channels that ramp up spend during peak seasons may appear to saturate faster if the model does not account for the seasonal baseline. By modeling seasonality explicitly, Simba ensures that [saturation curves](./saturation-curves.md) reflect true diminishing returns rather than seasonal artifacts.

### Seasonality and Baseline

The seasonal component works together with the trend and intercept to define the full baseline --- the level of outcome you would expect with zero media spend. This baseline is the reference point against which all incremental contributions are measured.

---

## Key Takeaways

- Seasonal effects are recurring, time-based patterns in demand that exist independently of marketing activity.
- Failing to model seasonality leads to inflated channel contributions during peak seasons and underestimated contributions during off-peak periods.
- Simba uses **Fourier-based seasonality** with default n=10 terms (20 features) and Normal(0, 10) priors to flexibly capture annual patterns. Weekly seasonality is available for daily data only.
- **Three trend types** are available: smooth HSGP (default, recommended), Gaussian Random Walk, and piecewise linear with changepoints.
- **Event effects** are modeled as GP-smoothed one-hot indicators with hierarchical Normal weights, not simple binary dummies.
- The model equation is fully additive: outcome = intercept + trend + seasonality + media + controls + events + noise.
- Automatic configuration works well for most use cases. Manual adjustments are available for the number of Fourier terms, trend type, event dates, and seasonality prior scale.

---

## Next Steps

- [Incrementality](./incrementality.md) --- See how seasonality separation improves causal attribution.
- [Marketing Mix Modeling](./marketing-mix-modeling.md) --- Understand how seasonality fits into the full model structure.
- [Priors and Distributions](./priors-and-distributions.md) --- Learn how seasonal component priors work.
- [Saturation Curves](./saturation-curves.md) --- See how proper seasonality avoids saturation artifacts.
