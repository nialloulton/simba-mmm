# Incremental Measurement --- Channel Attribution and Impact Analysis

Incremental Measurement is the second step in the Simba workflow. After the [AI Data Auditor](./data-auditor.md) confirms your data is clean, this step determines what each marketing channel actually contributed to revenue --- separating true media impact from baseline demand, seasonality, and other non-media factors.

## What Incremental Measurement Means in Practice

Traditional attribution models (last-click, first-touch, linear) assign credit based on who touched the customer last or most often. These models cannot tell you whether the marketing activity actually caused the sale or whether the customer would have purchased anyway.

Incremental measurement answers a different question: **how much additional revenue did each channel generate that would not have occurred without the spend?** Simba uses Bayesian causal inference to estimate this, accounting for confounders like seasonality, promotions, economic trends, and baseline demand.

The result is a clear picture of each channel's true contribution, not just its correlation with sales.

## Base Sales vs Media Lift Breakdown

Simba decomposes total revenue into three components:

- **Base Sales**: Revenue that would have occurred without any marketing activity. This captures organic demand, brand equity built over years, seasonal purchasing patterns, and macroeconomic factors. Base sales often represent the largest share of total revenue.
- **Media Lift**: The incremental revenue attributable to marketing channels. Each channel's lift is estimated independently, with the model accounting for interactions and overlap between channels.
- **Total Revenue**: The sum of base sales and media lift, which should align closely with observed revenue. The gap between modeled total and actual total is a measure of model fit.

This decomposition is displayed as a stacked visualization showing how base sales and individual channel contributions combine to produce total revenue over time.

## Causal Attribution Across All Channels

The model estimates each channel's incremental contribution using Bayesian regression with media transformations (saturation and adstock). This means:

- **Saturation effects** are captured: doubling spend on a channel does not double its impact. The model learns the point of diminishing returns for each channel.
- **Adstock (carryover) effects** are captured: a TV ad aired this week may continue driving sales for several weeks afterward. The model estimates how long each channel's effect persists.
- **Confounders are controlled for**: seasonality, holidays, promotions, and other non-media variables are included in the model so they do not inflate channel attribution.

Attribution results are shown per channel with posterior distributions, giving you not just a point estimate but a range of plausible values. Wider distributions indicate more uncertainty about a channel's contribution; narrower distributions indicate higher confidence.

## Lift Test Integration for Validation

If you have run controlled experiments --- geo-lift tests, conversion lift studies, or randomized holdout tests --- Simba can incorporate those results as Bayesian priors or use them to validate model outputs.

- **As priors**: Lift test results inform the model's expectations about a channel's effectiveness before it sees the observational data. This is especially valuable for channels with limited spend variation in historical data.
- **As validation**: Compare model-estimated lift against experimentally measured lift. Agreement between the two increases confidence in the model. Disagreement flags channels where the model may need recalibration or where the experiment had limitations.

Integrating lift tests is optional but recommended. It bridges the gap between observational modeling and experimental evidence, producing more trustworthy attribution.

## Interpreting Measurement Results

The measurement results page presents:

1. **Revenue decomposition chart**: A time series showing base sales and each channel's contribution stacked to equal total revenue.
2. **Channel contribution summary**: A table listing each channel's estimated incremental revenue, share of total media lift, and cost efficiency (incremental revenue per dollar spent).
3. **Posterior distributions**: For each channel, a density plot showing the range of plausible incremental contributions. The median is the best single estimate; the 90% credible interval shows the range within which the true value almost certainly falls.
4. **Model fit diagnostics**: Metrics showing how well the model's predicted revenue matches observed revenue. A good fit (R-squared above 0.90, low mean absolute error) supports trusting the attribution results.

Focus on the credible intervals, not just point estimates. A channel with a high median contribution but a wide interval that includes zero may not be reliably driving sales.

## Common Patterns and What They Mean

**Large base sales relative to media lift.** This is normal for established brands. It means most revenue comes from existing demand rather than marketing. The media channels are still valuable --- they are adding incremental revenue on top of a strong baseline.

**One channel dominates the media lift.** Check whether this reflects reality or a data artifact. If the dominant channel also has the most spend variation, the model has the most information to work with. Channels with flat, consistent spend are harder to measure and may appear less impactful than they truly are.

**A channel shows near-zero or negative estimated lift.** This does not necessarily mean the channel is worthless. It may mean the model cannot detect its effect given the available data. Consider whether the channel had enough spend variation during the measurement period, or whether a lift test could provide additional evidence.

**Seasonal patterns visible in base sales.** This is expected. The model separates seasonal demand from media impact, so you should see base sales rise and fall with natural demand cycles while media contributions reflect actual campaign performance.

After reviewing measurement results, proceed to [Scenario Planning](./scenario-planning.md) to forecast how different budget allocations would affect future revenue.
