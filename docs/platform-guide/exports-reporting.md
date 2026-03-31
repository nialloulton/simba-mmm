# Exports and Reporting --- PDF Reports, CSV Data, and Chart Images

Every model results tab in Simba supports both **PDF report generation** and **CSV data download**, giving you multiple ways to share findings with stakeholders and integrate with external tools. Additionally, Plotly charts offer built-in PNG export, and scenario/optimization results can be exported for offline analysis.

---

## PDF Reports

Every tab on the Active Model page has an **"Export to PDF"** button that generates a formatted report containing chart images and data tables.

**How it works:**
- Charts are captured as PNG images (Recharts via DOM capture, Plotly via its native export method)
- A progress bar shows capture progress (e.g., "Capturing Charts for PDF: 5/10 charts")
- The report is generated client-side and downloaded automatically
- **Filename format**: `{TabName}_Report_{modelId}_{date}.pdf`

### Available PDF Reports

| Tab | Report Contents |
|---|---|
| **Media Results** | Channel-level contribution charts, ROI metrics, spend/revenue breakdown |
| **Response Curves** | [Saturation curves](../core-concepts/saturation-curves.md) per channel with parameter summaries |
| **Contributions** | Time series decomposition showing each channel's contribution over time |
| **Coefficients** | [Posterior](../core-concepts/bayesian-modeling.md) coefficient estimates with 94% HDI bounds |
| **Model Statistics** | R², MAPE, convergence diagnostics, goodness-of-fit metrics |
| **Actual vs Model** | Time series overlay of actual vs predicted values |
| **Residuals** | Residual plots, ACF, Q-Q diagnostics |
| **Impulse Response** | [IRF](./long-term-effects.md) charts showing variable response to shocks (VAR models) |
| **Variance Decomposition** | [FEVD](./long-term-effects.md) pie and stacked bar charts (VAR models) |
| **Long-Run Effects** | Elasticities, long-term multipliers, and path breakdown (VAR models) |

---

## CSV Data Downloads

Every tab also has a **"Download CSV"** button that exports the underlying data for that view.

### Available CSV Exports

| CSV Type | Tab / Location | Contents |
|---|---|---|
| `media_results` | Media Results | Per-channel metrics: contribution, spend, revenue, ROI |
| `contributions` | Contributions | Time series of channel contributions |
| `parameters` | Response Curves | [Adstock](../core-concepts/adstock-effects.md) and [saturation](../core-concepts/saturation-curves.md) parameter estimates |
| `curves` | Response Curves | Response curve data points (spend vs predicted response) |
| `coefficients` | Coefficients | Posterior coefficient estimates with credible intervals |
| `model_stats` | Model Statistics | R², MAPE, DIC, convergence metrics |
| `avm` | Actual vs Model | Actual and predicted time series values |
| `residuals` | Residuals | Residual values and diagnostic statistics |
| `irf` | Impulse Response | IRF trace data per variable (VAR models) |
| `fevd` | Variance Decomposition | FEVD proportions per variable and horizon (VAR models) |
| `long_run_effects` | Long-Run Effects | Elasticities, multipliers, path breakdown data (VAR models) |
| `posterior_config_grid` | Model Configuration | Full [prior](../core-concepts/priors-and-distributions.md) configuration as CSV |
| `optimization_results` | [Budget Optimization](./budget-optimization.md) | Optimized allocation per channel per week |

> **Note**: Response Curves downloads a **ZIP file** containing two CSVs (`parameters.csv` + `curves.csv`).

---

## Chart Image Export

Charts built with Plotly.js include a built-in toolbar with a **"Download plot as PNG"** button. Hover over any Plotly chart to see the toolbar appear in the top-right corner.

**Charts with PNG export (Plotly.js):**
- Response Curves (revenue curves, marginal curves)
- Actual vs Model time series
- Residuals (time series, ACF, Q-Q plot)
- Impulse Response Function charts
- Variance Decomposition charts
- Portfolio Forecast (stacked area)

**Charts without individual PNG export (Recharts):**
- Contributions (stacked area/bar)
- Media Results charts
- Portfolio ROI charts

> Recharts charts cannot be exported individually as PNG, but they are captured and included in PDF reports.

---

## Optimization Exports

| Export | Format | Location | Contents |
|---|---|---|---|
| **Optimization Results** | CSV | Results header (Download icon) | Optimized spend per channel per week |
| **Laydown Weights** | CSV | Optimizer wizard → Laydown step | Weekly distribution weights |
| **Weekly Overrides Template** | CSV | Optimizer wizard → Weekly Overrides | Blank template for custom weekly allocations |

See [Budget Optimization](./budget-optimization.md) for the full optimization workflow.

---

## Scenario Exports

| Export | Format | Location | Contents |
|---|---|---|---|
| **Scenario Results** | CSV | [Scenario Planner](./scenario-planning.md) results header | Predicted revenue per channel per period |
| **Portfolio Scenario** | JSON | [Portfolio](./portfolio-analysis.md) scenario results | Full state: brand templates, results, budget allocation, timestamp |

The portfolio scenario JSON export includes everything needed to reproduce the scenario: all brand configurations, per-brand results, portfolio-level aggregates, and budget allocation details.

---

## Configuration Exports

These exports help you save and reuse model configurations across projects:

| Export | Format | Location | Contents |
|---|---|---|---|
| **Model Configuration** | JSON | Wizard → Model Details (Download Config) | Complete model setup: variables, [priors](../core-concepts/priors-and-distributions.md), transforms, options |
| **Lift Test Data** | JSON | Wizard → Lift Test Calibration (Export) | Lift test entries with channels, values, units, cost types |
| **Variable Selection** | JSON | Wizard → Variable Selection (Export) | Variable categorizations and assignments |

Configuration JSON files can be imported into a new model setup via the corresponding "Upload" or "Import" buttons.

---

## Next Steps

**Platform guides:**
- [Measurement](./measurement.md) --- Interpreting the model results you're exporting
- [Budget Optimization](./budget-optimization.md) --- Optimization workflow and results
- [Scenario Planning](./scenario-planning.md) --- Forecasting and what-if analysis
- [Model Configuration](./model-configuration.md) --- Configuration JSON details
- [Long-Term Effects](./long-term-effects.md) --- VAR-based exports (IRF, FEVD, LRE)

**Core concepts:**
- [Bayesian Modeling](../core-concepts/bayesian-modeling.md) --- Understanding posterior estimates in exports
- [Saturation Curves](../core-concepts/saturation-curves.md) --- Response curve data interpretation
- [Adstock Effects](../core-concepts/adstock-effects.md) --- Carryover parameters in exports
