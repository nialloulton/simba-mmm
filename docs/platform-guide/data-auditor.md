# Data Validator --- AI-Powered Data Validation

The Data Validator is an AI-powered validation tool that inspects your uploaded dataset and checks it against the requirements of a Bayesian Marketing Mix Model. It catches problems that would otherwise surface as poor model fit or unreliable results --- issues like missing spend data for key weeks, duplicated rows, multicollinearity between channels, or data leakage.

> **Note**: The Data Validator is not automatic. You trigger it manually from the Warehouse configuration screen by clicking **Start Validator Agent** after uploading your data file.

---

## How It Works

1. Upload your CSV or Excel file in the Warehouse configuration screen.
2. Click **Start Validator Agent** in the data source panel.
3. Choose a model for the validation: **Haiku** (faster, suitable for standard datasets) or **Sonnet** (more thorough, better for complex or messy data).
4. The validator runs asynchronously. A progress modal shows live status updates as the analysis proceeds.
5. When complete, a results modal displays all findings organized by severity.

The validator uses Claude AI with a specialized Data Validator skill that runs 10 category-specific checks against your data. Typical validation takes 3 to 10 minutes depending on dataset size and the model selected.

---

## What It Checks

The validator runs 10 specialized checks across your dataset:

| Category | What It Checks |
|---|---|
| **Schema** | Date and KPI column detection, required columns present, correct data types |
| **Frequency** | Time series cadence analysis --- confirms consistent weekly or daily intervals |
| **Alignment** | Media and KPI variable alignment --- date ranges match, no misaligned periods |
| **Multiplier** | Multiplier column validation for panel or hierarchical data |
| **Controls** | Control variable checks --- appropriate types, variation, and coverage |
| **Coverage** | Zero-spend patterns, missing data gaps, and inactive channel periods |
| **Outliers** | Statistical outlier detection using IQR-based methods on numeric columns |
| **Multicollinearity** | Variance Inflation Factor (VIF) and correlation analysis between media channels |
| **Leakage** | Data leakage detection --- variables that could leak future information into the model |
| **Documentation** | Column naming conventions and documentation quality audit |

---

## Interpreting Results

The results modal displays findings in three severity levels:

| Severity | Meaning |
|---|---|
| **Errors** | Critical issues that should be resolved before modeling. These indicate problems likely to produce unreliable results (e.g., missing KPI column, severe multicollinearity, data leakage). |
| **Warnings** | Issues worth investigating but not necessarily blocking. These may affect result quality if unaddressed (e.g., high outlier count in a channel, moderate correlation between channels). |
| **Info** | Observations and recommendations for improving data quality. Not blocking, but addressing them can improve model accuracy (e.g., column naming suggestions, coverage notes). |

Each issue includes:

- A description of the problem
- The affected columns or rows
- A specific recommendation for how to fix it
- The category it belongs to (schema, outliers, multicollinearity, etc.)

When category-level insights are available, the modal also shows summary findings and action items grouped by validation category.

---

## Applying Fixes

After reviewing validation results, you can:

- **Fix issues externally**: Edit your data file and re-upload it, then re-run the validator to confirm the fixes.
- **Use the Data Transformer**: From the validation results modal, you can trigger the Data Transformer skill to apply automated fixes for certain issues (e.g., removing outliers, handling missing values, reformatting columns).

Validation results are not stored permanently --- they are displayed in the modal during your session. Re-run the validator after making changes to confirm your data is ready.

---

## Tips for Clean Data

- **Use consistent date formats** across your file. Mixed formats are the most common cause of schema errors.
- **Include at least 52 weeks of data** when possible. Short time series reduce model reliability and make outlier detection less accurate.
- **Ensure spend variation per channel.** Channels with constant spend (no variation) cannot be reliably measured by any model.
- **Break out platforms individually** (e.g., Facebook and Instagram as separate columns rather than combined "Social") for more granular attribution.
- **Check for multicollinearity** before modeling. If two channels always spend together, the model cannot distinguish their effects. The validator flags this automatically.

---

## Next Steps

- [Data Requirements](../data/data-requirements.md) --- What data Simba needs for modeling
- [Data Preparation](../data/data-preparation.md) --- How to prepare your data before upload
- [Model Creation Wizard](./model-creation-wizard.md) --- Continue to model setup after validation
- [Incremental Measurement](./measurement.md) --- Interpreting model results
