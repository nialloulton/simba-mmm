# Model Configuration

The Model Configuration wizard guides you through a five-step process to build a [Bayesian](../core-concepts/bayesian-modeling.md) Marketing Mix Model or Vector Autoregression model. Each step collects specific inputs that determine how the model is structured, what [priors](../core-concepts/priors-and-distributions.md) are applied, and how media effects are parameterized.

## Wizard Overview

The configuration workflow consists of five sequential steps:

| Step | Name | Purpose |
|------|------|---------|
| 1 | **Data Source Configuration** | Upload CSV data, preview columns, and optionally run the Data Validator |
| 2 | **Model Setup** | Choose between Marketing Mix Model (MMM) and Vector Autoregression (VAR) |
| 3 | **Variable Selection** | Assign each column a role: Date, KPI, Media, Cost, Control, Multiplier, or Hierarchy |
| 4 | **Prior Builder** | Configure prior distributions in Standard (AI-driven) or Custom (manual) mode |
| 5 | **Model Details** | Set model name, likelihood, train/test split, advanced options, and build |

Each step must be completed before proceeding to the next. You can navigate back to any previous step to modify your selections.

---

## Step 1: Data Source Configuration

Upload your dataset in **CSV format** (50 MB maximum; Excel files are not supported). The upload panel accepts drag-and-drop or file browser selection.

After uploading, the right panel shows a data preview with column headers and the first rows of your dataset. This preview confirms that your file was parsed correctly and that columns are recognized.

### Actions available at this step

| Action | Description |
|--------|-------------|
| **Use Demo File** | Loads a built-in two-year weekly marketing dataset for exploration |
| **Start Validator Agent** | Runs the Data Validator, an AI agent that checks your dataset for 10 categories of issues (schema, frequency, alignment, multiplier, controls, coverage, outliers, multicollinearity, leakage, documentation). Choose between Claude Haiku (fast, 2-3 min) or Claude Sonnet (deep analysis, 4-6 min) |
| **Continue to Model Selection** | Proceeds to Step 2 once your data is ready |

### Data requirements

Your CSV should include at minimum:
- A **date column** with consistent time intervals (daily, weekly, or monthly)
- At least one **media activity variable** (impressions, clicks, GRPs)
- At least one **cost/spend variable** linked to a media variable
- A **KPI/target variable** (revenue, conversions, sales)

Optional columns include control variables (holidays, promotions, weather), a multiplier variable, and a hierarchy/brand column for panel data models.

---

## Step 2: Model Setup

Choose between two model types:

| Model Type | Description |
|------------|-------------|
| **Marketing Mix Model** | Bayesian MMM for media attribution, optimization, and scenario planning. Proceeds to Variable Selection. |
| **Vector Autoregression** | Bayesian VAR with Minnesota prior shrinkage for cross-channel dynamics, impulse response functions, and forecast error variance decomposition. Builds directly from this step. |

For MMM, click **Next** to proceed to Variable Selection. For VAR, configure endogenous/exogenous variables, lag settings, and build directly from this step.

---

## Step 3: Variable Selection

This is the core step where you assign each column in your dataset to a specific role. The screen is divided into three panels:

### Panel layout

| Panel | Description |
|-------|-------------|
| **Available Variables** (left) | Lists all unassigned column headers from your CSV. Select one or more variables by clicking their checkboxes. |
| **Assignment Buttons** (center) | Category buttons that assign selected variables to a role: Control, Media, Cost, Date, Multiplier, Model KPI, Hierarchy, or Reset All. |
| **Selected Variables** (right) | Shows variables organized into their assigned categories with color-coded panels. |

### Variable roles

