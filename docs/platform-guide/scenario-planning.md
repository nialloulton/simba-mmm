# Scenario Planning --- Forecasting and What-If Analysis

Scenario Planning lets you explore how different budget allocations and market conditions affect future revenue. Using the [Bayesian model](../core-concepts/bayesian-modeling.md) fitted during [Incremental Measurement](./measurement.md), you create custom spend plans and generate revenue predictions with uncertainty bands powered by the full posterior distribution.

![Scenario Planning Workflow](./images/scenario-workflow.png)
*The scenario planning process: choose a mode, configure your budget, set allocation strategy, adjust control variables, generate predictions, and analyze the results dashboard.*

---

## Choosing a Planning Mode

When you open the Scenario Planner, you are presented with two planning modes. Both produce the same prediction output --- the difference is how you build the input plan.

![Monthly vs Advanced Planner](./images/planner-comparison.png)
*The Monthly Planner (left) walks you through a guided wizard. The Advanced Planner (right) gives you a full spreadsheet grid for week-by-week control.*

### Monthly Planner (Recommended)

A guided 6-step wizard designed for marketers who think in months. You set a total budget, configure channel costs, allocate by month, choose a within-month distribution strategy, optionally adjust non-media drivers, and set a revenue conversion multiplier.

**Best for:** Strategic planning, quick scenario exploration, users who prefer a structured flow.

### Advanced Planner

A full AG Grid spreadsheet editor where you control every value for every period (week or day). Media channels appear in white cells, control variables in yellow italic cells, and proxy channels in blue cells.

**Best for:** Detailed campaign planning, importing plans from Excel, users who need cell-level precision.

> Not sure which to choose? Start with **Monthly Planner** --- you can always switch to the Advanced Planner later, and the wizard output feeds directly into the advanced grid.

---

## Monthly Planner Wizard

The Monthly Planner is a 6-step wizard that converts high-level monthly budgets into period-level activity values for prediction.

### Step 1: Budget Configuration

Set your total marketing budget and review the planning period.

| Element | Description |
|---|---|
| **Total Budget** | The total amount to allocate across all channels and months |
| **Planning Period** | Auto-calculated from your selected horizon (1, 3, or 6 months). Weeks are grouped by calendar month, with partial months highlighted in amber |
| **Configuration Summary** | Shows total budget, duration, average per month, and total periods |

The planning period starts from the next period after your model's last data point. If your model data ends mid-month, the first planning month will be partial (fewer weeks) and is flagged accordingly.

### Step 2: Configure Channel Costs

Define how each channel's activity is measured and what it costs.

| Column | Description |
|---|---|
| **Channel** | Media channel name from your fitted model |
| **Metric Type** | How the channel is measured: Spend, Impressions, Clicks, GRP, or TRP |
| **Avg Cost** | Average CPM, CPP, or CPC. Editing this auto-fills all month columns |
| **Monthly columns** | Per-month cost overrides if costs vary seasonally |

Channels with metric type "Spend" do not require a cost column (spend is entered directly in Step 3).

Average costs are pre-filled from historical data when available. The system calculates cost-per-unit from your model's last year of data.

**Proxy channels** can be added at the bottom of this step. A proxy channel borrows the response curve of an existing reference channel, allowing you to model new channels (e.g., Podcasts) that were not in the original training data. Proxy channels appear with a blue highlight and a "(Proxy)" label.

### Step 3: Enter Monthly Budgets

Allocate spend to each channel for each month using an editable AG Grid.

| Column | Description |
|---|---|
| **Channel** (pinned) | Channel name |
| **Total Budget** (pinned, blue) | Total budget for this channel across all months. Editing this auto-distributes evenly across months |
| **Monthly columns** (green) | Per-month budget for this channel. Editing any month recalculates the channel total |

Partial months are shown with an amber background and include a "(Nw)" suffix showing the number of weeks in that month. Budget is distributed proportionally across the actual weeks in each month.

### Step 4: Choose Allocation Strategy

Select how each month's budget is distributed across the weeks (or days) within that month.

![Allocation Strategies](./images/allocation-strategies.png)
*Six allocation strategies control how monthly budgets are split into weekly (or daily) values.*

| Strategy | Behavior |
|---|---|
| **Equal Distribution** | Budget split evenly across all periods. Simple and balanced |
| **Business-Week Weighting** | Customizable weights for early, mid, and late month (sliders from 0.5x to 1.5x) |
| **Always-On** | Stable shares throughout the month for consistent media presence |
| **Pulsed** | High-Low-High pattern to create variation and maintain audience interest |
| **Launch Burst** | Front-loaded spending (40%, 30%, 20%, 10%) for product launches or campaign openings |
| **Event-Centric** | Peak spending concentrated in a specific week, ideal for promotions and events |

