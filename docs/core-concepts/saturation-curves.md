# Saturation Curves --- Understanding Diminishing Returns in Media Spend

Every marketing channel hits a point of diminishing returns. The first thousand dollars you spend on paid search generates more conversions per dollar than the hundred-thousandth dollar. Saturation curves model this relationship mathematically, and they are one of the most important components of any Marketing Mix Model.

---

## The Concept of Diminishing Returns

Diminishing returns is a fundamental economic principle: as you increase investment in a single input while holding everything else constant, each additional unit of investment produces a smaller incremental gain than the previous one.

In marketing, this happens because:

- **Audience exhaustion.** At low spend levels, your ads reach the most receptive audiences first. As spend increases, you reach less interested or less relevant audiences.
- **Frequency saturation.** The first few exposures to an ad drive awareness and intent. Additional exposures to the same audience yield progressively less response.
- **Competitive dynamics.** In auction-based channels (search, social), increasing spend raises your own bid costs, reducing efficiency.
- **Finite demand.** There is a ceiling on how many people want your product in any given period. No amount of advertising can push conversions beyond total addressable demand.

Ignoring diminishing returns leads to dramatically wrong conclusions. A linear model would suggest that doubling your TV spend doubles your TV-driven revenue. In reality, the incremental gain from doubling spend is almost always much less than double.

---

## Linear vs. Saturation Functions

### The Linear (Wrong) Assumption

A linear model assumes that the relationship between spend and outcome is a straight line: every additional dollar produces the same incremental effect. This is the default in simple regression models and is almost never true for marketing data.

### The Saturation (Correct) Approach

A saturation function maps raw spend to an "effective" spend value that accounts for diminishing returns. The function starts steep (low spend, high marginal return) and flattens as spend increases (high spend, low marginal return).

Simba uses the **hyperbolic tangent (tanh)** saturation function, which has the form:

> effective_spend = tanh(spend / scale)

Where **scale** is a parameter that controls how quickly the curve saturates. The tanh function has several desirable properties:

- It starts at zero when spend is zero.
- It rises steeply for small values of spend relative to the scale parameter.
- It approaches an asymptote (maximum effect) as spend increases.
- It is smooth and differentiable everywhere, which is important for stable model fitting and optimization.

---

## How Saturation Parameters Work in Simba

The saturation function in Simba is controlled by parameters that determine the **shape** of the diminishing returns curve for each channel. The key concept is the **scale** parameter (sometimes called the half-saturation point):

- **Small scale value** --- The channel saturates quickly. Even moderate spend levels are close to the maximum possible effect. This is typical of niche channels with small target audiences.
- **Large scale value** --- The channel can absorb more spend before diminishing returns become severe. This is typical of broad-reach channels like TV or large digital platforms.

### Channel-Specific Saturation

Different channels saturate at different rates. For example:

- **Paid search (brand terms)** typically saturates quickly because the audience searching for your brand name is finite and the first few positions capture most clicks.
- **Video (YouTube, CTV)** may have a larger saturation point because the available audience is vast and frequency can build over time before fatigue sets in.
- **Out-of-home (OOH)** can have a gradual saturation curve because coverage increases with more placements across a metro area.

Simba estimates saturation parameters from your data, but you can also set informative priors based on domain knowledge. If you know from experience that a channel saturates quickly, you can encode that expectation. See [Priors and Distributions](./priors-and-distributions.md).

---

## Interpreting Saturation Curves

Simba visualizes the fitted saturation curve for each channel, showing the relationship between spend and modeled effect. Here is how to read these curves:

### The Steep Region (Low Spend)

The initial steep portion of the curve represents the range where your spend is most efficient. Each additional dollar generates a large incremental effect. If your current spend for a channel falls in this region, there may be opportunity to increase investment profitably.

### The Transition Zone (Moderate Spend)

The middle portion of the curve is where diminishing returns begin to take hold. Spend is still productive but less efficient than at lower levels. Many well-optimized channels operate in this zone.

### The Flat Region (High Spend)

When the curve flattens, additional spend produces very little incremental effect. If a channel's current spend falls in this region, the model is suggesting that the budget would generate more return if reallocated to a less-saturated channel.

### Marginal Return Curves

In addition to the saturation curve itself, Simba can display the **marginal return curve** --- the derivative of the saturation function, showing the incremental effect of one additional dollar at each spend level. This is directly useful for budget optimization: you want to allocate budget such that the marginal return is equalized across all channels.

---

## Configuring Saturation in Model Setup

When setting up a model in Simba, you configure saturation as part of the channel specification. The platform offers two approaches:

### Smart Defaults

For most channels, Simba's smart defaults provide reasonable saturation priors based on the scale of your data. The model will estimate the saturation parameters from the data, with the priors providing gentle regularization to prevent extreme values.

### Manual Prior Configuration

If you have strong domain knowledge about a channel's saturation behavior, you can adjust the prior on the scale parameter. For example:

- If you know from past analysis that a channel saturates quickly, set a prior with a smaller mean for the scale parameter.
- If you believe a channel can absorb significantly more spend before saturating, widen the prior or increase the mean.

Simba's UI lets you visualize the implied prior saturation curve before fitting the model, so you can confirm that your prior expectations are reasonable.

### Interaction with Adstock

Saturation and [adstock](./adstock-effects.md) work together in Simba's model. The order of operations matters: typically, adstock (carryover) is applied first, spreading a week's spend across multiple weeks, and then saturation is applied to the adstocked values. This means that a heavy spend week is partially spread out over subsequent weeks before the saturation function is applied, which can moderate the apparent diminishing returns.

---

## Why Saturation Matters for Optimization

Saturation curves are the single most important input to budget optimization. Without them, an optimizer would simply recommend putting all budget into the channel with the highest average ROAS --- which ignores the fact that ROAS declines as spend increases.

With saturation curves, Simba's optimizer can:

1. Identify channels that are **under-saturated** (spending in the steep part of the curve) and recommend increasing investment.
2. Identify channels that are **over-saturated** (spending in the flat part of the curve) and recommend shifting budget elsewhere.
3. Find the **optimal allocation** where the marginal return per dollar is equalized across all channels, maximizing total incremental outcome for a given budget.

---

## Key Takeaways

- Diminishing returns are a universal feature of marketing spend. Linear models ignore this and produce misleading results.
- Simba uses the tanh saturation function to model how channel effectiveness decreases as spend increases.
- Each channel has its own saturation parameters, reflecting its unique audience size, frequency dynamics, and competitive environment.
- Saturation curves are directly interpretable: the steep region indicates efficient spend, the flat region indicates waste.
- Saturation is the foundation of budget optimization --- it tells the optimizer where the next dollar will generate the most return.

---

## Next Steps

- [Adstock Effects](./adstock-effects.md) --- Understand how saturation interacts with carryover dynamics.
- [Priors and Distributions](./priors-and-distributions.md) --- Learn how to set priors on saturation parameters.
- [Incrementality](./incrementality.md) --- See how saturation feeds into incremental contribution estimates.
