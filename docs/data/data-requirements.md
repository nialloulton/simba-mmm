# Data Requirements — What Data You Need for Marketing Mix Modeling

To build an accurate marketing mix model in Simba, you need structured time-series data that captures your business outcomes and marketing activities. This guide explains exactly what data is required, what formats are supported, and how much history you need.

## Overview

Marketing mix modeling works by analyzing the relationship between your marketing inputs (spend, impressions, GRPs) and business outcomes (revenue, conversions, sales) over time. The more complete and accurate your data, the more reliable your model will be.

## Required Data

### 1. Target Variable (Dependent Variable)

Your primary business outcome that you want to measure marketing's impact on:

- **Revenue** — Total sales revenue per time period
- **Conversions** — Number of conversions, sign-ups, or transactions
- **Units sold** — Physical or digital units sold
- **Leads** — Number of qualified leads generated

You need **one target variable** per model. If you want to model multiple outcomes, create separate models.

### 2. Media Variables (Independent Variables)

Marketing activity data for each channel you want to measure:

| Data Type | Examples | Notes |
|-----------|----------|-------|
| **Spend** | Media spend in currency per period | Most common input |
| **Impressions** | Ad impressions served | Good for digital channels |
| **GRPs** | Gross Rating Points | Standard for TV |
| **Clicks** | Click-through data | Useful for search/display |
| **Reach** | Unique audience reached | For awareness campaigns |

### 3. Control Variables (Optional but Recommended)

Non-marketing factors that influence your target variable:

- **Pricing** — Product prices, discounts, promotions
- **Distribution** — Store count, availability, distribution changes
- **Competitors** — Competitor spend or activity (if available)
- **Economic indicators** — Consumer confidence, unemployment, GDP
- **Weather** — Temperature, precipitation (for weather-sensitive products)
- **Events** — Holidays, sporting events, cultural moments

## Data Format

### File Format

Simba accepts data in the following formats:

- **CSV** (.csv) — Comma-separated values (recommended)
- **Excel** (.xlsx) — Microsoft Excel format

### Structure

Your data should be in a **tabular format** with:

- **Rows** representing time periods (e.g., weeks)
- **Columns** representing variables (target, media channels, controls)
- **First column** should be the date/period identifier

Example structure:

| date | revenue | tv_spend | digital_spend | social_spend | ooh_spend | price_index |
|------|---------|----------|---------------|--------------|-----------|-------------|
| 2023-01-02 | 245000 | 50000 | 30000 | 15000 | 10000 | 1.00 |
| 2023-01-09 | 262000 | 50000 | 35000 | 15000 | 10000 | 1.00 |
| 2023-01-16 | 258000 | 45000 | 32000 | 18000 | 10000 | 0.95 |

## Time Granularity

- **Weekly data** is recommended for most use cases
- **Daily data** can work but may introduce noise
- **Monthly data** is acceptable but provides fewer data points for modeling
- All variables must use the **same time granularity**

## Minimum Data Requirements

| Requirement | Minimum | Recommended |
|-------------|---------|-------------|
| **Time periods** | 52 weeks (1 year) | 104+ weeks (2+ years) |
| **Media channels** | 1 | 3–10 |
| **Completeness** | No gaps longer than 2 consecutive periods | No gaps at all |
| **Variation** | Some spend variation per channel | Meaningful variation including periods of zero/low spend |

## Data Quality Tips

1. **Consistency** — Use the same units and currency throughout
2. **Completeness** — Fill gaps or mark them explicitly (Simba's Data Auditor will flag missing values)
3. **Accuracy** — Double-check that spend data reconciles with your media buying records
4. **Granularity** — More granular channel breakdowns (e.g., Facebook vs Instagram vs TikTok rather than "Social") yield better insights
5. **History** — More history = better seasonal modeling and more robust estimates

## What Simba's Data Auditor Checks

After upload, Simba's AI Data Auditor automatically validates your data:

- Missing values and gaps
- Anomalies and outliers
- Schema integrity
- Data health scoring
- Source validation

→ **Next**: [Data Preparation](data-preparation.md) | [Data Validation](data-validation.md)

---

*See also: [AI Data Auditor](../platform-guide/data-auditor.md) | [Supported Channels](supported-channels.md)*
