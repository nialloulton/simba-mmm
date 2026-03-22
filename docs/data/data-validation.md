# Data Validation — How Simba's AI Auditor Validates Your Data

Simba includes an AI-powered Data Auditor that automatically validates and scores your data before modeling begins. This ensures your inputs are trustworthy and your model results are reliable.

## Why Data Validation Matters

The principle is simple: **garbage in, garbage out**. If your data contains errors, gaps, or inconsistencies, no statistical model — however sophisticated — can produce reliable insights. Simba's Data Auditor acts as a quality gate between your raw data and your model.

## How the Data Auditor Works

When you upload data to Simba, the AI Data Auditor runs a comprehensive validation pipeline:

### 1. Schema Validation

The auditor checks that your data structure is valid:

- Date column is present and correctly formatted
- All columns have headers
- Data types are consistent (numbers are numbers, dates are dates)
- No structural issues (merged cells, hidden characters, encoding problems)

### 2. Completeness Check

The auditor identifies gaps in your data:

- Missing values by column and time period
- Gaps in the date sequence (skipped weeks/periods)
- Channels with insufficient variation
- Periods where all media activity is zero

### 3. Anomaly Detection

The auditor flags statistical outliers and suspicious patterns:

- Unusually high or low values relative to historical patterns
- Sudden step-changes that may indicate data source issues
- Repeated identical values that suggest copy-paste errors
- Negative values where only positive values are expected

### 4. Source Validation

Cross-checks across your data sources:

- Verifies consistency between related variables
- Flags when channel spend and impression data don't align
- Checks that totals reconcile

## The Data Health Score

After validation, Simba assigns your dataset a **Data Health Score** from 0–100%:

| Score | Rating | Meaning |
|-------|--------|---------|
| 90–100% | Excellent | Data is high quality, ready for modeling |
| 75–89% | Good | Minor issues detected, model will be reliable |
| 50–74% | Fair | Several issues found, review recommendations |
| Below 50% | Needs Work | Significant data quality issues, address before modeling |

## Interpreting Audit Results

The Data Auditor provides actionable results for each issue found:

- **Issue description** — What was detected
- **Severity** — How much it impacts model quality
- **Location** — Which column(s) and row(s) are affected
- **Recommendation** — Suggested action to resolve the issue

## Common Issues and Fixes

| Issue | Impact | Fix |
|-------|--------|-----|
| Missing values in media spend | Moderate — gaps reduce model accuracy | Fill with 0 if no spend occurred, or source the missing data |
| Outlier in revenue | High — can skew model coefficients | Verify if real (e.g., Black Friday) or a data error |
| Inconsistent time periods | High — breaks time-series alignment | Standardize all data to the same granularity |
| Low variation in a channel | Low — model can't estimate impact well | Consider combining with similar channels |

## Tips for a High Health Score

1. **Prepare data carefully** before upload — see [Data Preparation](data-preparation.md)
2. **Use zero instead of blank** for periods with no activity
3. **Verify source data** against original platforms before export
4. **Include at least 2 years** of history for robust seasonal patterns
5. **Separate channels** where possible rather than combining

## Re-Running the Audit

You can re-run the Data Auditor at any time after making changes to your uploaded data. The score updates in real time as data quality improves.

→ **Next**: [Supported Channels](supported-channels.md) | [Data Requirements](data-requirements.md)

---

*See also: [AI Data Auditor Guide](../platform-guide/data-auditor.md) | [Data Preparation](data-preparation.md)*
