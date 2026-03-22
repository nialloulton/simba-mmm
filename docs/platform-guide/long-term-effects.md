# Long-Term Effects --- Modeling Lasting Brand Impact

Standard Marketing Mix Models measure short-term media impact: the incremental revenue generated within a few weeks of spend. But some marketing activities --- brand campaigns, sponsorships, sustained awareness efforts --- produce effects that persist for months or longer. The Long-Term Effects module captures this extended impact using Vector AutoRegression (VAR) to trace how marketing spend flows through brand-building variables (awareness, consideration, equity) to ultimately drive revenue.

> **Availability**: Long-Term Effects is available on the **Pro tier and above**.

---

## What Long-Term Effects Are

Marketing impact operates on two timescales:

- **Short-term (performance)**: A paid search ad drives a click and a purchase this week. A promotional email generates orders within days. These effects are captured by the standard adstock decay parameters in [Model Configuration](./model-configuration.md).
- **Long-term (brand building)**: A TV brand campaign gradually shifts consumer awareness, making them more likely to purchase in future months. A sponsorship increases brand consideration that compounds over quarters. These effects extend well beyond the standard adstock window.

The Long-Term Effects module uses a [VAR model](./var-models.md) to capture these extended dynamics. By modeling the entire system of interactions --- how marketing drives brand metrics, and how brand metrics drive revenue --- Simba quantifies the full, cumulative impact of each channel over a configurable time horizon.

---

## How Long-Term Effects Work in Simba

Long-term effects are computed using a VAR (Vector AutoRegression) model that is linked to your standard MMM model.

### 1. Build a VAR Model

Create a VAR model that includes your revenue variable alongside brand-building variables such as awareness, brand consideration, or brand equity scores. The VAR estimates how each variable influences every other variable over time through lagged relationships.

### 2. Configure Long-Run Analysis

During VAR setup, you specify:

- **Base variable**: The primary outcome you care about (typically revenue or sales).
- **Equity variables**: The brand-building metrics that mediate long-term impact (e.g., awareness, brand consideration, unaided recall).
- **Horizon**: How many periods to trace cumulative effects (default: 156 weeks / 3 years).
- **Confidence interval**: The credible interval level for uncertainty bounds (default: 95%).

### 3. C-Multipliers and Impulse Response Functions

The system computes **C-multipliers** --- the cumulative long-run response of the base variable to a sustained unit change in each channel. This is derived from the VAR Impulse Response Functions (IRFs):

- For stationary VARs, an analytical formula provides exact long-run multipliers.
- For non-stationary or complex systems, iterative IRF computation traces effects over the configured horizon.

The C-multiplier tells you: if you permanently increase spend on a channel by 1%, what is the total cumulative percentage change in revenue after all dynamic effects have played out?

### 4. Path Decomposition

The total long-run effect of each channel is decomposed into:

- **Brand-mediated effects**: Impact that flows through equity variables. For example, TV spend increases awareness, which raises consideration, which drives more revenue. Each equity variable contribution is quantified separately.
- **Direct effects**: Impact that reaches revenue without going through brand metrics. This captures performance-oriented responses that bypass the brand-building pathway.

This decomposition reveals *how* each channel creates long-term value, not just *how much*.

---

## Interpreting Long-Term Effects Results

When a VAR model with long-run effects is complete, the results page shows five tabs:

### Tab 1: Elasticities

The primary results table showing each channel long-run elasticity:

| Channel | Elasticity | 95% CI | Via Awareness | Via Consideration | Direct |
|---|---|---|---|---|---|
| TV | 0.046 | [0.031, 0.060] | 65% | 20% | 15% |
| Search | 0.012 | [0.005, 0.019] | 10% | 5% | 85% |

- **Elasticity**: A 1% sustained increase in this channel spend produces an X% cumulative increase in revenue over the analysis horizon.
- **Confidence interval**: The range of plausible elasticity values, reflecting model uncertainty.
- **Via columns**: What percentage of the total effect flows through each equity variable.
- **Direct**: What percentage bypasses brand metrics entirely.

Channels with large via percentages are brand builders. Channels with large direct percentages are performance drivers.

### Tab 2: Long-Term Multipliers

Shows the C-multipliers for each equity variable:

- Format: A 1% sustained increase in the equity variable produces an X% cumulative effect on the base variable over the horizon.
- Also shows **own persistence** --- how much the base variable amplifies its own shocks over time.

### Tab 3: Path Decomposition

A visual breakdown showing, for each channel:

- The proportion of long-run impact flowing through each equity variable.
- The proportion of direct impact.
- Stacked bar charts with percentage attribution for easy comparison across channels.

This is the most actionable view for understanding *why* channels differ in their long-run effectiveness.

### Tab 4: Long-Run ROI (Optional)

When annual spend data is provided, this tab shows:

- Present value factors for long-run returns.
- Annual spend by channel.
- Net present value of long-run returns.
- Long-run ROI accounting for the full cumulative impact, not just short-term returns.

### Tab 5: NPV Scenarios (Optional)

When NPV configuration is provided (change percentage, years, discount rate), this tab shows:

- What happens to revenue NPV under sustained spend changes.
- Scenario comparisons for different levels of spend increase or decrease.
- Discounted cumulative returns over the specified time horizon.

---

## Linking VAR to MMM Models

Long-term effects are most valuable when combined with standard MMM results:

1. Build a standard MMM model for channel attribution and short-term optimization.
2. Build a VAR model with the same data plus brand metrics.
3. Link the VAR model to the MMM model.
4. The MMM results page is augmented with long-run elasticities, giving you both short-term attribution and long-term impact in one view.

This linked approach lets you use standard MMM for budget optimization while understanding the long-term brand implications of allocation decisions.

---

## Implications for Budget Optimization

When long-term effects are available, they inform budget decisions:

- **Brand-building channels** (high via-equity percentages) may warrant higher spend than short-term ROAS alone suggests, because their full return materializes over months.
- **Performance channels** (high direct percentages) deliver most of their value immediately and are well-captured by standard MMM optimization.
- **Cutting brand spend** saves money immediately but erodes the equity variables that support future revenue. The long-run elasticity quantifies exactly how much future revenue is at risk.
- **NPV analysis** helps justify brand investment to stakeholders by translating long-run effects into financial terms with appropriate discounting.

---

## Configuration Reference

| Setting | Description | Default |
|---|---|---|
| Base variable | Revenue or sales variable | Required |
| Equity variables | Brand-building metrics (awareness, consideration, etc.) | Required |
| Horizon | Number of periods for cumulative effects | 156 (3 years) |
| Confidence interval | Credible interval level | 0.95 (95%) |
| NPV discount rate | Annual discount rate for NPV calculations | Optional |
| NPV years | Time horizon for NPV scenarios | Optional |
| Annual base revenue | For ROI calculation | Optional |
| Annual spend | Per-channel annual spend for ROI | Optional |

---

## Next Steps

- [VAR Modeling](../core-concepts/var-modeling.md) --- The statistical foundation for long-run effects
- [VAR Models](./var-models.md) --- Building VAR models in Simba
- [Budget Optimization](./budget-optimization.md) --- How long-term effects influence allocation
- [Model Configuration](./model-configuration.md) --- Standard model prior configuration
