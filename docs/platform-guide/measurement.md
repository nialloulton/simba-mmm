# Incremental Measurement --- Channel Attribution and Impact Analysis

Incremental Measurement is where Simba determines what each marketing channel actually contributed to revenue --- separating true media impact from baseline demand, seasonality, and other non-media factors.

## What Incremental Measurement Means in Practice

Traditional attribution models (last-click, first-touch, linear) assign credit based on who touched the customer last or most often. These models cannot tell you whether the marketing activity actually caused the sale or whether the customer would have purchased anyway.

Incremental measurement answers a different question: **how much additional revenue did each channel generate that would not have occurred without the spend?** Simba uses Bayesian causal inference to estimate this, accounting for confounders like seasonality, promotions, economic trends, and baseline demand.

The result is a clear picture of each channel true contribution, not just its correlation with sales.

## Base Sales vs Media Lift Breakdown

Simba decomposes total revenue into components:

- **Base Sales**: Revenue that would have occurred without any marketing activity. This captures organic demand, brand equity built over years, seasonal purchasing patterns, and macroeconomic factors. Base sales often represent the largest share of total revenue.
- **Media Lift**: The incremental revenue attributable to marketing channels. Each channel lift is estimated independently, with the model accounting for interactions and overlap between channels.

This decomposition is displayed in the **Contributions** tab as stacked area charts, waterfall charts, and year-over-year comparison views showing how base sales and individual channel contributions combine to produce total revenue over time.

## Causal Attribution Across All Channels

The model estimates each channel incremental contribution using Bayesian regression with media transformations (saturation and adstock). This means:

- **Saturation effects** are captured: doubling spend on a channel does not double its impact. The model learns the point of diminishing returns for each channel.
- **Adstock (carryover) effects** are captured: a TV ad aired this week may continue driving sales for several weeks afterward. The model estimates how long each channel effect persists.
- **Confounders are controlled for**: seasonality, holidays, promotions, and other non-media variables are included in the model so they do not inflate channel attribution.

Attribution results are shown per channel with **94% Highest Density Intervals (HDI)** --- bounded at 3% and 97% --- giving you not just a point estimate but a range of plausible values. Wider intervals indicate more uncertainty about a channel contribution; narrower intervals indicate higher confidence.

## Lift Test Integration

If you have run controlled experiments --- geo-lift tests, conversion lift studies, or randomized holdout tests --- Simba can incorporate those results as Bayesian priors that calibrate the model.

Lift tests are configured in **Step 5 (Model Details)** of the model creation wizard. For each lift test, you provide:

- **Channel**: Which media channel the test measured.
- **Baseline spend**: The spend level during the control period.
- **Spend change**: The change in spend during the test period.
- **Revenue change**: The observed incremental revenue from the test.
- **Sigma**: The uncertainty around the measurement (auto-calculated or manually set).
- **Cost mode**: Low, medium, or high confidence in the measurement.

Lift test results inform the model expectations about a channel effectiveness before it sees the observational data. This is especially valuable for channels with limited spend variation in historical data.

Integrating lift tests is optional but recommended. It bridges the gap between observational modeling and experimental evidence, producing more trustworthy attribution.

## Active Model Results

When a model completes, the Active Model page presents results across multiple tabs:

### Media Results

The primary performance summary:

- **Channel Performance Summary** --- Table of key metrics for each channel.
- **ROAS Bar Chart** --- Visual comparison of return on ad spend across channels.
- **ROI Analysis Panel** --- Detailed return on investment breakdown.
- **Quarterly ROI Analysis** --- Performance trends over quarters.
- **Spend vs Revenue** --- Scatter plot showing the relationship between spend and outcome for each channel.
- **Efficiency vs Effectiveness** --- Matrix chart positioning channels by both dimensions.

### Contributions

Channel contribution analysis with multiple views:

- **Stacked Area Chart** --- Time series showing how base sales and each channel contribution combine over time.
- **Waterfall Chart** --- Breakdown of contribution by channel for a selected period.
- **Year Comparison Chart** --- Year-over-year contribution comparison.
- **Driver Grouping** --- Custom contribution groups (see below).
- **Channel Color Customizer** --- Assign colors to channels for consistent visualization.

### Curves

Response curve analysis:

- **Revenue Curves** --- Nonlinear response curves showing revenue as a function of spend for each channel.
- **Marginal Revenue Curves** --- Incremental revenue from spending one more dollar, with the optimal spend point (where marginal revenue equals marginal cost) highlighted.
- **Decay Curves** --- Adstock decay visualization showing how each channel effect fades over time.
- **Statistics** --- Optimal spend, ROAS at equilibrium, and profit curves.

### Actual vs Model (AVM)

Model fit visualization:

- Line chart overlaying predicted revenue against actual revenue.
- **HDI confidence bands** at 50% and 95% showing prediction uncertainty.
- Coverage metric: percentage of actual values falling within the 95% HDI.

### Coefficients

Posterior coefficient estimates:

- **Table** showing mean, standard deviation, HDI 3%, HDI 97%, and R-hat convergence diagnostic for each parameter.
- **Coefficient Time Series Chart** with HDI bands showing how time-varying coefficients evolve.

### Model Stats

Diagnostic metrics:

- **R-squared** --- Model explained variance (above 0.7 is generally good).
- **MAPE** --- Mean Absolute Percentage Error (below 10% is excellent).
- **R-hat** --- Convergence diagnostic (near 1.0 indicates good convergence).
- Each metric includes an evaluation assessment (excellent, good, warning).

### Residuals

Residual analysis with residual plots and Q-Q plots for assessing distributional assumptions.

### AI Assistant

Interactive analysis powered by Claude AI. Ask questions in natural language and receive custom charts and analyses. See [AI Assistant](./ai-assistant.md).

### VAR-Specific Tabs

For models linked to a VAR model:

- **IRF Chart** --- Impulse Response Function heatmap.
- **Variance Decomposition** --- FEVD tables.
- **Long-Run Effects** --- Elasticities, C-multipliers, path decomposition, ROI, and NPV analysis. See [Long-Term Effects](./long-term-effects.md).

## Common Patterns and What They Mean

**Large base sales relative to media lift.** This is normal for established brands. It means most revenue comes from existing demand rather than marketing. The media channels are still valuable --- they are adding incremental revenue on top of a strong baseline.

**One channel dominates the media lift.** Check whether this reflects reality or a data artifact. If the dominant channel also has the most spend variation, the model has the most information to work with. Channels with flat, consistent spend are harder to measure and may appear less impactful than they truly are.

**A channel shows near-zero or negative estimated lift.** This does not necessarily mean the channel is worthless. It may mean the model cannot detect its effect given the available data. Consider whether the channel had enough spend variation during the measurement period, or whether a lift test could provide additional evidence.

**Seasonal patterns visible in base sales.** This is expected. The model separates seasonal demand from media impact, so you should see base sales rise and fall with natural demand cycles while media contributions reflect actual campaign performance.

## CSV Exports

Results can be downloaded as CSV files for offline analysis. Available exports include: contributions, media results, parameters, curves, posterior configuration grid, model stats, AVM, residuals, coefficients, IRF, FEVD, and long-run effects.

After reviewing measurement results, proceed to [Scenario Planning](./scenario-planning.md) to forecast how different budget allocations would affect future revenue.

---

## Model Lifecycle and Status

When you start a model fit, it progresses through a series of statuses:

| Status | Description |
|---|---|
| **Pending** | The model is queued and waiting for compute resources. |
| **Under Way** | Bayesian inference is actively running. You will see a progress indicator. |
| **Revoke in Progress** | A cancellation request has been submitted and is being processed. |
| **Complete** | The model has finished fitting successfully. Results are available for review. |
| **Failed** | The model encountered an error during fitting. Check the error message for details --- common causes include data issues, prior misconfiguration, or convergence problems. |
| **Revoked** | The model fit was manually cancelled by the user before completion. |
| **Time Exceeded** | The model fit exceeded the maximum allowed computation time. Consider reducing model complexity (fewer channels, wider priors, or weekly instead of daily data). |

You can navigate away from Simba during model fitting and return when it completes. The model status is visible in the Warehouse and on the Dashboard.

### Recovering from Failed Models

If a model fails, review the error message and consider:

- Checking your data for issues flagged by the Data Validator
- Adjusting priors that may be too narrow or contradictory
- Reducing the number of channels or control variables
- Switching from daily to weekly data granularity to reduce complexity

## Model Copying

Completed models that have been shared with you can be copied to your own workspace:

1. Find a shared model in your "Shared with me" section.
2. Click the copy action.
3. Simba creates a duplicate with all results, configuration, and contribution groups preserved.
4. The copy appears in your own model list with a new unique identifier.

Note: You can copy models shared with you by other users. To iterate on your own models, use the model creation wizard with similar settings or re-run with adjusted configuration.

## Custom Contribution Groups

By default, Simba shows individual channel contributions in the results dashboard. **Contribution Groups** let you create custom groupings that aggregate channels for higher-level reporting.

For example, you might group:

- Facebook, Instagram, and TikTok into "Paid Social"
- Google Search and Bing Search into "Paid Search"
- TV and Radio into "Traditional Media"

To configure contribution groups:

1. Open a completed model results page.
2. In the Contributions tab, use the Driver Grouping interface.
3. Create named groups, assign channels, and set group colors.
4. The contribution charts update to show grouped views.

Contribution groups are saved per model and persist across sessions. Channel colors set here are also synced to the Optimizer and Scenario Planner pages for consistent visualization.

---

## Next Steps

- [Scenario Planning](./scenario-planning.md) --- Forecast different budget allocations
- [Budget Optimization](./budget-optimization.md) --- Algorithmic budget allocation
- [Model Configuration](./model-configuration.md) --- Adjust priors and settings
- [Exports and Reporting](./exports-reporting.md) --- PDF reports and CSV downloads
