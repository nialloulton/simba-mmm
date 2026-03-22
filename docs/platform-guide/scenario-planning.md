# Scenario Planning --- Forecasting and What-If Analysis

Scenario Planning is the third step in the Simba workflow. After [Incremental Measurement](./measurement.md) establishes each channel's causal impact, this step lets you explore how different budget allocations and market conditions would affect future revenue.

## Multi-Scenario Forecasting

Simba generates three default forecast scenarios that bracket the range of likely outcomes:

- **Aggressive**: Assumes favorable market conditions, higher media effectiveness, and optimistic response curves. This represents an upper-bound estimate of what your marketing investment could deliver.
- **Base**: Uses the model's best estimates for all parameters. This is the most likely outcome given current data and reflects a continuation of recent trends and media effectiveness.
- **Conservative**: Assumes less favorable conditions, lower media responsiveness, and tighter saturation curves. This represents a lower-bound estimate and is useful for risk planning.

All three scenarios are generated from the same underlying Bayesian model by sampling different regions of the posterior distribution. The aggressive scenario draws from the optimistic tail; the conservative scenario draws from the pessimistic tail; the base scenario uses the median estimates.

You can also create custom scenarios by adjusting specific parameters, budget levels, or market assumptions beyond the three defaults.

## Uncertainty Bands and Confidence Intervals

Every forecast in Simba includes uncertainty bands that show the range of plausible outcomes, not just a single line. These bands are derived from the posterior predictive distribution of the Bayesian model.

- **Inner band (50% credible interval)**: The outcome will fall within this range about half the time. This represents the core range of likely results.
- **Outer band (90% credible interval)**: The outcome will fall within this range about 90% of the time. This captures most realistic possibilities, including moderately optimistic and pessimistic outcomes.

Wider bands indicate more uncertainty. This typically happens when:

- The forecast horizon extends further into the future.
- A channel has limited historical data to inform its response curve.
- Budget levels in the scenario fall outside the range observed in historical data (extrapolation is inherently less certain than interpolation).

Use the width of the bands to calibrate how much confidence to place in a given scenario's projections.

## What-If Budget Reallocation

The what-if tool lets you adjust channel budgets and immediately see the projected impact on revenue. You can:

- **Shift budget between channels**: Move spend from a saturated channel to one with more headroom and see the projected net effect.
- **Increase or decrease total budget**: Test what happens if overall marketing spend goes up 20% or down 15%.
- **Add or remove channels**: Model the impact of launching a new channel or pausing an existing one.
- **Change timing**: Shift spend earlier or later in the planning period to explore the effect of pacing on projected revenue.

Each adjustment updates the forecast in real time, including the uncertainty bands. This lets you iterate quickly through dozens of allocation strategies without waiting for a new model run.

## How to Create and Compare Scenarios

1. **Start from the base scenario.** The base forecast is generated automatically from your measurement results and current budget levels.
2. **Duplicate and modify.** Create a copy of any scenario and adjust the budget inputs. Give each scenario a descriptive name (for example, "Shift 30% from TV to Digital" or "Q3 Aggressive Push").
3. **Compare side by side.** The comparison view overlays multiple scenarios on the same chart, showing projected revenue, channel contributions, and uncertainty bands for each. A summary table highlights the differences in total revenue, per-channel spend, and projected ROI.
4. **Save and share.** Scenarios persist in your project and can be shared with stakeholders for review.

When comparing scenarios, pay attention to where the uncertainty bands overlap. If two scenarios have overlapping bands, their projected outcomes are not statistically distinguishable --- the difference in expected revenue may not be reliable enough to drive a decision.

## Using Scenarios for Budget Decisions

Scenarios are most useful when paired with a decision framework:

- **Best case / worst case framing**: Use the aggressive and conservative scenarios to understand the upside potential and downside risk of a budget plan.
- **Marginal analysis**: Compare scenarios that differ by a single change (one channel's budget) to isolate the expected impact of that change.
- **Risk tolerance alignment**: If your organization is risk-averse, weight decisions toward scenarios where the conservative projection still meets targets. If the team has more appetite for risk, the aggressive scenario's upside may justify a bolder allocation.
- **Threshold testing**: Set a revenue target and test which budget configurations achieve it under base and conservative conditions. This identifies the minimum investment needed to hit a goal with reasonable confidence.

## Revenue Forecast Interpretation

The revenue forecast chart shows projected total revenue over time for each scenario. Key elements to review:

- **Trajectory**: Is revenue projected to grow, flatten, or decline? The shape of the curve matters as much as the endpoint.
- **Seasonality**: Forecasts incorporate seasonal patterns learned from historical data. Expect peaks and troughs that mirror past cycles unless you have modeled a structural change.
- **Channel decomposition within the forecast**: You can drill into any scenario to see which channels contribute how much to the projected revenue. This shows not just total revenue but where it comes from.
- **Divergence between scenarios**: The point where the aggressive and conservative projections diverge most is where uncertainty is highest and where your budget decisions have the most leverage.

After identifying your preferred scenario, proceed to [Budget Optimization](./budget-optimization.md) to generate precise per-channel allocation recommendations.
