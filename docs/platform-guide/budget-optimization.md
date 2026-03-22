# Budget Optimization --- Risk-Adjusted Spend Allocation

Budget Optimization generates per-channel budget recommendations that maximize expected revenue while respecting your risk tolerance, channel constraints, and spend timing preferences. It uses the full Bayesian posterior from your fitted model --- including response curves, saturation, adstock decay, and parameter uncertainty --- to find the optimal allocation.

---

## The Optimization Wizard

The optimizer uses a 6-step wizard (5 steps if optimizing a single period):

### Step 1: Budget and Risk

Configure the core optimization parameters:

- **Total Budget** --- The total amount to allocate across all channels.
- **Planning Period** --- Select 1 week, 1 month, 3 months, or a custom number of periods.
- **Risk Tolerance (Gamma)** --- A slider from 0.0 to 1.0 that controls how the optimizer balances expected return against uncertainty:
  - **0.0 (Risk-Seeking)**: Concentrates budget on the highest-performing channels regardless of uncertainty. Maximizes expected return.
  - **0.3--0.7 (Balanced)**: Moderate diversification. Balances expected return with stability.
  - **1.0 (Risk-Averse)**: Spreads budget to minimize variance. Prioritizes reliable channels over potentially higher-return but uncertain ones.
- **Warm Start** --- When enabled, accounts for historical spend carryover effects (adstock from previous periods carrying into the planning window).
- **Historical Effect** --- When enabled, includes residual effects from past media activity in the optimization.

The risk-adjusted objective function maximizes: `mean_response - gamma x std_response`. Low gamma values chase maximum return; high gamma values reduce volatility.

### Step 2: Configure Channel Costs

Define how each channel is costed:

- **Spend** --- Direct spend-based (no conversion needed).
- **Impressions** --- Set CPM (cost per thousand impressions). CPM can vary per period.
- **Clicks** --- Set CPC (cost per click).
- **GRP/TRP** --- Set CPP (cost per point).

Per-period cost columns let you account for seasonal CPM variation (e.g., higher costs during Q4).

### Step 3: Channel Constraints

Set minimum and maximum spend bounds for each channel as percentages of total budget:

- Default bounds are 5% minimum, 30% maximum per channel.
- Trademark channels and halo channels are detected from the model and shown separately.
- Adjust bounds to enforce business rules (contractual minimums, experimental channel caps, etc.).

### Step 4: Laydown Strategy (Multi-Period Only)

Choose how budget is distributed across the planning periods:

| Strategy | Behavior |
|---|---|
| **Equal** | Distribute evenly across all periods |
| **Front-Loaded** | Concentrate spend in early periods |
| **Back-Loaded** | Concentrate spend in later periods |
| **Custom** | User-defined per-period weights (must sum to 100%) |

This step is skipped when optimizing a single period.

### Step 5: Revenue Setup

Configure per-period revenue multipliers to convert model output to revenue:

- **Volume/Units models** --- Set average price per unit.
- **Customer models** --- Set customer lifetime value (LTV).
- **Revenue/Sales models** --- No conversion needed (use 1.0).

Multipliers can vary by period to account for seasonal pricing or expected conversion rate changes.

### Step 6: Review and Run

Review all configuration settings and click **Optimize**. A progress bar shows optimization progress (0--100%) with status messages.

---

## How the Optimizer Works

The optimizer uses **SLSQP (Sequential Least Squares Programming)** to solve for the budget allocation that maximizes the risk-adjusted objective across all posterior samples from the Bayesian model.

It accounts for:

- **Diminishing returns**: Each additional dollar spent on a channel produces less incremental revenue as the channel approaches saturation. The optimizer spreads budget across channels to capture the most efficient marginal returns.
- **Carryover effects**: Adstock decay curves mean that spend in one period continues generating response in subsequent periods. The results include carryover tail periods beyond the planning window.
- **Uncertainty**: The gamma parameter controls how much the optimizer penalizes channels with high variance in their posterior response estimates.
- **Constraints**: Per-channel percentage bounds, total budget constraint, and laydown weights are all enforced.

---

## Interpreting Optimization Results

The results page shows:

### Results Table

The main output table with one row per channel plus a Total row:

| Column | Description |
|---|---|
| **Channel** | Channel name |
| **Optimal Spend** | Recommended spend allocation |
| **Spend Share** | Percentage of total budget |
| **Response Share** | Percentage of total expected response |
| **Expected Response** | Mean response across posterior samples |
| **Revenue** | Expected revenue (response multiplied by multiplier) |
| **ROI** | Return on investment ratio |
| **Saturation** | Saturation level at the recommended spend |

### Share Donuts

Two donut charts showing:

- **Spend Share** --- How the budget is distributed across channels.
- **Response Share** --- How the expected response is distributed. Comparing these reveals which channels deliver disproportionate value relative to their budget share.

### Top Insights

The top 3 channels ranked by:

- Highest ROI
- Highest expected revenue
- Highest expected response

### Weekly Flighting Chart

A stacked bar chart showing the week-by-week (or day-by-day) spend and response distribution:

- **Weekly Spend** bars show how each channel budget is distributed across planning periods.
- **Weekly Response** bars show the expected response per period, including **adstock carryover tail** periods beyond the planning window (labeled as Tail 1, Tail 2, etc.). This visualizes how the effects of spend persist after the campaign ends.
- **Weekly Revenue** view is available via a metric toggle.

---

## Acting on Recommendations

Optimization results are recommendations, not automatic actions. To move from recommendation to execution:

1. **Review the recommendations** with your media team. Check whether the suggested changes are operationally feasible (minimum buys, platform constraints, creative availability).
2. **Apply business constraints** that the model may not know about. If there are contractual commitments or strategic mandates, add these as constraints in Step 3 and re-run the optimizer.
3. **Phase large changes.** If the optimizer recommends a major shift, consider implementing the change in stages and monitoring actual performance against the forecast.
4. **Close the loop.** After implementing the recommended allocation, feed the new performance data back into Simba. Run [Incremental Measurement](./measurement.md) to update attribution estimates, and the cycle continues.

---

## Portfolio Optimization with Halo and Trademark Effects

When optimizing at the portfolio level (available on Pro tier and above), the optimizer extends beyond single-brand allocation to account for cross-brand effects.

### Halo Channel Optimization

Halo channels generate incremental lift not just for their primary brand but for other brands in the portfolio. The optimizer gives halo channels credit for their **total portfolio impact**, which often results in higher recommended spend than a single-brand analysis would suggest.

### Trademark Channel Optimization

Trademark (masterbrand, portfolio, corporate) channels are treated as portfolio-wide investments. Their budget is optimized against the total revenue impact across all brands in the portfolio, not attributed to any single brand.

The optimizer solves for the allocation that maximizes **total portfolio revenue**, including:

- Direct channel effects within each brand
- Halo effects (brand-specific spillover)
- Trademark effects (portfolio-wide impact)

See [Halo and Trademark Channels](./halo-trademark-channels.md) for configuration details and [Portfolio Analysis](./portfolio-analysis.md) for the full portfolio workflow.

---

## Next Steps

- [Scenario Planning](./scenario-planning.md) --- Test budget scenarios before optimizing
- [Model Configuration](./model-configuration.md) --- Adjust the underlying model parameters
- [Incremental Measurement](./measurement.md) --- The attribution results that drive optimization
- [Portfolio Analysis](./portfolio-analysis.md) --- Cross-brand optimization
