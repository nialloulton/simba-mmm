# Quick Start Guide — Build Your First Marketing Mix Model

This guide walks you through the complete Simba workflow, from signing up to interpreting your first optimized budget recommendation. By the end, you will have a working Bayesian marketing mix model with actionable channel-level insights.

**Time required:** Most users complete their first model run within a few hours. The actual computation takes minutes; the majority of your time will be spent reviewing data and results.

**Prerequisites:** A dataset with time-series marketing data (weekly or daily), including spend by channel and a target KPI. See [Data Requirements](../data-preparation/data-requirements.md) for full details.

---

## Step 1: Create Your Account

1. Go to [getsimba.ai](https://getsimba.ai) and click **Start Free Trial**.
2. Register with your email or sign in with Google/SSO.
3. You will land in the **Sandbox** plan, which gives you a full 14-day free trial with access to core features.
4. No credit card is required to start.

For detailed information about plans, workspaces, and team setup, see [Account Setup](account-setup.md).

---

## Step 2: Prepare and Upload Your Data

### Prepare your data

Simba expects a time-series dataset in CSV format with:

- A **date column** (weekly or daily granularity)
- One or more **media spend or activity columns** (e.g., `tv_spend`, `paid_search_spend`, `social_impressions`)
- A **target KPI column** (e.g., `revenue`, `conversions`, `leads`)
- Optional: **control variables** (e.g., `price`, `promotions`, `seasonality_flag`, `competitor_activity`)

A clean dataset with 1 to 3 years of weekly data is ideal for most use cases. See [Data Preparation](../data-preparation/data-requirements.md) for a full guide on formatting, granularity, and common pitfalls.

### Upload your data

1. From the dashboard, click **New Model** or navigate to the data upload screen.
2. Drag and drop your CSV file or click to browse.
3. Simba will parse your file and display a preview of the detected columns.
4. Map your columns: select which column is the date, which are media channels, which is the target KPI, and which are control variables.

> **Tip:** Name your CSV columns clearly (e.g., `paid_search_spend` rather than `channel_3`). Simba uses column names in all charts and reports.

---

## Step 3: Run the AI Data Auditor

Before building a model, Simba's **AI Data Auditor** automatically reviews your dataset. This step is part of the **Audit** phase of the Simba workflow.

The auditor checks for:

- **Missing values** — gaps in your time series that could bias results
- **Outliers** — extreme values that may distort model estimation
- **Multicollinearity** — channels whose spend patterns are too correlated, making it difficult to disentangle their effects
- **Stationarity and trends** — structural changes in your data over time
- **Data quality issues** — formatting errors, zero-variance columns, or insufficient data length

You will receive a clear audit report with a health score and specific recommendations. Address any critical issues before proceeding. Many issues can be resolved directly in Simba's data preparation tools.

Read more: [AI Data Auditor](../workflow/ai-data-auditor.md)

---

## Step 4: Configure Your Model

This is the **Measure** phase. Simba needs to know how to model the relationship between your marketing channels and your KPI. There are three key configuration areas:

### Priors

Priors express what you believe about each channel's effect before seeing the data. For example, you might believe that TV has a positive but uncertain effect on revenue. Simba lets you set prior distributions through the UI — no code needed.

**Smart Defaults:** Simba auto-generates sensible priors from your historical data. For your first model, **we recommend starting with the smart defaults** and refining later. This gets you to results quickly while maintaining statistical validity.

Read more: [Setting Priors](../model-configuration/setting-priors.md) | [Smart Defaults](../model-configuration/smart-defaults.md)

### Adstock (Carryover Effects)

Marketing does not always have an immediate effect. A TV ad aired on Monday may drive searches and conversions throughout the week. Adstock parameters control how each channel's effect decays over time. Simba provides geometric and Weibull adstock options, configurable per channel via the UI.

Smart defaults will suggest appropriate adstock settings based on channel type and your data patterns.

Read more: [Adstock Settings](../model-configuration/adstock-settings.md)

### Saturation (Diminishing Returns)

At some point, spending more on a channel yields diminishing returns. Saturation curves model this effect. Simba uses logistic and Hill saturation functions, configurable per channel.

Smart defaults estimate saturation parameters from the observed spend ranges in your data.

Read more: [Saturation Curves](../model-configuration/saturation-curves.md)

### Running the model

Once you are satisfied with your configuration (or have accepted the smart defaults):

1. Review the model summary panel, which shows your selected priors, adstock, and saturation settings.
2. Click **Run Model**.
3. Simba will run the Bayesian inference using PyMC-Marketing. This typically takes a few minutes depending on dataset size and model complexity.
4. You will see a progress indicator and be notified when the run completes.

---

## Step 5: Interpret Your Results

When the model finishes, you will land on the **results dashboard**. Here is what to look at first:

### Channel Contributions

The channel contribution chart shows how much each marketing channel (and baseline/control factors) contributed to your KPI over the modeled period. Unlike deterministic tools, Simba shows you **credible intervals** — the range of plausible contribution values — not just a single number.

### Return on Ad Spend (ROAS)

Simba calculates the posterior ROAS for each channel, telling you how much KPI return you get for each unit of spend. Channels with wide credible intervals have more uncertainty — this is honest reporting, not a flaw.

### Adstock and Saturation Curves

Visualize how each channel's effect decays over time (adstock) and how it responds to increased spend (saturation). These curves are essential for understanding channel dynamics.

### Model Diagnostics

Check the model fit, convergence diagnostics, and posterior predictive checks. These tell you whether the model adequately captures your data patterns. Simba highlights any issues and provides plain-language explanations.

Read more: [Interpreting Results](../results/interpreting-results.md) | [Model Diagnostics](../results/model-diagnostics.md)

---

## Step 6: Plan Scenarios

With a fitted model, move to the **Predict** phase. Scenario Planning lets you simulate changes to your budget and see the predicted impact:

1. Navigate to **Scenario Planning** from the results screen.
2. Adjust channel budgets using the sliders or input fields. For example, increase paid social by 20% and decrease TV by 10%.
3. Click **Simulate** to see the predicted KPI outcome with uncertainty intervals.
4. Compare multiple scenarios side by side.

This is where Simba moves beyond measurement into decision support. You can test hypotheses before committing real budget.

Read more: [Scenario Planning](../workflow/scenario-planning.md)

---

## Step 7: Optimize Your Budget

The final step is the **Optimize** phase. Budget Intelligence automatically finds the best allocation:

1. Navigate to **Budget Intelligence** from the scenario planning screen or main navigation.
2. Set your **total budget constraint** (the total amount you have to allocate).
3. Optionally set **per-channel minimum and maximum spend** constraints (e.g., "TV must be at least 10% of total").
4. Choose your optimization objective (maximize revenue, conversions, etc.).
5. Click **Optimize**.
6. Simba returns the recommended allocation with the expected KPI lift compared to your current spend.

The optimization is grounded in the full posterior distribution of your Bayesian model, meaning it accounts for uncertainty in channel effects rather than optimizing against a single point estimate.

Read more: [Budget Optimization](../workflow/budget-optimization.md)

---

## What to Do Next

Congratulations — you have built, interpreted, and optimized your first Bayesian marketing mix model. Here are recommended next steps:

- **Refine your priors.** Now that you have seen the results, consider whether the smart defaults align with your domain knowledge. Adjust priors and re-run to see how results change. See [Setting Priors](../model-configuration/setting-priors.md).
- **Add control variables.** If you did not include price, promotions, or seasonality controls, adding them can improve model accuracy. See [Control Variables](../model-configuration/control-variables.md).
- **Explore model diagnostics.** Dive deeper into convergence, posterior predictive checks, and sensitivity analysis. See [Model Diagnostics](../results/model-diagnostics.md).
- **Set up regular updates.** As new data comes in, re-run your model to keep insights current. Simba preserves your configuration for easy re-runs.
- **Invite your team.** Share results and collaborate on scenarios. See [Account Setup](account-setup.md) for team management.

---

## Troubleshooting

| Issue | Solution |
|---|---|
| Data upload fails | Check that your file is a valid CSV with a header row. See [Data Requirements](../data-preparation/data-requirements.md). |
| Audit flags critical issues | Address the flagged issues in your data before running the model. The audit report includes specific guidance. |
| Model takes too long | Large datasets or complex configurations increase run time. Try reducing the number of channels or using weekly instead of daily data. |
| Poor model fit | Review diagnostics and consider adding control variables, adjusting priors, or checking data quality. See [Model Diagnostics](../results/model-diagnostics.md). |
| Results seem unreasonable | Check your priors and data. Unreasonable results often indicate data issues or overly vague priors. See [Setting Priors](../model-configuration/setting-priors.md). |

For additional help, contact **support@simba-mmm.com**.

---

## Related Documentation

- [What is Simba?](what-is-simba.md) — Understand the platform and methodology
- [Account Setup](account-setup.md) — Plans, workspaces, and team management
- [Platform Overview](platform-overview.md) — Navigate the full interface
- [Data Requirements](../data-preparation/data-requirements.md) — Detailed data preparation guide
- [Bayesian Modeling in Marketing](../core-concepts/bayesian-modeling.md) — The theory behind the engine
