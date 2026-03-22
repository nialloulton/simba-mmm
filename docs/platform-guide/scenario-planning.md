# Scenario Planning --- Forecasting and What-If Analysis

Scenario Planning lets you explore how different budget allocations and market conditions would affect future revenue. Using the model fitted during [Incremental Measurement](./measurement.md), you create custom spend plans and generate revenue predictions with uncertainty bands.

---

## Getting Started

From the Scenario Planner page, choose one of two modes:

### Monthly Planner (Recommended)

A guided 6-step wizard for creating structured budget plans:

**Step 1: Budget Configuration** --- Set your total budget and select the planning period (1, 3, or 6 months).

**Step 2: Configure Channel Costs** --- Define cost metrics for each channel: CPM (cost per thousand impressions), CPP (cost per point), or cost-per-click. CPM can vary over time if needed.

**Step 3: Enter Monthly Budgets** --- Allocate monthly budgets to each channel. This is where you set the overall spend distribution across channels and months.

**Step 4: Choose Allocation Strategy** --- Select how each month budget is distributed across the weeks or days within that month:

| Strategy | Behavior |
|---|---|
| **Equal** | Distribute evenly across all periods |
| **Business Week** | Weight spend toward early, mid, or late week |
| **Always On** | Constant spend throughout |
| **Pulsed** | Varying intensity with peaks and troughs |
| **Launch Burst** | Front-loaded spike for product launches or campaign openings |
| **Event Centric** | Peak spend around a specific week or date |

**Step 5: Business Scenario Adjustments** (conditional) --- If your model includes control variables, adjust them here. Set percentage changes to pricing, distribution, promotional, or other control factors. Non-editable controls (seasonality, trend, intercept) are auto-populated from historical data.

**Step 6: Configure Revenue Conversion** --- Set revenue multipliers by month to account for expected changes in conversion rates or average order value.

### Advanced Planner

A manual grid editor for precise, period-by-period control:

- **Editable AG Grid table** with date rows and columns for each channel (media and control variables).
- Edit individual cells for granular week-by-week or day-by-day spend plans.
- Media channels shown in white, control variables in yellow (italic), proxy channels in blue.
- Add proxy channels to model channels not in the original model.
- Upload and download templates as JSON for reuse.

The template is auto-generated from the last year of your model data via the template-from-model endpoint, giving you a starting point based on actual historical spend patterns.

---

## Generating Predictions

Scenario planning does **not** update forecasts in real time as you edit. Instead:

1. Configure your scenario in either the Monthly Planner wizard or the Advanced Planner grid.
2. Click **Predict** to queue the forecast.
3. The prediction runs asynchronously. The system polls for results every 5 seconds.
4. When complete, the results dashboard appears with full visualizations.

Each prediction uses the full Bayesian posterior from your fitted model to generate forecasts with uncertainty bands.

---

## Uncertainty Bands

Every forecast includes **95% HDI (Highest Density Interval)** bands showing the range of plausible outcomes:

- The prediction line shows the median forecast.
- The shaded band shows the 95% credible interval --- the range within which the outcome will fall with 95% probability given the model.

Wider bands indicate more uncertainty. This typically happens when:

- The forecast horizon extends further into the future.
- Budget levels fall outside the range observed in historical data.
- A channel has limited historical data to inform its response curve.

---

## Scenario Results

When predictions complete, the results dashboard shows:

### Summary Views

- **Executive Summary** --- High-level KPI summary of the scenario outcome.
- **Forecasted Outcome** --- Total predicted revenue for the planning period.
- **Overall Prediction Summary** --- Statistics (total, average, growth) split between in-sample validation and out-of-sample forecast.

### Forecast Visualization

- **Forecast Chart** --- Prediction line with 95% HDI uncertainty bands overlaying the planning period. Shows both the historical fit (in-sample) and future projection (out-of-sample).

### Channel Analysis

- **Channel Performance Table** --- By-channel metrics including spend, contribution, and ROAS.
- **Channel ROAS Chart** --- ROAS comparison across channels for the scenario.
- **Contribution Waterfall** --- Breakdown of predicted revenue by channel.
- **Contribution Time Series** --- How each channel contribution evolves over the planning period.
- **Efficiency Scatter** --- Spend vs ROAS scatter plot highlighting efficient and inefficient channels.

### Detailed Breakdowns

- **Weekly Breakdown Card** --- Period-by-period view of predictions and contributions.
- **Control Contributions Card** --- Impact of control variable adjustments from Step 5 (shows the effect of pricing, distribution, or promotional changes).
- **Proxy Spotlight** --- Details on proxy channel contributions (if proxy channels were added).
- **Top Performers Card** --- Best-performing channels in the scenario.
- **Opportunities Card** --- Optimization suggestions based on the scenario results.
- **Scenario Insights** --- In-sample validation metrics, out-of-sample statistics, and top contributing factors.

---

## Portfolio Scenario Planning

For portfolio models, scenario planning extends across multiple brands:

- Queue predictions for all brands in a portfolio simultaneously.
- Each brand prediction uses its own fitted model.
- Results are aggregated at the portfolio level.

See [Portfolio Analysis](./portfolio-analysis.md) for the full portfolio workflow.

---

## Using Scenarios for Budget Decisions

Scenarios are most useful when paired with a decision framework:

- **Marginal analysis**: Compare scenarios that differ by a single change (one channel budget) to isolate the expected impact of that change.
- **Risk assessment**: Use the width of uncertainty bands to gauge confidence. Narrow bands suggest reliable forecasts; wide bands suggest the outcome is uncertain.
- **Control variable testing**: Use Step 5 adjustments to model how changes in pricing, distribution, or promotions interact with your media plan.
- **Threshold testing**: Set a revenue target and test which budget configurations achieve it within the uncertainty bands.

After identifying your preferred budget plan, proceed to [Budget Optimization](./budget-optimization.md) to generate precise per-channel allocation recommendations.

---

## Next Steps

- [Budget Optimization](./budget-optimization.md) --- Algorithmic budget allocation
- [Incremental Measurement](./measurement.md) --- The model results that power scenario forecasts
- [Model Configuration](./model-configuration.md) --- Adjust the underlying model
- [Portfolio Analysis](./portfolio-analysis.md) --- Cross-brand scenario planning
