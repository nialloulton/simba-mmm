# Incrementality --- Measuring the True Causal Impact of Marketing

Not every sale that follows an ad was caused by that ad. Incrementality measurement answers the most important question in marketing analytics: **"How many conversions would I have lost if I had not spent on this channel?"**

Simba's Bayesian MMM is designed from the ground up to isolate incremental impact, separating organic demand from media-driven lift across every channel in your mix.

---

## What Is Incrementality?

Incrementality is the difference between what happened and what **would have happened** in the absence of a marketing activity. It is the causal effect of your spend.

Consider this scenario: your company generated 10,000 conversions last month while spending $500K across five channels. How many of those conversions were caused by the marketing spend, and how many would have occurred anyway --- from brand awareness, word of mouth, direct traffic, or seasonal demand?

The conversions that would have happened regardless are your **base** (or organic) demand. The conversions above that baseline, caused by your marketing activities, are the **incremental lift**. Incrementality measurement is the process of estimating this lift for each channel.

---

## Base Sales vs. Incremental Lift

Every outcome in your data can be decomposed into components:

- **Base (organic) demand** --- Sales driven by brand equity, repeat purchasing, direct navigation, and other factors unrelated to current media spend. This is what you would observe if you turned off all paid media.
- **Seasonality and trend** --- Predictable patterns driven by time of year, holidays, or long-term growth trends. See [Seasonality](./seasonality.md).
- **Control variables** --- External factors you include in the model, such as pricing, promotions, competitor activity, or economic indicators.
- **Incremental media contributions** --- The causal lift from each marketing channel, after accounting for [saturation](./saturation-curves.md) and [adstock](./adstock-effects.md) effects.

Simba's model estimates each of these components simultaneously, producing a full decomposition of your outcome variable. The media contributions are your incremental effects.

---

## Causal Attribution Across Channels

A key strength of MMM-based incrementality is that it attributes outcomes **causally** rather than by association. Here is the difference:

- **Correlational attribution** (e.g., last-click): "The user clicked a paid search ad before converting, so paid search gets credit." This ignores the possibility that the user would have converted anyway.
- **Causal attribution** (MMM): "Controlling for all other channels, seasonality, and baseline demand, the observed variation in paid search spend is associated with X additional conversions." This isolates the effect of the channel from confounding factors.

Simba achieves causal attribution by modeling all channels simultaneously. When the model estimates the effect of TV spend, it holds paid search, social, display, and every other channel constant. This controls for the fact that channels often scale up and down together (e.g., during a product launch) and prevents double-counting.

### Handling Correlated Channels

In practice, many channels are correlated --- brands often increase TV and digital spend during the same campaign flights. This multicollinearity makes it difficult for any model to perfectly separate channel effects. Bayesian MMM handles this better than frequentist alternatives for two reasons:

1. **Lift test calibration constrains the solution space.** If lift test data shows paid search ROAS is between 2x and 4x, this observation constrains the model so it will not attribute all of the effect to TV just because the two channels happen to be correlated. See [Priors and Distributions](./priors-and-distributions.md).
2. **Uncertainty reflects ambiguity.** When two channels are highly correlated, the posterior distributions will be wider, honestly reflecting the difficulty of separating their effects. This prevents overconfident attribution.

---

## Lift Test Integration for Validation

Lift tests (also called incrementality tests, geo tests, or holdout experiments) are randomized experiments that measure the causal effect of a single channel by comparing a treatment group (exposed to ads) with a control group (not exposed).

While lift tests are the gold standard for single-channel causal measurement, they have practical limitations:

- You can only test one or two channels at a time.
- Tests require sufficient duration and sample size.
- Running them on every channel every quarter is logistically impractical.

Simba bridges this gap by letting you **calibrate your MMM with lift test results**. When you have a lift test result for a channel, you can add it as a likelihood observation that calibrates the model. The model then combines this experimental evidence with the observational data through the likelihood function, producing posterior estimates that are consistent with both the time-series patterns and the experimental results.

This creates a virtuous cycle:

1. Run a lift test on a high-priority channel.
2. Feed the result into Simba as a calibration observation in the Model Details step.
3. The model uses this likelihood constraint to improve estimates for all channels (because better-calibrated response curves for one channel reduce ambiguity for correlated channels).
4. Use model output to prioritize the next lift test.

---

## How Simba Separates Organic from Media-Driven Outcomes

Simba's decomposition engine isolates incrementality through several mechanisms working together:

### Baseline Estimation

The model includes an intercept and trend component that captures organic demand --- the level of outcome you would expect with zero media spend. This baseline absorbs brand equity, repeat purchase behavior, and other non-media factors.

### Seasonal Controls

Seasonal patterns --- holiday spikes, summer lulls, back-to-school peaks --- are modeled explicitly so they are not mistakenly attributed to media channels that happen to ramp up during the same periods. See [Seasonality](./seasonality.md).

### Saturation and Adstock Transformations

Raw spend or impression data is transformed through [saturation functions](./saturation-curves.md) and [adstock decay](./adstock-effects.md) before entering the model. These transformations capture the nonlinear, time-lagged nature of advertising effects, producing more accurate incrementality estimates than models that treat media spend as a simple linear input.

### Bayesian Posterior Decomposition

After the model is fitted, Simba computes the contribution of each component by evaluating the model with and without each channel's transformed spend. The difference is the channel's incremental contribution. Because this is done using the full posterior distribution, every contribution estimate comes with a [credible interval](./bayesian-modeling.md) that quantifies uncertainty.

### Contribution Waterfall

Simba visualizes the decomposition as a contribution waterfall chart, showing:

- Base demand
- Seasonal effects
- Each channel's incremental contribution (with uncertainty bands)
- Total predicted outcome

This makes it easy for stakeholders to see how much of the business is driven by media versus organic demand.

---

## Practical Considerations

### What "Incremental" Does Not Mean

Incrementality is not the same as last-touch attribution, first-touch attribution, or any rule-based model. It is a **counterfactual** concept: what would have happened if you had not spent? This is a fundamentally different (and more useful) question than "which touchpoint did the user interact with last?"

### Incrementality Can Be Negative

It is possible for a channel to have a negative incremental effect --- meaning the spend actively reduced conversions. This can happen with over-frequency (ad fatigue), poor creative, or audiences that find the ads intrusive. Simba's Bayesian framework will surface these effects when the data supports them.

### Incrementality Changes Over Time

A channel's incremental contribution is not static. As spend levels change, competitors adjust, and audiences evolve, incrementality shifts. Simba supports regular model refreshes so your incrementality estimates stay current.

---

## Key Takeaways

- Incrementality measures the causal impact of marketing --- the conversions that would not have happened without media spend.
- Simba decomposes outcomes into base demand, seasonal effects, control variables, and incremental media contributions.
- Bayesian priors and full uncertainty quantification handle correlated channels and sparse data more effectively than frequentist alternatives.
- Lift test results can be integrated as likelihood observations, creating a feedback loop between experiments and modeling.
- Every incrementality estimate in Simba comes with a credible interval, enabling risk-aware decision-making.

---

## Next Steps

- [Saturation Curves](./saturation-curves.md) --- Learn how diminishing returns affect incrementality.
- [Adstock Effects](./adstock-effects.md) --- Understand how carryover impacts the timing of incremental lift.
- [Bayesian Modeling](./bayesian-modeling.md) --- Dive deeper into the statistical foundation.