| Role | Color | Required | Description |
|------|-------|----------|-------------|
| **Date Variable** | Purple | Yes | The time column. One variable only. Simba auto-detects periodicity (daily/weekly/monthly). |
| **Model KPI** | Indigo | Yes | The target variable the model predicts (e.g., revenue, sales, conversions). One variable only. |
| **Media Variables** | Green | Yes | Channel activity metrics (impressions, clicks, GRPs). These receive [adstock](../core-concepts/adstock-effects.md) and [saturation](../core-concepts/saturation-curves.md) transforms. |
| **Cost Variables** | Amber | Yes | Channel spend data. Must be linked 1:1 with media variables. |
| **Control Variables** | Blue | No | External factors (holidays, promotions, weather, competitor activity). Receive DM (Divide by Mean) transform by default. |
| **Multiplier** | Pink | No | A scaling factor applied to the model. |
| **Hierarchy** | Teal | No | A brand/segment/region column for panel data. When set, Simba builds one model per unique value. |

### Linking cost and media variables

After assigning cost and media variables, you must link them in pairs. Each cost variable maps to exactly one media variable (e.g., `tv_spend` links to `tv_impressions`). The **Linked Items** panel below the selection grid shows all active links.

Simba includes a **semantic matcher** that automatically detects channel types across 13 categories (TV, Digital, Social, Search, Video, Radio, Print, OOH, Email, Influencer, Affiliate, Direct, Mobile) and 8 metric types (Cost, Impressions, GRP, Clicks, Engagement, Conversions, Frequency, Duration). When you assign cost and media variables, the system suggests links based on matching channel and metric types.

### Smart Variable Categorization

When you upload data, Simba analyzes column names using keyword matching and pattern detection to suggest which category each variable belongs to. Suggestions appear below the selection grid with confidence scores. You can accept all suggestions at once or apply them individually.

### Halo and Trademark channels

Below the linked items, two additional sections allow you to designate:

- **[Halo Channels](../core-concepts/halo-effects.md)**: Brand awareness channels (e.g., TV, OOH) whose effects spill over to other brands in a portfolio. These receive a fixed small coefficient (0.005) rather than a data-driven prior.
- **Trademark/Portfolio Channels**: Masterbrand or corporate-level campaigns. These receive 25% of the calculated coefficient to account for shared attribution.

### Data validation

When you click **Next**, Simba runs automatic validation on your selected variables. If issues are found (e.g., missing values, misaligned dates), error messages appear at the top of the page and must be resolved before proceeding.

---

## Step 4: Prior Builder

The Prior Builder configures the [prior distributions](../core-concepts/priors-and-distributions.md) that encode your beliefs about each channel's effect before the model sees data. Two modes are available:

### Standard mode (recommended)

In Standard mode, the AI generates optimal priors automatically. Four toggleable features control the standard configuration:

| Feature | Default | Description |
|---------|---------|-------------|
| **Enable Baseline** | On | Adds a dynamic baseline (smooth local linear trend using HSGP Matern52) to capture underlying trends |
| **Enable Seasonality** | On | Adds [Fourier-based seasonality](../core-concepts/seasonality.md) to capture recurring patterns |
| **AI Media Priors** | On | Calculates per-channel coefficients using industry benchmarks, cost shares, and saturation adjustment |
| **Time-Varying Parameters** | Off | Allows media coefficients to evolve over time (TVP distribution) |

The AI Media Priors calculation pipeline works as follows:

1. **Cost share analysis** -- Each channel is weighted by its percentage of total spend
2. **Industry benchmark** -- Total media effect is estimated using benchmarks (e.g., E-Commerce: 21.9%, FMCG: 6.0%, Retail: 8.9%, Financial Services: 18.9%, TelCo: 30%)
3. **Saturation adjustment** -- Coefficients are adjusted for the tanh saturation curve using `impact / tanh(avg / (max * alpha))` where alpha mean is fixed at 1.7
4. **Output** -- Each channel receives an InverseGamma prior with calculated mean (mu) and sigma

### Custom mode (advanced)

Custom mode provides an interactive AG Grid table with direct cell editing. Single-click any cell to modify its value.

#### Media variable columns

