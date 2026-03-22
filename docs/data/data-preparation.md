# Data Preparation — Cleaning and Formatting Best Practices

Good data preparation is the foundation of a reliable marketing mix model. This guide covers best practices for cleaning, formatting, and structuring your data before uploading it to Simba.

## Before You Start

Simba's [Data Validator](../platform-guide/data-auditor.md) can detect many data quality issues after upload. It is not automatic — you trigger it by clicking **Start Validator Agent** in the Warehouse configuration screen. However, addressing obvious problems beforehand leads to faster model setup and better results.

## Step 1: Consolidate Your Data Sources

Marketing data typically lives across multiple platforms. Gather data from:

- **Ad platforms** — Google Ads, Meta Ads Manager, TikTok Ads, DV360
- **TV buying systems** — GRP or spend data from your media agency
- **OOH platforms** — Out-of-home spend or impression data
- **Business systems** — Revenue, sales, or conversion data from your CRM, ERP, or analytics platform
- **External data** — Pricing, weather, economic indicators

Combine everything into a **single table** with consistent time periods.

## Step 2: Align Time Periods

All variables must share the same time granularity:

- If your revenue data is weekly, aggregate all media data to weekly totals
- Use **Monday-start weeks** (ISO standard) for consistency
- Ensure date formats are consistent (YYYY-MM-DD recommended)

### Common Pitfalls

- Media platforms may report on different day boundaries (e.g., Facebook uses PST)
- TV data may come in 4-week periods — convert to weekly
- Don't mix calendar months with ISO weeks

## Step 3: Handle Missing Values

| Scenario | Recommended Action |
|----------|-------------------|
| Channel had zero spend | Enter 0 (not blank) |
| Data is genuinely missing | Leave blank — the Data Validator will flag it |
| Channel didn't exist yet | Enter 0 for periods before launch |
| Temporary data gap (1–2 periods) | Interpolate if reasonable, or leave blank |

**Never fill missing values with averages** — this distorts the model's ability to measure impact during low/zero activity periods.

## Step 4: Standardize Units

- Use a **single currency** for all spend data (convert if needed)
- Keep impression data in consistent units (thousands, millions, or raw counts — just be consistent)
- Use the same revenue metric throughout (gross vs net — pick one)

## Step 5: Check for Anomalies

Before uploading, manually inspect your data for:

- **Spikes** — Unusually high spend or revenue periods (are they real or data errors?)
- **Zeros** — Unexpected zero values that should have data
- **Negative values** — Should not appear in spend data; may be valid for returns/refunds in revenue
- **Duplicates** — Overlapping time periods

## Step 6: Add Context Variables

Enrich your model with non-media variables that explain business outcomes:

- **Promotions** — Binary flags (0/1) for sale periods or use discount depth
- **Seasonality indicators** — Holiday flags, back-to-school, etc.
- **Pricing** — Price index or actual prices
- **Distribution changes** — New store openings, distribution expansions
- **External shocks** — Supply chain disruptions, competitor launches

## Final Checklist

Before uploading to Simba:

- [ ] All data is in a single CSV or Excel file
- [ ] First column is date (YYYY-MM-DD format)
- [ ] All columns have clear, descriptive headers
- [ ] Time granularity is consistent across all variables
- [ ] Zero spend is entered as 0, not blank
- [ ] No duplicate time periods
- [ ] Currency and units are consistent
- [ ] File size is reasonable (under 50MB)

## What Happens Next

After uploading your data, click **Start Validator Agent** in the Warehouse configuration screen to run the [Data Validator](../platform-guide/data-auditor.md). It will run 10 specialized checks across your dataset covering schema integrity, frequency diagnostics, alignment, multiplier logic, controls, coverage, outlier detection, multicollinearity, leakage, and documentation quality — then provide categorized findings and actionable recommendations.

→ **Next**: [Data Validation](data-validation.md) | [Data Requirements](data-requirements.md)

---

*See also: [Data Validator](../platform-guide/data-auditor.md) | [Supported Channels](supported-channels.md)*
