# Budget Optimization --- Risk-Adjusted Spend Allocation

Budget Optimization is the fourth and final step in the Simba workflow. After [Scenario Planning](./scenario-planning.md) identifies your preferred direction, the optimizer generates precise per-channel budget recommendations that maximize expected revenue while respecting your risk tolerance and practical constraints.

## How the Optimizer Works

The optimizer takes the full Bayesian model --- including each channel's response curve, saturation point, adstock decay, and uncertainty estimates --- and solves for the budget allocation that maximizes expected incremental revenue given a total budget constraint.

Unlike simple ROI ranking (which would dump all budget into the highest-ROI channel), the optimizer accounts for:

- **Diminishing returns**: Each additional dollar spent on a channel produces less incremental revenue as the channel approaches saturation. The optimizer spreads budget across channels to capture the most efficient marginal returns.
- **Carryover effects**: Spend this week continues to generate impact in subsequent weeks. The optimizer factors this into allocation timing.
- **Uncertainty**: Channels with highly uncertain response curves are treated differently than channels with well-measured effects, depending on your risk settings.
- **Constraints**: Minimum and maximum spend per channel, total budget caps, and any business rules you define (for example, a contractual minimum with a media partner).

## Risk-Adjusted Optimization Explained

Standard optimization maximizes expected (average) revenue. Risk-adjusted optimization goes further by incorporating the uncertainty around each channel's effectiveness.

Two channels might have the same expected incremental revenue per dollar, but one might have a tight confidence interval (consistent results) while the other has a wide interval (sometimes great, sometimes poor). A risk-adjusted optimizer will favor the consistent channel unless you explicitly choose a higher risk tolerance.

Simba lets you set a risk appetite level:

- **Conservative**: Prioritizes channels with well-measured, reliable effects. Sacrifices some expected upside to reduce the chance of underperformance.
- **Balanced**: Weights expected return and uncertainty equally. This is the default and is appropriate for most situations.
- **Aggressive**: Maximizes expected return even if it means relying on channels with wider uncertainty bands. Appropriate when the upside of a successful campaign justifies the risk of underperformance.

## Multi-Week Carryover-Aware Allocation

Marketing spend does not produce impact only in the week it is deployed. TV advertising, for example, may generate response for three to six weeks after airing. Digital display ads may have a shorter but still measurable carryover.

The optimizer uses each channel's estimated adstock decay curve (configured in [Model Configuration](./model-configuration.md)) to plan across multiple weeks:

- **Front-loading**: Channels with long carryover benefit from earlier spend, since their effects accumulate over time. The optimizer may recommend concentrating spend for these channels in earlier weeks.
- **Pacing**: Channels with short carryover need sustained spend to maintain their impact. The optimizer distributes budget more evenly for these channels across the planning window.
- **Interaction effects**: When one channel's carryover overlaps with another's active spend period, the optimizer accounts for the combined effect rather than treating each channel in isolation.

The result is a week-by-week allocation plan, not just a single total per channel.

## Per-Channel Recommendations

The optimizer produces a recommendation table showing:

| Channel | Current Spend | Recommended Spend | Change | Expected Lift | Confidence |
|---|---|---|---|---|---|
| Example row | $50,000 | $62,000 | +24% | +$180,000 | High |

For each channel, you see:

- **Current spend**: What you are spending now (or in the scenario you selected).
- **Recommended spend**: The optimizer's suggested allocation.
- **Change**: The absolute and percentage difference.
- **Expected incremental lift**: The projected additional revenue from following the recommendation.
- **Confidence level**: Based on the width of the posterior distribution for that channel's response curve. High confidence means the model is relatively certain about the expected lift; low confidence means there is meaningful risk that actual results could differ.

## Balancing ROI with Risk Appetite

The optimizer does not simply recommend putting all budget into the highest-ROI channel. Several factors prevent this:

- **Saturation**: The highest-ROI channel at current spend levels may become the lowest-ROI channel if you triple its budget. The optimizer finds the allocation where marginal ROI is equalized across channels.
- **Diversification**: Concentrating budget in a single channel increases exposure to platform-specific risks (algorithm changes, audience fatigue, supply constraints). The risk-adjusted optimizer naturally diversifies unless one channel is overwhelmingly superior.
- **Measurement reliability**: Channels with limited historical spend variation have wider uncertainty bands. The optimizer discounts these channels proportionally to their uncertainty under conservative and balanced risk settings.

If the optimizer recommends a large shift toward a single channel, review the confidence level for that channel carefully. A large recommended increase paired with low confidence may warrant running a lift test before committing full budget.

## Interpreting Optimization Results

The results page includes:

1. **Recommended allocation summary**: The table described above, showing per-channel recommendations.
2. **Expected revenue impact**: The total projected revenue under the recommended allocation compared to the current allocation, including uncertainty bands.
3. **Efficiency frontier chart**: A curve showing the tradeoff between total budget and expected revenue. Your current position is marked, along with the recommended position. This shows whether you are underspending (below the frontier), overspending (past the point of diminishing returns), or misallocating (below the frontier at the same total budget).
4. **Week-by-week plan**: The multi-week allocation schedule showing how spend should be distributed over the planning window.
5. **Sensitivity analysis**: How much the recommendation changes if key assumptions shift. For example, if a channel's response curve is 20% weaker than estimated, does the optimal allocation change significantly?

## Acting on Recommendations

Optimization results are recommendations, not automatic actions. To move from recommendation to execution:

1. **Review the recommendations** with your media team. Check whether the suggested changes are operationally feasible (minimum buys, platform constraints, creative availability).
2. **Apply business constraints** that the model may not know about. If there are contractual commitments, brand safety requirements, or strategic mandates (such as maintaining presence in a specific channel regardless of ROI), add these as constraints and re-run the optimizer.
3. **Phase large changes.** If the optimizer recommends a major shift (for example, cutting one channel by 50% and doubling another), consider implementing the change in stages and monitoring actual performance against the forecast.
4. **Close the loop.** After implementing the recommended allocation, feed the new performance data back into Simba. The [AI Data Auditor](./data-auditor.md) will validate the incoming data, [Incremental Measurement](./measurement.md) will update attribution estimates, and the cycle continues.

For details on the underlying model parameters that drive optimization, see [Model Configuration](./model-configuration.md) and [Smart Defaults](./smart-defaults.md).
