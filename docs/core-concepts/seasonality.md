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

If your model does not account for seasonal effects, it will **confuse seasonality with marketing effectiveness**. This leads to two serious errors:

### Error 1: Inflating Channel Contributions

Suppose your brand increases TV spend during the holiday season (a common strategy). Sales also increase during the holiday season --- but much of that increase is seasonal demand that would have occurred without any advertising. A model without seasonality controls will attribute the seasonal sales lift to TV, dramatically overestimating its effectiveness.

### Error 2: Underestimating Channels That Run in Off-Peak Periods

Conversely, if a channel runs primarily during a slow season (e.g., a summer display campaign), a model without seasonality will see lower-than-average sales during the campaign period and may underestimate or even estimate a negative effect for the channel.

In both cases, the root cause is the same: the model cannot distinguish between "sales went up because we spent more" and "sales went up because it is December." Seasonality controls solve this by giving the model an explicit mechanism to absorb time-based demand patterns.

---

## How Simba Handles Seasonal Patterns

Simba incorporates seasonality directly into the model structure, ensuring that seasonal demand is separated from media-driven outcomes before channel effects are estimated.

### Fourier-Based Seasonality

Simba models seasonal patterns using **Fourier features** --- pairs of sine and cosine functions at different frequencies that, when combined, can represent any periodic pattern. This is the same approach used in the widely adopted Prophet forecasting framework and in PyMC-Marketing.

The key advantage of Fourier-based seasonality is flexibility. Rather than hard-coding specific holiday dates or assuming a fixed seasonal shape, the model learns the seasonal pattern from your data. It can capture:

- Smooth annual cycles (e.g., gradual summer increase, gradual winter decrease)
- Sharp holiday spikes (e.g., Black Friday)
- Complex multi-modal patterns (e.g., back-to-school and holiday peaks in the same year)

The number of Fourier terms controls the **smoothness** of the seasonal pattern:

- **Fewer terms** produce smoother seasonal curves that capture broad annual trends.
- **More terms** allow the model to fit sharper, more localized seasonal effects.

Simba's defaults are calibrated to capture the most important seasonal patterns without overfitting to noise.

### Trend Components

In addition to seasonality, Simba models **long-term trends** --- gradual upward or downward shifts in your baseline that occur over months or years. This could reflect organic brand growth, market expansion, competitive dynamics, or macroeconomic conditions.

By modeling trend separately from seasonality and media effects, the model avoids attributing gradual growth to whatever channels happened to be active during the growth period.

### Holiday and Event Effects

For known events with outsized impact (e.g., Black Friday, Prime Day), Simba supports **event indicators** --- binary or weighted variables that flag specific dates. These allow the model to capture sharp, short-duration effects that Fourier terms alone might smooth over.

You can configure event indicators through the UI by specifying dates and, optionally, the expected duration of each event's impact.

---

## Automatic vs. Manual Seasonality Configuration

### Automatic Handling

For most users, Simba's default seasonality configuration is sufficient. The platform automatically:

1. Detects the frequency of your data (daily, weekly, monthly).
2. Selects an appropriate number of Fourier terms for annual and, if applicable, weekly seasonality.
3. Fits the seasonal component as part of the full model, jointly estimating seasonality alongside channel effects, [saturation](./saturation-curves.md), and [adstock](./adstock-effects.md).

### Manual Adjustments

Power users can adjust seasonality settings when needed:

- **Number of Fourier terms.** If the fitted seasonal pattern is too smooth (missing known peaks) or too jagged (fitting noise), you can increase or decrease the number of terms.
- **Event indicators.** Add specific dates for holidays or events that are important to your business.
- **Disabling seasonality.** In rare cases where your data has no meaningful seasonal pattern (e.g., a B2B SaaS product with stable monthly demand), you can simplify the model by reducing or removing seasonality components.

---

## Examples of Seasonal Effects Across Industries

### Retail and E-Commerce

Retail businesses experience the most pronounced seasonal patterns. The holiday shopping season (November through December) can account for 20% to 40% of annual revenue. Black Friday and Cyber Monday create massive single-day spikes. Back-to-school drives a secondary peak in August and September.

Without seasonality controls, a model would attribute the Q4 sales surge to the heavy advertising that typically accompanies it, dramatically overstating media effectiveness.

### Travel and Hospitality

Travel demand follows strong seasonal patterns: summer peaks for leisure travel, holiday peaks for family visits, and business travel lulls in December and August. Airlines and hotels that increase advertising during peak season need their MMM to separate seasonal demand from ad-driven bookings.

### Financial Services

Tax preparation services see demand concentrated in January through April. Insurance open enrollment drives a predictable spike. Wealth management sees elevated activity at year-end. These patterns must be modeled explicitly to avoid misattributing cyclical demand to marketing.

### Food and Beverage

Quick-service restaurants may see weekly seasonality (higher sales on Fridays and weekends), monthly patterns (payday effects), and annual cycles (summer drink promotions, holiday catering). Fast-moving consumer goods (FMCG) brands face similar dynamics in grocery.

### Consumer Technology

Product launch cycles create predictable demand patterns --- new smartphone launches in September, gaming console releases in Q4, and back-to-school laptop demand in August. These interact with marketing campaigns and must be modeled separately.

---

## Interaction with Other Model Components

Seasonality does not operate in isolation. It interacts with other model components in important ways:

### Seasonality and Incrementality

Proper seasonality modeling is essential for accurate [incrementality](./incrementality.md) estimates. If seasonal demand is not absorbed by the seasonal component, it leaks into channel contribution estimates, inflating the apparent incrementality of channels that correlate with seasonal peaks.

### Seasonality and Saturation

Channels that ramp up spend during peak seasons may appear to saturate faster if the model does not account for the seasonal baseline. By modeling seasonality explicitly, Simba ensures that [saturation curves](./saturation-curves.md) reflect true diminishing returns rather than seasonal artifacts.

### Seasonality and Baseline

The seasonal component works together with the trend and intercept to define the full **baseline** --- the level of outcome you would expect with zero media spend. This baseline is the reference point against which all incremental contributions are measured.

---

## Diagnosing Seasonal Fit

After fitting a model, Simba provides tools to assess whether the seasonal component is capturing the right patterns:

- **Seasonal decomposition plot.** Visualizes the estimated seasonal pattern over the observed time period, letting you confirm that known peaks and troughs are captured.
- **Residual analysis.** If the model residuals show systematic patterns by time of year, it may indicate that the seasonal component needs more flexibility (more Fourier terms or event indicators).
- **Posterior predictive checks.** Comparing the model's predictions to actual data across different seasons confirms that the model reproduces known seasonal dynamics.

---

## Key Takeaways

- Seasonal effects are recurring, time-based patterns in demand that exist independently of marketing activity.
- Failing to model seasonality leads to inflated channel contributions during peak seasons and underestimated contributions during off-peak periods.
- Simba uses Fourier-based seasonality to flexibly capture annual and weekly patterns, supplemented by event indicators for known holidays and events.
- Automatic seasonality configuration works well for most use cases. Manual adjustments are available for power users.
- Proper seasonality modeling is a prerequisite for accurate incrementality estimation and realistic saturation curves.

---

## Next Steps

- [Incrementality](./incrementality.md) --- See how seasonality separation improves causal attribution.
- [Marketing Mix Modeling](./marketing-mix-modeling.md) --- Understand how seasonality fits into the full model structure.
- [Priors and Distributions](./priors-and-distributions.md) --- Learn how seasonal component priors work.
