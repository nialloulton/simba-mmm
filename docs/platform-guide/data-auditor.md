# AI Data Auditor --- Automated Data Validation and Quality Scoring

The AI Data Auditor is the first step in the Simba workflow. Before any model runs, the auditor validates every connected data source, detects problems, and produces a single data health score that tells you whether your data is ready for modeling.

## What It Does

The auditor automatically inspects all uploaded or connected datasets and checks them against the requirements of a Bayesian Marketing Mix Model. It catches problems that would otherwise surface as poor model fit or unreliable results --- issues like missing spend data for key weeks, duplicated rows, inconsistent date formats, or sudden spikes that suggest logging errors rather than real performance changes.

## Why It Matters

Model quality depends entirely on data quality. A model trained on incomplete or corrupted data will produce attribution results and budget recommendations that look plausible but are wrong. The auditor prevents this by flagging issues before they propagate into downstream steps like [Incremental Measurement](./measurement.md) or [Budget Optimization](./budget-optimization.md).

## Data Health Score

After the audit completes, Simba assigns a **data health score** ranging from 0 to 100. This score reflects the overall readiness of your data for modeling.

| Score Range | Meaning |
|---|---|
| 90--100 | Excellent. Data is clean and ready for modeling with high confidence. |
| 70--89 | Good. Minor issues detected that are unlikely to affect results significantly. Review flagged items. |
| 50--69 | Fair. Several issues found. Address the flagged problems before relying on model outputs. |
| Below 50 | Poor. Significant data quality problems. Resolve critical issues before proceeding. |

The score is a weighted combination of completeness, consistency, freshness, and schema conformance. Each dimension is scored independently so you can see exactly where problems lie.

## Automated Validation Across Data Sources

The auditor validates each connected source independently and then checks cross-source consistency. Typical checks include:

- **Completeness**: Are there gaps in the time series? Missing values for key variables like spend, impressions, or revenue?
- **Consistency**: Do date ranges align across sources? Do channel names match between spend and performance data?
- **Freshness**: Is the most recent data point current, or has a data pipeline stopped updating?
- **Range checks**: Are numeric values within plausible bounds? Negative spend, zero impressions with nonzero clicks, or revenue values orders of magnitude outside historical norms are flagged automatically.

## Real-Time Anomaly Detection

The auditor applies statistical anomaly detection to every numeric column. It identifies:

- **Sudden spikes or drops** that deviate significantly from historical patterns, which may indicate tracking errors, campaign misattribution, or data pipeline issues.
- **Structural breaks** where the statistical properties of a series change abruptly, such as a mean shift in daily impressions that could signal a platform API change.
- **Outliers** that fall outside expected distributions, flagged with severity levels so you can distinguish between minor noise and critical errors.

Detected anomalies are shown inline alongside the affected data, with explanations of why each was flagged and suggested remediation steps.

## Schema Integrity Checks

Simba expects data in a specific structure. The schema integrity check verifies:

- Required columns are present (date, channel identifiers, spend, and target variable at minimum).
- Column data types are correct (dates are parseable, numeric fields contain numbers, categorical fields have consistent labels).
- No duplicate rows exist for the same date-channel combination.
- Column names match the expected naming conventions or have been mapped correctly.

Schema violations are reported as blocking errors --- the model will not run until they are resolved.

## Missing Value Handling

When gaps are detected, the auditor reports the location and extent of missing data and offers handling strategies:

- **Small gaps** (a few isolated missing values in an otherwise complete series) can be interpolated automatically using methods appropriate for time series data.
- **Systematic gaps** (an entire channel missing data for a stretch of weeks) are flagged for manual review since interpolation would be unreliable.
- **Structural missingness** (a channel that was not active during part of the modeling window) is handled by marking that channel as inactive for the affected period rather than imputing zeros.

The auditor documents every imputation it applies so you have full transparency into what was changed and why.

## How to Interpret the Audit Results

The audit results page shows:

1. **Overall health score** at the top, with a breakdown by dimension.
2. **Source-by-source status** showing which data sources passed and which have issues.
3. **Issue list** sorted by severity (critical, warning, informational), each with a description, the affected rows or columns, and a recommended fix.
4. **Data preview** for each source after any automated cleaning has been applied, so you can verify the results before proceeding.

Review critical issues first. Warnings are worth investigating but may not require action. Informational items are observations that could improve model accuracy if addressed but are not blocking.

## Tips for Improving Data Quality

- **Use consistent date formats and timezones** across all sources. Mixed formats are the most common cause of alignment errors.
- **Avoid manual edits to raw data files.** Use Simba's cleaning tools or fix issues at the source.
- **Check for platform-specific quirks.** Some ad platforms report spend with a one-day lag, or aggregate weekend data differently. Align reporting windows before uploading.
- **Include at least 52 weeks of data** when possible. Short time series reduce model reliability and make it harder for the auditor to distinguish anomalies from normal variation.
- **Re-run the audit after making changes.** The auditor is designed to be run iteratively until the health score reaches an acceptable level.

Once the audit passes, proceed to [Incremental Measurement](./measurement.md) to begin attribution analysis.
