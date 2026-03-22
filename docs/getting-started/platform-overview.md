# Platform Overview — Navigating the Simba Interface

This guide walks you through the Simba interface so you know exactly where to find every feature. Simba is organized around a clear four-step workflow — Audit, Measure, Predict, Optimize — and the interface is designed to guide you through that flow while giving you the flexibility to jump between stages as needed.

---

## The Four-Step Workflow

The Simba workflow is the backbone of the interface. It appears as a navigation bar or stepper at the top of your screen, showing where you are in the modeling process.

### Step 1: Audit (AI Data Auditor)

**Purpose:** Validate your data before modeling.

When you upload a dataset, the AI Data Auditor automatically analyzes it and presents a comprehensive audit report. This screen shows:

- **Data health score** — An overall assessment of your dataset's readiness for modeling.
- **Issue breakdown** — Individual checks grouped by severity (critical, warning, informational). Each issue includes an explanation of why it matters and what to do about it.
- **Column summary** — Statistics for each column including data type, range, missing value count, and distribution preview.
- **Correlation matrix** — A visual display of relationships between your media channels, used to flag multicollinearity risks.

You can address issues by editing your data externally and re-uploading, or in some cases by using Simba's built-in data preparation tools.

**Key action:** Review the audit report and resolve any critical issues before proceeding to modeling.

Read more: [AI Data Auditor](../workflow/ai-data-auditor.md)

---

### Step 2: Measure (Incremental Measurement)

**Purpose:** Build and run your Bayesian marketing mix model.

The Measure step is where the core modeling happens. It has several sub-screens:

#### Model Configuration

This is where you set up how Simba should model your data. The configuration interface is divided into panels:

- **Channel Configuration** — For each media channel, configure:
  - **Prior distributions** for the channel coefficient (effect size). Use the visual distribution editor to set mean and spread, or accept the smart default.
  - **Adstock parameters** — Choose geometric or Weibull decay, and set the decay rate and maximum lag. Visual previews show how the decay curve looks with your settings.
  - **Saturation parameters** — Choose logistic or Hill function and configure the half-saturation point and slope. A live preview shows the saturation curve.

- **Control Variables** — Select which non-media columns to include as controls (e.g., price, promotions, holidays). Controls help the model separate marketing effects from other business drivers.

- **Target KPI** — Confirm which column is the target variable and whether to model it on a raw or log scale.

- **Smart Defaults Panel** — A summary showing what Simba auto-generated for each setting, with the option to accept all defaults with a single click or customize individually.

Read more: [Setting Priors](../model-configuration/setting-priors.md) | [Adstock Settings](../model-configuration/adstock-settings.md) | [Saturation Curves](../model-configuration/saturation-curves.md) | [Smart Defaults](../model-configuration/smart-defaults.md)

#### Model Execution

Once configured, click **Run Model** to start the Bayesian inference. The execution screen shows:

- **Progress indicator** — Real-time status of the MCMC sampling process.
- **Estimated time remaining** — Based on your dataset size and model complexity.
- **Run log** — Technical details for advanced users who want to monitor convergence.

You can navigate away during execution and return when it completes. Simba will notify you.

#### Results Dashboard

When the model finishes, you arrive at the results dashboard. This is the most information-rich screen in Simba:

- **Channel Contribution Chart** — A stacked area or waterfall chart showing how much each channel contributed to the KPI over the modeled period. Each channel includes credible intervals.
- **ROAS Summary** — A table and bar chart showing the return on ad spend for each channel, with posterior medians and credible intervals.
- **Adstock Curves** — Per-channel visualizations of the estimated carryover effect.
- **Saturation Response Curves** — Per-channel visualizations showing how the KPI responds to increasing spend, highlighting where diminishing returns begin.
- **Model Fit** — Actual versus predicted KPI values over time, so you can visually assess how well the model captures your data.
- **Posterior Distributions** — For advanced users, the full posterior distribution plots for every model parameter.
- **Diagnostics Tab** — Convergence diagnostics (R-hat, effective sample size), posterior predictive checks, and model comparison metrics.

Read more: [Interpreting Results](../results/interpreting-results.md) | [Model Diagnostics](../results/model-diagnostics.md)

---

### Step 3: Predict (Scenario Planning)

**Purpose:** Simulate budget changes and forecast outcomes.

The Scenario Planning screen lets you create and compare hypothetical budget allocations:

- **Budget Sliders** — Adjust each channel's spend up or down using sliders or direct numeric input. Changes are expressed as absolute values or percentage shifts from the current allocation.
- **Simulation Output** — As you adjust budgets, Simba recalculates the predicted KPI using your fitted model. Results include the median prediction and credible intervals.
- **Scenario Comparison** — Save multiple scenarios and view them side by side in a comparison table or chart. This is useful for presenting options to stakeholders.
- **Scenario Library** — Previously saved scenarios are stored here for reference and re-use.

Read more: [Scenario Planning](../workflow/scenario-planning.md)

---

### Step 4: Optimize (Budget Intelligence)

**Purpose:** Automatically find the best budget allocation.

