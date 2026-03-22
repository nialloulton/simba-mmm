# Halo Effects --- Cross-Brand Marketing Impact

In a multi-brand portfolio, advertising for one brand can lift sales of related brands. This cross-brand spillover is called a **halo effect**, and modeling it correctly is essential for accurate portfolio-level budget optimization.

---

## What Are Halo Effects?

A halo effect occurs when marketing activity for one brand or product generates incremental lift for other brands or products in the same portfolio. The "halo" extends beyond the advertised brand, benefiting siblings, sub-brands, or the parent brand.

### Common Examples

- **Masterbrand campaigns**: A corporate TV campaign for the parent brand (e.g., "Unilever") lifts sales across all sub-brands.
- **Flagship products**: Advertising a flagship product (e.g., iPhone) increases awareness and sales of the entire product line (iPad, Mac, Apple Watch).
- **Category association**: Advertising one cereal brand in a portfolio lifts the entire cereal category shelf presence and drives incremental sales of sister brands.
- **Retail foot traffic**: A promoted brand drives store visits, and shoppers buy other brands from the same company while in-store.

---

## Why Halo Effects Matter for MMM

Without modeling halo effects, cross-brand impact is invisible to the measurement system:

- **Undervalued channels**: A TV campaign that lifts three brands gets credit only for the one brand it directly advertised. Its true portfolio ROI is underestimated, potentially leading to budget cuts on a highly effective channel.
- **Misattributed growth**: The sales lift in non-advertised brands is attributed to whatever other marketing those brands were running at the time, inflating their apparent effectiveness.
- **Suboptimal allocation**: Portfolio-level budget decisions made without halo effects will under-invest in cross-brand channels and over-invest in brand-specific ones.

---

## How Simba Models Halo Effects

Simba captures cross-brand impact through two mechanisms:

### Halo Channels

A **halo channel** is a media channel whose spend for one brand generates incremental lift for other brands in the portfolio. Halo channels can be configured:

- **Per-brand**: The channel only generates halo effects for specific brands. For example, Brand A's TV campaign may lift Brand B but not Brand C.
- **Globally**: The channel generates halo effects for all brands in the portfolio.

### Trademark Channels

A **trademark channel** represents masterbrand, portfolio-level, or corporate advertising that benefits multiple brands simultaneously. Unlike halo channels (which are brand-specific spillover), trademark channels are treated as portfolio-wide investments.

Simba recognizes three types of trademark channels:

- **Masterbrand**: Parent brand advertising (e.g., "Samsung" campaigns that lift Galaxy phones, tablets, and wearables).
- **Portfolio**: Product family advertising (e.g., "Galaxy" campaigns that lift all Galaxy devices).
- **Corporate**: Company-level advertising (e.g., CSR campaigns, employer branding that has commercial spillover).

Trademark channels are **always global** --- they affect all brands in the portfolio equally.

---

## Impact on Optimization

When the optimizer accounts for halo and trademark effects, budget recommendations change meaningfully:

- **Halo channels receive higher recommended spend** because the optimizer gives them credit for their total portfolio impact, not just their direct brand impact.
- **Portfolio-level budget allocation** shifts toward channels with strong cross-brand effects, even if their single-brand ROI appears average.
- **Diversification increases** as the optimizer recognizes that some channels create value across the entire portfolio.

---

## Tier Availability

Portfolio features, including halo and trademark channel modeling, are available on Pro tier and above:

| Tier | Portfolio / Halo Support |
|------|--------------------------|
| Trial | No |
| Analyst | No |
| Pro | 1 portfolio |
| Scale | 2 portfolios |
| Enterprise | Unlimited |

---

## Next Steps

- [Halo and Trademark Channels](../platform-guide/halo-trademark-channels.md) --- Configure halo and trademark channels in Simba
- [Portfolio Analysis](../platform-guide/portfolio-analysis.md) --- Cross-brand comparison and optimization
- [Budget Optimization](../platform-guide/budget-optimization.md) --- How the optimizer uses halo effects
