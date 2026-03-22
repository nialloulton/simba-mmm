# Model Configuration --- Configuring Priors, Saturation, and Decay

Simba provides a no-code interface for configuring the Bayesian priors that govern each channel's response curve. These settings control how the model expects each channel to behave before it sees your data, and they directly influence attribution, forecasting, and optimization results.

For most users, the [Smart Defaults](./smart-defaults.md) provide a strong starting point. This page explains what each setting means and when you might want to override the defaults.

## The Configuration Grid

The model configuration screen presents a grid with one row per channel variable. Each row contains:

| Column | Description |
|---|---|
| **Variable** | The channel or media variable being configured (for example, `Meta_Impressions`, `TV_GRPs`, `Search_Spend`). |
| **Distribution** | The prior distribution type that encodes your belief about the channel's coefficient. |
| **Mean** | The central tendency of the prior --- your best guess for the channel's effect size before the model sees data. |
| **Saturation** | The half-saturation point of the channel's response curve. Controls how quickly diminishing returns set in. |
| **Decay** | The adstock retention rate. Controls how much of this week's spend carries over to the next week. |

An example row:

```
Meta_Impressions    InverseGamma    2.5    sat: 0.85    decay: 0.3
```

This says: for Meta impressions, use an InverseGamma prior centered at 2.5, with a saturation parameter of 0.85 and a decay rate of 0.3.

## Choosing Distributions

Simba supports several prior distribution types. The two most commonly used are:

### InverseGamma

A positive-valued distribution that is naturally skewed right. It enforces the constraint that channel effects must be positive (marketing spend cannot reduce revenue) while allowing for the possibility of large effects.

- **When to use**: Default choice for most media channels. Works well when you believe the channel has a positive but uncertain effect.
- **Key behavior**: The shape parameter controls how tightly the prior is concentrated. A more concentrated prior gives the model less freedom to deviate from your expectation; a diffuse prior lets the data speak more.

### TruncatedNormal

A normal distribution truncated at zero (or another lower bound). Provides a symmetric belief around the mean while still enforcing positivity.

- **When to use**: When you have a strong prior belief about the channel's effect size and want the model to stay close to that belief unless the data strongly disagrees.
- **Key behavior**: The standard deviation controls how much the model can deviate from your prior mean. A small standard deviation creates a tight, informative prior; a large standard deviation creates a weak prior that defers to the data.

The choice between distributions rarely changes results dramatically if the mean and spread are similar. InverseGamma is the safer default because its right skew accommodates unexpectedly large effects without requiring you to set the spread precisely.

## Setting Saturation Parameters

The saturation parameter controls the shape of the diminishing returns curve for each channel. It represents the point at which the channel has captured roughly half of its maximum possible response.

- **Lower saturation values** (for example, 0.3--0.5) mean the channel saturates quickly. Small increases in spend produce meaningful lift, but doubling or tripling spend yields little additional return. This is typical for niche channels with limited audience reach.
- **Higher saturation values** (for example, 0.7--0.95) mean the channel can absorb more spend before hitting diminishing returns. This is typical for broad-reach channels like TV or large digital platforms where the addressable audience is vast.

**How to set it**: If you know from experience that increasing spend on a channel past a certain point stops producing results, set saturation to reflect that ceiling. If unsure, use the [Smart Defaults](./smart-defaults.md) and let the model learn from data.

## Setting Decay / Adstock Parameters

The decay parameter controls how much of a channel's effect carries over from one time period to the next. It is expressed as a retention rate between 0 and 1.

- **Decay of 0.0**: No carryover. The channel's effect is entirely within the week the spend occurs. This is rare but may apply to promotions or flash sales.
- **Decay of 0.3**: Moderate carryover. About 30% of this week's effect persists into the next week, 9% into the week after, and so on. Typical for digital channels like paid social or display.
- **Decay of 0.7**: Strong carryover. 70% of the effect persists each week, meaning the impact of a single week's spend is felt for many weeks afterward. Typical for TV and out-of-home advertising.
- **Decay of 0.9+**: Very strong carryover. The effect decays slowly over months. This is unusual for most media but may apply to major brand campaigns or sponsorships.

Higher decay values shift more of the [Budget Optimization](./budget-optimization.md) toward front-loading spend, since early investments compound over time.

## Channel-by-Channel Configuration