| Column | Background | Description |
|--------|-----------|-------------|
| **Variable** | White | Channel name. Halo channels show a sparkle icon; trademark channels show an award icon. |
| **Distribution** | Blue tint | Prior distribution: `inversegamma`, `normal`, `truncatednormal`, or `tvp` |
| **Mean (mu)** | White | Expected coefficient value |
| **Sigma** | White | Uncertainty (standard deviation). Default: 1.0 |
| **Transform** | Purple tint | Data transformation: `N` (None, for media), `DM` (Divide by Mean, for controls), `STA` (Standardize), `DDM` |
| **Saturation** | Yellow tint | Activity level where the channel reaches 50% of maximum effect. Auto-populated with average non-zero activity. |
| **alpha_sd** | Blue tint | Shape uncertainty of the saturation curve. Lower values = steeper diminishing returns. Alpha mean is fixed at 1.7; only alpha_sd is editable. |
| **Period** | Blue tint | Number of time periods the media effect persists (default: 6 for weekly, 45 for daily) |
| **Decay L** | Blue tint | Minimum [adstock](../core-concepts/adstock-effects.md) decay rate (0.01-0.99) |
| **Decay U** | Blue tint | Maximum adstock decay rate (0.01-0.99) |
| **Adstock** | Green tint | Adstock type: `geometric` (instant peak, exponential decay) or `delayed` (peak at theta lag, then decay) |
| **Theta Mean** | Green tint | For delayed adstock: expected peak delay in periods (Gamma prior mean) |
| **Theta SD** | Green tint | For delayed adstock: uncertainty in peak delay (Gamma prior std dev) |
| **Lower / Upper** | Yellow tint | Bounds for Truncated Normal and TVP distributions. Media channels enforce Lower >= 0. |

#### Control variable columns

Control variables share the same Distribution, Mean, Sigma, Transform, Lower, and Upper columns but do not have saturation, decay, or adstock columns. Lower bounds can be negative for controls.

#### Bulk operations

Each row has action buttons:
- **Copy** -- Opens a bulk update dialog to copy settings from one variable to others
- **Chart** -- Opens a graph preview showing the prior distribution shape and decay curve

---

## Step 5: Model Details

The final step configures model-level settings and triggers the build.

### Model Configuration panel

| Setting | Description |
|---------|-------------|
| **Model Name** | Optional custom name. If blank, an auto-generated name is used (e.g., `MMM_a1b2c3d4`). When a hierarchy column is set, a **Batch Name** is required instead, and models are named `{BatchName}_{BrandValue}_001`. |
| **Transformation Method** | Fixed to **DM (Divide by Mean)** -- the dependent variable is scaled by its mean value. |
| **Likelihood Function** | `Normal` (default), `LogNormal` (strictly positive data), `StudentT` (robust to outliers), or `Quantile` (quantile regression). |

### Train/Test Split

A slider controls the percentage of data used for training (50%-100%, default: 100%). The visualization shows the date ranges for training and test periods.

### Advanced Options (collapsible)

The Advanced Options accordion expands to reveal four sections:

#### Seasonality settings

| Setting | Default | Description |
|---------|---------|-------------|
| **Prior Scale** | 10 | Controls flexibility of the [seasonality](../core-concepts/seasonality.md) component |
| **Fourier Terms (Annual)** | 2 | Number of Fourier terms for yearly seasonality (range: 1-25) |
| **Weekly Seasonality** | Off | Only available for daily data. Captures day-of-week effects. |
| **Weekly Fourier Terms** | 3 | Number of Fourier terms for weekly patterns (range: 1-7). Only shown when weekly seasonality is enabled. |

#### Intercept Priors

| Setting | Default | Description |
|---------|---------|-------------|
| **Prior Mean** | 1 | Expected baseline level as a multiple of KPI mean |
| **Lower Bound** | 0 | Minimum allowed intercept value |
| **Upper Bound** | 2 | Maximum allowed intercept value |

#### MCMC Sampling

| Setting | Default | Description |
|---------|---------|-------------|
| **Sampler Backend** | NUMBA | `NUMBA` (recommended, with progress tracking) or `Nutpie` (faster, no progress updates) |
| **Target Accept Rate** | 0.85 | NUTS sampler acceptance probability (0.6-0.99). Higher values reduce divergences but slow sampling. |
| **Warmup Iterations** | 1500 | Tuning samples for step-size and mass matrix adaptation (discarded after tuning) |
| **Posterior Samples** | 1000 | Number of posterior draws per chain |
| **Quantile** | 0.5 | Only shown when Quantile likelihood is selected |