Budget Intelligence is the final workflow step, moving from manual "what if" analysis to algorithmic optimization:

- **Objective Selector** — Choose what you want to maximize (e.g., revenue, conversions) or set a target KPI value.
- **Budget Constraint** — Enter your total available budget.
- **Channel Constraints** — Optionally set minimum and maximum spend per channel. For example, you might require at least a baseline level of brand advertising or cap spend on an experimental channel.
- **Optimization Results** — After clicking **Optimize**, Simba displays:
  - The recommended allocation per channel
  - The expected KPI outcome with credible intervals
  - A comparison against your current allocation showing the estimated improvement
  - A visual breakdown of where budget shifted and why

Read more: [Budget Optimization](../workflow/budget-optimization.md)

---

## The Dashboard

The **Dashboard** is your landing page when you log in. It provides a high-level overview of your workspace:

- **Recent Models** — A list of your most recent model runs, showing status (running, completed, failed), date, and a link to jump directly to results.
- **Quick Actions** — Shortcuts to common tasks: upload new data, create a new model, open a recent scenario.
- **Workspace Summary** — Key metrics like the number of models run, datasets uploaded, and most recent optimization.
- **Notifications** — Alerts about completed model runs, audit warnings, or system updates.

---

## Model Management

Over time, you will build multiple models — different time periods, different channel sets, different prior configurations. The **Model Management** screen helps you organize and compare them:

- **Model List** — All models in your workspace, sortable by date, name, status, or KPI.
- **Model Comparison** — Select two or more completed models and compare their results side by side. This is valuable for understanding how different configurations or data updates affect conclusions.
- **Model Versioning** — Each run is saved with its full configuration, so you can always return to a previous version or understand what changed between runs.
- **Clone Model** — Duplicate a model configuration as a starting point for a new run with adjusted settings.
- **Archive and Delete** — Archive old models to keep your workspace clean, or delete models you no longer need.

---

## Data Management

The **Data** section is where you manage all datasets in your workspace:

- **Dataset Library** — All uploaded datasets with metadata (upload date, row count, column count, date range).
- **Upload New Data** — The data upload interface with drag-and-drop support and column mapping.
- **Data Preview** — View any dataset with summary statistics, distributions, and time-series plots.
- **Data Audit History** — Review past audit reports for any dataset.

---

## Settings

The **Settings** area, accessible from the main navigation menu or the gear icon, contains:

### Workspace Settings
- Workspace name and description
- Default currency and date format
- Default KPI selection

### Team Management (Scale, Enterprise, Managed)
- Invite and remove team members
- Assign and update roles
- View team activity

### Billing
- Current plan and usage
- Upgrade or downgrade plan
- Payment method management
- Invoice history

### Profile
- Update your name, email, and password
- Notification preferences
- API key management (Enterprise)

### Security
- Two-factor authentication setup
- Active session management
- SSO configuration (Enterprise)

For details on security infrastructure, see [Security and Compliance](../platform/security-and-compliance.md).

---

## Navigation Reference

Here is a summary of the main navigation structure:

| Menu Item | What It Contains |
|---|---|
| **Dashboard** | Overview, recent models, quick actions, notifications |
| **Audit** | AI Data Auditor reports and data validation |
| **Measure** | Model configuration, execution, and results |
| **Predict** | Scenario Planning and simulation |
| **Optimize** | Budget Intelligence and allocation recommendations |
| **Data** | Dataset library, upload, and preview |
| **Models** | Model list, comparison, versioning, and management |
| **Settings** | Workspace, team, billing, profile, and security |

The workflow steps (Audit, Measure, Predict, Optimize) also appear as a linear stepper within each model context, making it easy to move forward through the process or jump back to an earlier stage.

---

## Keyboard Shortcuts and Tips

- Use the **workspace switcher** in the top-left corner to move between workspaces (Scale and above).
- The **notification bell** in the top-right corner shows model completion alerts and system messages.
- Most charts support **hover for details** — hover over any data point to see exact values and credible intervals.
- **Export buttons** are available on all charts and tables for downloading results as CSV, PNG, or PDF.

---

## Next Steps

Now that you know your way around the interface:

- Follow the [Quick Start Guide](quick-start-guide.md) to build your first model using this interface.
- Read about [Data Requirements](../data-preparation/data-requirements.md) to prepare your dataset.
- Explore [Setting Priors](../model-configuration/setting-priors.md) to understand the model configuration options in detail.

For questions about navigating the platform, contact **support@simba-mmm.com**.

---

## Related Documentation

- [What is Simba?](what-is-simba.md) — Product overview and positioning
- [Quick Start Guide](quick-start-guide.md) — Step-by-step first model walkthrough
- [Account Setup](account-setup.md) — Plans, workspaces, and team management
- [AI Data Auditor](../workflow/ai-data-auditor.md) — Deep dive on the audit step
- [Incremental Measurement](../workflow/incremental-measurement.md) — The modeling methodology
- [Scenario Planning](../workflow/scenario-planning.md) — Simulation and forecasting
- [Budget Optimization](../workflow/budget-optimization.md) — Algorithmic budget allocation