Each channel can be configured independently. There is no requirement that all channels use the same distribution or parameter ranges. In practice, different channel types have different response dynamics and should be configured accordingly.

When configuring channels:

- Group similar channels (for example, all paid social platforms) and start with similar parameters, then adjust individually if performance data suggests different behavior.
- Channels with very low spend levels may need tighter priors to prevent the model from overfitting to noise.
- New channels with no historical data should use informative priors based on industry benchmarks or results from similar channels.

## Example Configurations for Common Channels

These are starting points. Adjust based on your data and domain knowledge.

**Television (TV GRPs or Spend)**
```
TV_GRPs    InverseGamma    3.0    sat: 0.80    decay: 0.65
```
TV typically has strong carryover and moderate saturation. The effect builds over weeks and reaches a broad audience before diminishing returns set in.

**Paid Search (Spend or Clicks)**
```
Search_Spend    InverseGamma    2.0    sat: 0.60    decay: 0.15
```
Search tends to saturate faster (the audience actively searching is finite) and has minimal carryover since intent is immediate.

**Paid Social (Meta, TikTok --- Impressions or Spend)**
```
Meta_Impressions    InverseGamma    2.5    sat: 0.85    decay: 0.30
```
Social platforms have large audiences (high saturation ceiling) and moderate carryover as brand impressions linger for a few weeks.

**Out-of-Home (OOH Spend or Reach)**
```
OOH_Spend    InverseGamma    1.5    sat: 0.70    decay: 0.50
```
OOH has moderate to strong carryover (repeated exposure over weeks) and moderate saturation depending on market coverage.

## When to Override Smart Defaults

The [Smart Defaults](./smart-defaults.md) are appropriate for most situations. Consider overriding them when:

- **You have lift test results** that provide direct experimental evidence of a channel's effectiveness. Use these to set a more informative prior mean.
- **A channel is new** and has no historical data in your dataset. Defaults based on historical data will not be available, so you need to set priors manually based on industry knowledge.
- **You have strong domain expertise** that contradicts the data-driven defaults. For example, if you know a channel was running a flawed creative for the first six months and the data underestimates its true potential.
- **The model's posterior is dominated by the prior** rather than the data. This happens when spend variation is too low for the data to update the prior. In that case, the prior effectively becomes the answer, so it needs to be set carefully.

For details on how defaults are generated, see [Smart Defaults](./smart-defaults.md). For information on long-term brand effects that extend beyond standard adstock decay, see [Long-Term Effects](./long-term-effects.md).


---

## Variable Transformations

Simba supports several mathematical transformations that can be applied to variables before they enter the model. Transformations help normalize data distributions and can improve model fit.

### Available Transformations

| Transformation | Formula | When to Use |
|---|---|---|
| **Identity** | y = x | Default. Use when the variable does not need transformation. |
| **Log** | y = log(x) | When the variable has a right-skewed distribution or when you expect multiplicative (percentage) effects rather than additive. Common for revenue and spend variables. |
| **Log-Log** | y = log(log(x)) | For highly skewed variables where a single log is insufficient. Rarely needed but useful for variables spanning many orders of magnitude. |
| **Power** | y = x^p | Applies a power transformation with a configurable exponent. Useful for fine-tuning the relationship shape between input and output. |
| **Box-Cox** | y = (x^lambda - 1) / lambda | A flexible family of transformations parameterized by lambda. Automatically finds the best power transformation to normalize the data. Includes log (lambda=0) and identity (lambda=1) as special cases. |

Transformations are configured during Step 4 (Model Setup) of the model creation wizard.

### Choosing a Transformation

For most models, **identity or log** transformations are sufficient. Use log when your target variable (e.g., revenue) spans a wide range and you expect percentage changes in spend to drive percentage changes in outcome. Use identity when the relationship is expected to be additive.

Power and Box-Cox transformations are advanced options for cases where standard transformations produce poor model fit.

## Adstock Type Selection

In addition to configuring the decay rate parameter, you can choose the adstock function type for each channel:

- **Geometric** (default): Immediate peak with exponential decay. Appropriate for most channels.
- **Power Law**: Immediate peak with non-linear decay that varies with accumulation level.
- **Delayed**: Peak occurs after a configurable delay, then decays. Use for channels where impact builds before converting.

See [Adstock Effects](../core-concepts/adstock-effects.md) for detailed explanations of each type, including when to use each one.