#### Diagnostics

| Setting | Default | Description |
|---------|---------|-------------|
| **Sample from Prior** | Off | Generates prior predictive samples before fitting. Useful for validating prior assumptions. |

### Model Features (right column, Custom mode only)

When in Custom build mode, a right column shows toggleable model features:

| Feature | Default | Description |
|---------|---------|-------------|
| **Include Dynamic Baseline** | On | Adds smooth local linear trend (HSGP Matern52) |
| **Include Automatic Seasonality** | On | Adds Fourier-based seasonal components |
| **Time-Varying Media Variables** | Off | Allows channel effects to change over time |
| **Include Special Events** | Off | Enables holiday/event selection with country-specific calendars and manual date entry |

When **Include Special Events** is enabled, the panel expands to show:
- Auto-detected data periodicity (daily/weekly)
- Week convention selector (commencing vs. ending, for weekly data only)
- Holiday country selector
- Manual date picker for custom event dates

### Lift Test Calibration (collapsible)

Enable the **Include Lift Test Calibration** checkbox to add experimental results. Lift tests are integrated as **likelihood observations** (not priors) that constrain the model's saturation parameters with direct evidence of diminishing returns.

Each lift test entry requires:
- **Channel**: Which media variable the test applies to
- **x**: Baseline spend level during the test
- **delta_x**: Change in spend (the test increment)
- **delta_y**: Observed change in response
- **sigma**: Uncertainty in the observed effect (auto or manual)

Cost modes available: Direct spend, CPA, CPC, CPM, or Custom metric.

### Footer actions

| Button | Description |
|--------|-------------|
| **Download Config** | Exports the complete model configuration as JSON |
| **Upload Config** | Imports a previously saved configuration file |
| **Import from Saved Model** | Loads posteriors and settings from a completed model (switches to Custom mode if priors are imported) |
| **Build Model** | Submits the configuration and starts the Bayesian fitting process |

---

## Semantic Channel Matching

Simba's semantic matcher recognizes 13 channel categories and 8 metric types from variable names:

**Channel categories**: TV, Digital, Social, Search, Video, Radio, Print, OOH, Email, Influencer, Affiliate, Direct, Mobile

**Metric types**: Cost, Impressions, GRP, Clicks, Engagement, Conversions, Frequency, Duration

The matcher parses variable names by splitting on underscores, hyphens, dots, and spaces, then identifies channel type, metric type, and brand/segment tokens. This powers:
- Automatic cost-to-media linking suggestions
- Smart variable categorization
- Semantic decay defaults (e.g., TV gets higher decay ranges than search)
- Halo and trademark channel detection

---

## Next Steps

### Platform guides

- [Smart Defaults](./smart-defaults.md) -- How AI Media Priors are calculated
- [Budget Optimization](./budget-optimization.md) -- Optimize spend allocation using your fitted model
- [Scenario Planning](./scenario-planning.md) -- Explore what-if scenarios
- [Measurement](./measurement.md) -- Understanding model results and diagnostics
- [Halo & Trademark Channels](./halo-trademark-channels.md) -- Cross-brand effects in portfolio models
- [VAR Models](./var-models.md) -- Vector Autoregression configuration and results
- [Long-Term Effects](./long-term-effects.md) -- Brand effects beyond standard adstock

### Core concepts

- [Bayesian Modeling](../core-concepts/bayesian-modeling.md) -- How Bayesian inference powers the MMM
- [Priors and Distributions](../core-concepts/priors-and-distributions.md) -- Understanding prior distributions
- [Saturation Curves](../core-concepts/saturation-curves.md) -- Diminishing returns modeling
- [Adstock Effects](../core-concepts/adstock-effects.md) -- Geometric and delayed carryover
- [Seasonality](../core-concepts/seasonality.md) -- Fourier-based seasonal modeling
- [Halo Effects](../core-concepts/halo-effects.md) -- Cross-brand spillover effects
