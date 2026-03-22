# Halo and Trademark Channels --- Configuring Cross-Brand Effects

This guide explains how to configure halo and trademark channels in Simba for multi-brand portfolio analysis. For the conceptual background, see [Halo Effects](../core-concepts/halo-effects.md).

---

## When to Use Halo and Trademark Channels

Configure these channels when:

- You have a **multi-brand portfolio** and suspect advertising for one brand influences sales of other brands.
- You run **masterbrand or corporate campaigns** that are not specific to a single brand.
- You want the optimizer to account for **cross-brand spillover** when allocating budget.

---

## Configuring Halo Channels

Halo channels are configured during the variable selection step of the model creation wizard.

### Automatic Detection

Simba uses **semantic detection with confidence scoring** to automatically suggest which channels might be halo channels. The system analyzes variable names and metadata to identify channels likely to generate cross-brand effects. Suggestions with a confidence score of 60% or higher are flagged for your review.

### Manual Configuration

You can manually mark any channel as a halo channel:

1. In the Variable Selection step, locate the channel you want to configure.
2. Enable the **halo channel** toggle.
3. Choose the scope:
   - **Per-brand**: The channel generates halo effects only for specific brands you select.
   - **Global**: The channel generates halo effects for all brands in the portfolio.

### Validation Rules

- At least one brand in the portfolio must **not** be a halo brand. You need at least one "primary" brand that is directly advertised.
- Halo channels must be associated with a brand that has direct spend data.

---

## Configuring Trademark Channels

Trademark channels represent portfolio-wide advertising.

### Automatic Detection

Simba's semantic matching detects three types of trademark channels:

- **Masterbrand**: Parent brand advertising (e.g., variable names containing "corporate", "brand", "umbrella").
- **Portfolio**: Product family advertising (e.g., variable names referencing product lines).
- **Corporate**: Company-level advertising (e.g., CSR, employer branding).

Detection uses confidence scoring, and suggestions above the threshold are flagged.

### Manual Configuration

1. In the Variable Selection step, locate the channel.
2. Enable the **trademark channel** toggle.
3. Trademark channels are **always global** --- they affect all brands equally. There is no per-brand option.

### Trademark Brands Mapping

The system tracks which virtual trademark channels map to which models in the portfolio via a `trademark_brands` mapping. This ensures the optimizer correctly attributes trademark spend across all relevant brands.

---

## How the Optimizer Handles Cross-Brand Effects

When running portfolio optimization with halo and trademark channels configured:

- The **optimizer objective function** accounts for both `halo_channels` and `trademark_channels`.
- Cross-brand spending effects are factored into the budget allocation.
- Halo channels receive credit for their **total portfolio impact**, not just their direct brand impact.
- Trademark channel budget is optimized against **total portfolio revenue** across all brands.

---

## Best Practices

- **Start with semantic suggestions** --- review Simba's automatic detection before manually configuring channels. The AI suggestions are calibrated to common naming patterns.
- **Use trademark channels for umbrella campaigns** --- if the campaign is not brand-specific, it is a trademark channel.
- **Use halo channels for brand-specific spillover** --- if Brand A's TV campaign lifts Brand B, mark Brand A's TV as a halo channel.
- **Review portfolio optimization results** to validate that cross-brand effects are being captured as expected. If results seem implausible, revisit your halo/trademark configuration.
- **Start simple** --- for your first portfolio model, use semantic suggestions without manual overrides. Refine in subsequent iterations based on results.

---

## Next Steps

- [Halo Effects](../core-concepts/halo-effects.md) --- Conceptual background on cross-brand marketing impact
- [Portfolio Analysis](./portfolio-analysis.md) --- Full portfolio analysis workflow
- [Budget Optimization](./budget-optimization.md) --- How halo/trademark effects change optimization
- [Model Creation Wizard](./model-creation-wizard.md) --- The full model setup process
