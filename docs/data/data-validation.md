# Data Validation — How the Data Validator Checks Your Data

Simba includes an AI-powered Data Validator that checks your uploaded dataset against the requirements of a Bayesian Marketing Mix Model. It catches problems that would otherwise surface as poor model fit or unreliable results.

## Why Data Validation Matters

The principle is simple: **garbage in, garbage out**. If your data contains errors, gaps, or inconsistencies, no statistical model — however sophisticated — can produce reliable insights. The Data Validator acts as a quality gate between your raw data and your model.

## How the Data Validator Works

The Data Validator is not automatic. After uploading your data in the Warehouse configuration screen, click **Start Validator Agent** to run it. You can choose between Haiku (faster) or Sonnet (more thorough) as the AI model powering the analysis. Validation typically takes 3 to 10 minutes depending on dataset size.

## What It Checks

The validator runs 10 specialized checks across your dataset:

### 1. Schema Validation

Checks that your data structure is valid:

- Date column is present and correctly formatted
- KPI (revenue/sales) column detected
- All columns have headers with consistent data types
- No structural issues (merged cells, hidden characters, encoding problems)

### 2. Frequency Diagnostics

Analyzes time series cadence:

- Confirms consistent weekly or daily intervals
- Detects plan-spreading patterns (e.g., even weekly splits of monthly budgets)
- Identifies gaps in the date sequence

### 3. Alignment

Checks that media and KPI variables align:

- Date ranges match across all variables
- No misaligned periods between spend and outcome data

### 4. Multiplier Validation

Validates multiplier columns for panel or hierarchical data:

- Checks multiplier column logic and consistency
- Verifies scaling relationships

### 5. Controls Validation

Reviews control variables:

- Appropriate variable types and variation
- Sufficient coverage across the modeling period

### 6. Coverage Analysis

Identifies gaps and inactive periods:

- Missing values by column and time period
- Zero-spend patterns and inactive channel periods
- Channels with insufficient variation

### 7. Outlier Detection

Flags statistical outliers using IQR (interquartile range — the spread between the 25th and 75th percentile of values)-based methods:

- Unusually high or low values on numeric columns
- Values that may indicate data errors vs genuine business events

### 8. Multicollinearity

Analyzes correlation between media channels:

- Variance Inflation Factor (VIF) analysis — VIF measures how much each channel's spend pattern overlaps with other channels; high VIF means the model struggles to tell channels apart
- Pairwise correlation detection between channels
- Flags channels that always spend together (model cannot distinguish their effects)

### 9. Leakage Detection

Checks for data leakage:

- Variables that could leak future information into the model
- Columns that are derived from the target variable

### 10. Documentation Audit

Reviews column naming and documentation quality:

- Column naming conventions
- Descriptive header quality

## Interpreting Results

The results modal displays findings in three severity levels:

| Severity | Meaning |
|----------|---------|
| **Errors** | Critical issues that should be resolved before modeling — e.g., missing KPI column, severe multicollinearity, data leakage |
| **Warnings** | Issues worth investigating — e.g., high outlier count, moderate channel correlation |
| **Info** | Observations and recommendations for improvement — e.g., naming suggestions, coverage notes |

Each issue includes:

- A description of the problem
- The affected columns and rows
- A specific recommendation for how to fix it
- The validation category it belongs to

When category-level insights are available, the modal also shows summary findings and action items grouped by validation category.

## Common Issues and Fixes

| Issue | Impact | Fix |
|-------|--------|-----|
| Missing KPI column | Blocking — model cannot fit without a target | Add a revenue or sales column |
| High VIF between channels | High — model cannot distinguish channel effects | Consider combining correlated channels or removing one |
| Plan-spreading pattern | Moderate — inflates contribution estimates | Use actual weekly spend data instead of evenly split monthly budgets |
| Missing values in media spend | Moderate — gaps reduce model accuracy | Fill with 0 if no spend occurred, or source the missing data |
| Outlier in revenue | Moderate — can skew model coefficients | Verify if real (e.g., Black Friday) or a data error; consider adding event flags |
| Low variation in a channel | Low — model cannot estimate impact well | Consider combining with similar channels |

## Tips for Clean Validation Results

1. **Prepare data carefully** before upload — see [Data Preparation](data-preparation.md)
2. **Use zero instead of blank** for periods with no activity
3. **Include at least 52 weeks** of history for reliable seasonal patterns
4. **Separate channels** where possible rather than combining
5. **Check for multicollinearity** — if two channels always spend together, the model cannot distinguish their effects

## Re-Running the Validator

You can re-run the Data Validator at any time after making changes to your uploaded data by clicking **Start Validator Agent** again. Validation results are displayed in the modal during your session and are not stored permanently.

→ **Next**: [Supported Channels](supported-channels.md) | [Data Requirements](data-requirements.md)

---

*See also: [Data Validator Guide](../platform-guide/data-auditor.md) | [Data Preparation](data-preparation.md)*