### Step 5: Business Scenario Adjustments (Conditional)

This step appears only if your model includes control variables (non-media drivers like pricing, distribution, or promotions). It lets you run "what-if" scenarios by adjusting these factors relative to their historical baseline.

![Control Variable Adjustments](./images/control-adjustments.png)
*Adjust non-media drivers by percentage. The KPI impact indicator shows whether each change helps or hurts predicted sales.*

Control variables are grouped into four categories:

| Category | Examples | Impact Direction |
|---|---|---|
| **Pricing** | Price index, unit cost | Higher price typically *decreases* sales |
| **Distribution** | Store count, availability | Higher distribution *increases* sales |
| **Promotional** | Promo depth, discount rate | More promotion *increases* sales |
| **Automatic** | Seasonality, trend, intercept | Read-only; auto-populated from historical patterns |

Each editable control has a slider (-50% to +50%) that adjusts the variable relative to its historical baseline mean. The "KPI" indicator to the right shows the expected impact direction based on the model's coefficient sign.

**Preset scenarios** are available for quick configuration:
- **Price +5%** --- Apply a 5% increase to all pricing variables
- **Distribution +10%** --- Apply a 10% increase to all distribution variables
- **Promo Push +20%** --- Apply a 20% increase to all promotional variables
- **Reset All** --- Return all adjustments to 0%

You can also **Skip** this step to use baseline (unadjusted) values for all controls.

### Step 6: Configure Revenue Conversion

Set a multiplier to convert the model's predicted target variable into revenue.

| Model Type | Multiplier Represents | Example |
|---|---|---|
| Volume/Units | Average price per unit | $25.00 |
| Customer Acquisition | Customer lifetime value (LTV) | $500.00 |
| Revenue/Sales | No conversion needed | 1.00 |

The multiplier can vary by month --- edit the "Avg Multiplier" column to auto-fill all months, then customize individual months if seasonal pricing applies.

After completing Step 6, the wizard converts your monthly budget plan into period-level rows (weekly or daily), merges control variables from historical data, and transitions you to the Advanced Planner grid for final review.

---

## Advanced Planner

The Advanced Planner presents a full AG Grid spreadsheet with one row per period (week or day) and columns for every variable in the model.

| Feature | Description |
|---|---|
| **Model info bar** | Shows last date, variable count, periodicity, and total periods |
| **Weekly Planning Grid** | Editable AG Grid with date rows and channel columns |
| **Save Grid** | Download the current grid as JSON for reuse |
| **Upload Grid** | Import a previously saved JSON grid (also supports CSV and Excel) |
| **Predict Results** | Submit the scenario for Bayesian prediction |

The grid is pre-filled using one of these sources (in priority order):
1. **Wizard data** --- If you came from the Monthly Planner, the wizard output populates the grid
2. **Last year data** --- Historical activity from the same period one year ago
3. **Empty template** --- A blank grid with the correct dates and channel names

**Cell color coding:**
- White cells --- Media channels (editable)
- Yellow italic cells --- Control variables (auto-filled from history, editable)
- Blue cells --- Proxy channels (editable)

**Tips:**
- Copy and paste from Excel using Ctrl+C / Ctrl+V
- Click a cell, type a value, press Enter to save, press Tab to move right
- Control variables are automatically populated from the previous year's data. Edit them only if you expect changes in pricing, distribution, or other non-media factors

---

## Generating Predictions

Scenario planning does **not** update forecasts in real time as you edit. Instead:

1. Configure your scenario in either the Monthly Planner wizard or the Advanced Planner grid.
2. Click **Predict Results** to queue the forecast.
3. The prediction runs asynchronously on the server. The UI polls for results every 5 seconds.
4. When complete, the Scenario Performance Dashboard appears with full visualizations.

Each prediction uses the full [Bayesian](../core-concepts/bayesian-modeling.md) posterior from your fitted model. The forecast applies the [adstock](../core-concepts/adstock-effects.md) and [saturation](../core-concepts/saturation-curves.md) transforms to your planned activity, then generates predictions with uncertainty bands from all posterior samples.

---

## Uncertainty Bands

Every forecast includes uncertainty bands showing the range of plausible outcomes:

![Forecast with Confidence Interval](./images/scenario-forecast.png)
*The forecast chart shows actual sales (cyan), predicted sales (purple dashed), and the 95% confidence interval (shaded band). The dashed vertical line marks the boundary between historical fit and forward projection.*

- The **prediction line** shows the median forecast from the Bayesian posterior.
- The **shaded band** shows the 95% credible interval --- the range within which the outcome will fall with 95% probability given the model and planned inputs.

Wider bands indicate greater uncertainty. This typically happens when:

