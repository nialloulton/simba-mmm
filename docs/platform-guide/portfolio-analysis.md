# Portfolio Analysis --- Cross-Brand and Cross-Model Insights

Portfolio Analysis enables cross-brand, cross-market, and cross-model comparison and optimization. Build individual models for each brand or market, link them into a portfolio, and analyze the combined picture to make portfolio-level decisions.

---

## Creating a Portfolio

1. Navigate to the **Warehouse > Portfolios** tab.
2. Click **Create Portfolio** and give it a descriptive name.
3. **Add models**: Select completed models to include in the portfolio. Each model typically represents a different brand, market, or product line.
4. **Link models**: Link the models together to enable cross-brand analysis.

Portfolios can contain models with different time periods, channel sets, and configurations. The analysis tools handle alignment automatically.

---

## Portfolio Analysis Tabs

The portfolio analysis page is organized into six tabs, each providing a different lens on your cross-brand data.

### 1. Model Statistics

Compare key metrics across all models in the portfolio:

- **Model fit**: R-squared, mean absolute error, and other goodness-of-fit metrics for each model.
- **Convergence diagnostics**: R-hat, effective sample size, and other Bayesian convergence indicators.
- **Data coverage**: Time period, number of observations, and number of channels per model.

Use this tab to identify models that may need reconfiguration or additional data.

### 2. Response Curves

Overlay and compare saturation response curves across brands and models:

- See which channels have more **headroom** (room to increase spend before hitting diminishing returns) in each brand.
- Identify channels that are **saturated** in one brand but still have capacity in another.
- Compare the shape and steepness of response curves to understand how channel dynamics differ across brands.

### 3. Portfolio Optimizer

Optimize budget allocation within a single brand's channels, but in the context of the broader portfolio. The optimizer considers how budget changes for one brand might affect portfolio-level outcomes through halo effects.

### 4. Cross-Brand Optimizer

Optimize budget allocation **across all brands and channels simultaneously**:

- The optimizer solves for the allocation that maximizes **total portfolio revenue**, not just individual brand revenue.
- **Halo effects**: Channels that generate cross-brand spillover receive credit for their total portfolio impact.
- **Trademark channels**: Portfolio-wide advertising budget is allocated based on its impact across all brands.
- Set constraints per brand and per channel.

This is the most powerful optimization mode, but requires halo and trademark channels to be properly configured. See [Halo and Trademark Channels](./halo-trademark-channels.md).

### 5. ROI Analysis

Compare return on ad spend across brands and channels:

- Identify the most and least efficient investments across the portfolio.
- Compare ROAS by channel across brands to find where each channel performs best.
- Spot opportunities to shift budget from low-ROI brand-channel combinations to high-ROI ones.

### 6. Scenario Planner

Run portfolio-level scenarios to forecast revenue across all brands under different budget allocations:

- Create scenarios that shift budget between brands, not just between channels.
- Compare portfolio-level forecasts with uncertainty bands.
- Test strategic questions like "What happens if we shift 20% of Brand A's budget to Brand B?"

---

## Portfolio Sharing

Portfolios can be shared with other users for collaborative analysis:

- Share a portfolio to grant access to the portfolio view and all linked models.
- Manage share permissions independently of individual model shares.

See [Sharing and Collaboration](./sharing-collaboration.md).

---

## Tier Availability

Portfolio analysis is available on Enterprise and Managed plans. For details, see [Pricing](../pricing/README.md).

---

## Next Steps

- [Halo Effects](../core-concepts/halo-effects.md) --- Understanding cross-brand marketing impact
- [Halo and Trademark Channels](./halo-trademark-channels.md) --- Configure cross-brand effects
- [Budget Optimization](./budget-optimization.md) --- Single-brand optimization details
- [Sharing and Collaboration](./sharing-collaboration.md) --- Collaborative workflows
