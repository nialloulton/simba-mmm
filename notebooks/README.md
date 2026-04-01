# Build Your Own MMM Platform with PyMC-Marketing

**Open-source notebooks showing how to build Marketing Mix Modeling components from scratch using [PyMC-Marketing](https://github.com/pymc-labs/pymc-marketing).**

These notebooks are companion materials for the [Simba MMM documentation](https://nialloulton.github.io/simba-mmm/). Each notebook teaches a core concept with hands-on code, visualizations, and practical guidance.

## Learning Path

### Foundation (Start Here)

| # | Notebook | What You'll Learn | Docs Link |
|---|----------|-------------------|-----------|
| 01 | [Data Quality Checklist](01-data-quality-checklist.ipynb) | Validate your data before modeling: missing values, multicollinearity, outliers, frequency checks | [Data Validation](../docs/data/data-validation.md) |
| 02 | [Smart Priors from Data](02-smart-priors-from-data.ipynb) | Auto-generate informed priors from your data characteristics | [Priors & Distributions](../docs/core-concepts/priors-and-distributions.md) |
| 03 | [Bayesian VAR for Marketers](03-bayesian-var-for-marketers.ipynb) | Model long-term cross-channel effects with Vector AutoRegression | [VAR Modeling](../docs/core-concepts/var-modeling.md) |
| 04 | [Portfolio Budget Optimization](04-portfolio-budget-optimization.ipynb) | Optimize budgets across multiple brands with risk adjustment | [Budget Optimization](../docs/core-concepts/budget-optimization.md) |

### Enhanced Modeling

| # | Notebook | What You'll Learn | Docs Link |
|---|----------|-------------------|-----------|
| 05 | [Delayed Adstock](05-delayed-adstock.ipynb) | Model advertising effects that peak days or weeks after exposure | [Adstock Effects](../docs/core-concepts/adstock-effects.md) |
| 06 | [GP-Smoothed Events](06-gp-smoothed-events.ipynb) | Handle holidays and events with Gaussian Process smoothing | [Seasonality](../docs/core-concepts/seasonality.md) |
| 07 | [Time-Varying Coefficients](07-time-varying-coefficients.ipynb) | Allow media effectiveness to change over time with HSGP | [Bayesian Modeling](../docs/core-concepts/bayesian-modeling.md) |
| 08 | [Tanh Saturation Deep Dive](08-tanh-saturation-deep-dive.ipynb) | Understand the two-parameter tanh saturation function | [Saturation Curves](../docs/core-concepts/saturation-curves.md) |

### Production Workflows

| # | Notebook | What You'll Learn | Docs Link |
|---|----------|-------------------|-----------|
| 09 | [Model Diagnostics Checklist](09-model-diagnostics-checklist.ipynb) | Comprehensive post-fit model validation | [Measurement](../docs/platform-guide/measurement.md) |
| 10 | [Lift Test Calibration](10-lift-test-calibration.ipynb) | Integrate incrementality evidence as likelihood observations | [Incrementality](../docs/core-concepts/incrementality.md) |
| 11 | [Scenario Planning](11-scenario-planning.ipynb) | Run what-if budget scenarios with posterior uncertainty | [Scenario Planning](../docs/platform-guide/scenario-planning.md) |
| 12 | [Halo & Trademark Effects](12-halo-trademark-effects.ipynb) | Model cross-brand advertising spillover | [Halo Effects](../docs/core-concepts/halo-effects.md) |

### Integration & Advanced

| # | Notebook | What You'll Learn | Docs Link |
|---|----------|-------------------|-----------|
| 13 | [MMM-to-VAR Pipeline](13-mmm-to-var-pipeline.ipynb) | Combine short-term MMM with long-term VAR insights | [VAR Modeling](../docs/core-concepts/var-modeling.md) |
| 14 | [Semantic Channel Detection](14-semantic-channel-detection.ipynb) | Auto-classify media columns by channel type | [Supported Channels](../docs/data/supported-channels.md) |

## Requirements

```bash
pip install pymc-marketing matplotlib pandas numpy scipy scikit-learn
```

## Sample Data

The `data/` directory contains synthetic marketing datasets used across notebooks:

- `sample_mmm_weekly.csv` — 104 weeks of media spend + revenue for a single brand
- `sample_multi_brand.csv` — Multi-brand dataset for portfolio analysis

## About

Built by [PyMC Labs](https://www.pymc-labs.com/) as companion materials for [Simba MMM](https://www.simba-mmm.com/). The open-source [PyMC-Marketing](https://github.com/pymc-labs/pymc-marketing) library provides the foundation; these notebooks show you how to use it effectively.