- The forecast horizon extends further into the future
- Budget levels fall outside the range observed in historical data
- A channel has limited historical data to inform its [response curve](../core-concepts/saturation-curves.md)

---

## Scenario Results Dashboard

When predictions complete, a comprehensive results dashboard appears with multiple views.

![Results Dashboard](./images/results-overview.png)
*The results dashboard includes channel ROAS comparison (left), revenue decomposition waterfall (center), and efficiency scatter plot (right).*

### Prediction Summary

Three hero cards show the top-level forecast metrics (out-of-sample periods only):

| Card | Metric |
|---|---|
| **Total Predicted Sales** | Sum of predictions across all forecast periods |
| **Average Weekly Sales** | Mean prediction per period in the forecast window |
| **Growth vs Historical** | Percentage change between forecasted average and historical in-sample average |

### Sales Forecast Chart

An interactive time series chart showing:
- **Actual** values (cyan line) for in-sample periods
- **Prediction** values (indigo dashed line) for both in-sample and out-of-sample periods
- **95% confidence interval** (indigo shaded band) that widens over the forecast horizon
- A toggle to show/hide the confidence interval
- Filters to view All Data, In-Sample only, or Out-of-Sample only

### Media Performance Analysis

This section appears when spend data is available (from the Monthly Planner or when metric costs are configured):

| Component | Description |
|---|---|
| **Executive Summary** | Three gradient cards showing Total Investment, Predicted Return, and Portfolio ROAS with a quality rating (Excellent/Good/Below Target) |
| **Channel Performance Table** | Per-channel metrics: spend, contribution, ROAS, and share of total |
| **Channel ROAS Chart** | Horizontal bar chart comparing ROAS across all media channels |
| **Contribution Waterfall** | Stacked breakdown showing how each channel and non-media factor contributes to total predicted revenue |
| **Contribution Time Series** | Area chart showing how channel contributions evolve week by week |
| **Efficiency Scatter** | Spend vs. ROAS scatter plot with portfolio average reference line |

### Insight Cards

| Card | Content |
|---|---|
| **Top Performers** | Channels with the highest ROAS in this scenario |
| **Opportunities** | Optimization suggestions --- channels above or below portfolio average |
| **Weekly Breakdown** | Best and worst performing periods, plus consistency score |

### Additional Analysis

| Component | Description |
|---|---|
| **Control Contributions Card** | Shows the impact of Step 5 adjustments (pricing, distribution, promotional changes) on predicted revenue |
| **Proxy Spotlight** | Detailed performance of any proxy channels added during planning |
| **Export CSV** | Download the full prediction data (dates, actuals, predictions, confidence bounds, per-channel contributions) as a CSV file |

---

## Portfolio Scenario Planning

For portfolio models, scenario planning extends across multiple brands:

- Queue predictions for all brands in a portfolio simultaneously
- Each brand prediction uses its own fitted model
- The Monthly Planner supports portfolio mode with brand-level tabs in Step 3
- Revenue multipliers can be set per-brand in Step 6
- Results are aggregated at the portfolio level

See [Portfolio Analysis](./portfolio-analysis.md) for the full portfolio workflow.

---

## Using Scenarios for Budget Decisions

Scenarios are most useful when paired with a decision framework:

- **Marginal analysis**: Compare scenarios that differ by a single change (one channel budget increase) to isolate the expected impact of that change
- **Risk assessment**: Use the width of uncertainty bands to gauge confidence. Narrow bands suggest reliable forecasts; wide bands suggest more risk
- **Control variable testing**: Use Step 5 adjustments to model how changes in pricing, distribution, or promotions interact with your media plan
- **Threshold testing**: Set a revenue target and test which budget configurations achieve it within the confidence bands
- **Strategy comparison**: Run the same budget through different allocation strategies (Equal vs. Launch Burst vs. Pulsed) to see how within-month timing affects outcomes

After identifying your preferred budget plan, proceed to [Budget Optimization](./budget-optimization.md) to generate algorithmically optimized per-channel allocation recommendations.

---

## Next Steps

**Platform guides:**

- [Budget Optimization](./budget-optimization.md) --- Algorithmic budget allocation
- [Incremental Measurement](./measurement.md) --- The model results that power scenario forecasts
- [Model Configuration](./model-configuration.md) --- Adjust the underlying model
- [Portfolio Analysis](./portfolio-analysis.md) --- Cross-brand scenario planning

**Core concepts:**

- [Bayesian Modeling](../core-concepts/bayesian-modeling.md) --- How the posterior distribution drives uncertainty bands
- [Saturation Curves](../core-concepts/saturation-curves.md) --- Diminishing returns in media response
- [Adstock Effects](../core-concepts/adstock-effects.md) --- Carryover effects from media spend
- [Incrementality](../core-concepts/incrementality.md) --- Measuring true incremental impact
