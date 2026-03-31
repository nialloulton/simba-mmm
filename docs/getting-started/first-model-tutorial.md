# Your First Model --- A Hands-On Tutorial

This tutorial walks you through building a complete Marketing Mix Model in Simba using sample data. By the end, you will have fitted a model, read the results, run a scenario, and generated an optimized budget recommendation.

**Time required:** About 2 hours (most of that is model fitting time — you can step away while it runs).

**What you'll need:** A Simba account ([create one here](./account-setup.md)) and the sample dataset below.

---

## Step 1: Download the Sample Data

Download the sample CSV file: [sample-marketing-data.csv](../../resources/sample-data/sample-marketing-data.csv)

This is a synthetic dataset with 104 weeks (2 years) of data for a fictional brand. It contains:

| Column | Description |
|--------|-------------|
| `date` | Weekly dates (Mondays) |
| `revenue` | Total weekly revenue ($) — this is the target KPI |
| `tv_spend` | Weekly TV advertising spend ($) |
| `facebook_spend` | Weekly Facebook/Meta spend ($) |
| `google_ads_spend` | Weekly Google Ads spend ($) |
| `email_spend` | Weekly email marketing spend ($) |
| `avg_price_index` | Average price index (control variable, ~1.0) |

The data is already in the format Simba expects: one row per week, a date column, a KPI column, media spend columns, and a control variable. For your own data, see [Data Requirements](../data/data-requirements.md).

---

## Step 2: Upload Your Data

1. Log in to Simba and navigate to the **Model Warehouse**.
2. Click **New Model** to start the [Model Creation Wizard](../platform-guide/model-creation-wizard.md).
3. Upload the sample CSV file.
4. Simba will detect the columns automatically. Confirm:
   - **Date column:** `date`
   - **Target KPI:** `revenue`
   - The 4 spend columns are classified as **media channels**
   - `avg_price_index` is classified as a **control variable**

If the semantic matcher doesn't auto-classify a column correctly, you can drag it to the right category. See [Smart Defaults](../platform-guide/smart-defaults.md) for how Simba identifies channels.

---

## Step 3: Run the Data Validator

After uploading, click **Run Data Validator**. The [Data Validator](../platform-guide/data-auditor.md) runs 10 automated checks on your data:

- **Schema validation** — correct column types, no blanks
- **Frequency diagnostics** — confirms weekly periodicity
- **Outlier detection** — flags unusual values
- **Multicollinearity** — checks if channels are too correlated to distinguish

With the sample data, you should see mostly green (pass) results. If you see warnings about outliers, that's expected — the Validator flags them for your review, but they don't block model fitting.

---

## Step 4: Configure the Model (Accept Smart Defaults)

For this tutorial, **accept the Smart Defaults** — Simba's automatic configuration:

- **[Priors](../core-concepts/priors-and-distributions.md):** Each media channel gets an InverseGamma prior on its coefficient, and Beta/Gamma priors on decay and saturation parameters. These are calibrated from your data's cost shares.
- **[Adstock](../core-concepts/adstock-effects.md):** Geometric decay with channel-appropriate initial values (shorter for digital, longer for TV).
- **[Saturation](../core-concepts/saturation-curves.md):** tanh function with alpha parameter (Gamma prior, mean 1.7).

You don't need to change anything for your first model. The defaults are designed to produce good results for most datasets. Once you're comfortable with the platform, you can customize every prior — see [Model Configuration](../platform-guide/model-configuration.md).

Click **Fit Model** to start the [Bayesian](../core-concepts/bayesian-modeling.md) estimation process.

**What to expect:** Model fitting takes 15–60 minutes depending on data size. You'll see a progress indicator. You can close the browser and come back — the model runs on Simba's servers.

---

## Step 5: Interpret Your Results

Once the model finishes, navigate to the **Active Model** tab. You'll see several key outputs:

### Channel Contributions

A stacked area chart showing how total revenue breaks down into:
- **Base demand** — revenue that would have happened without any marketing
- **Each channel's [incremental](../core-concepts/incrementality.md) contribution** — the revenue each channel caused

Look for: Which channel contributes the most? Is the base demand high (meaning marketing adds a small layer) or low (meaning marketing drives most of the revenue)?

### ROAS (Return on Ad Spend)

For each channel, Simba reports the posterior mean ROAS with a [94% HDI](../core-concepts/bayesian-modeling.md) (credible interval). For example:

> **TV ROAS:** 1.85 (94% HDI: 1.20 – 2.55)

This means: for every $1 spent on TV, the model estimates $1.85 in incremental revenue, and there's a 94% probability the true value falls between $1.20 and $2.55.

### Response Curves

Click the **Response Curves** tab to see [saturation curves](../core-concepts/saturation-curves.md) for each channel. These show how each channel's incremental return changes with spend level. Look for:
- **Steep curves** — the channel still has room to grow
- **Flat curves** — the channel is saturated; more spend won't help much

---

## Step 6: Run a Scenario

Navigate to the **Scenario Planner** tab. This lets you ask "what if?" questions about your budget:

1. Click **New Scenario**.
2. Try a simple change: increase `google_ads_spend` by 20% and decrease `tv_spend` by 20%.
3. Click **Run Scenario**.

Simba will show you the projected change in total revenue, with uncertainty bands. Compare the scenario to the current allocation to see whether the reallocation improves or hurts total performance.

See [Scenario Planning](../platform-guide/scenario-planning.md) for the full guide.

---

## Step 7: Run the Optimizer

Navigate to the **Optimization** tab. The [Budget Optimizer](../platform-guide/budget-optimization.md) finds the mathematically optimal allocation:

1. Set your **total budget** (use the current total from your data as a starting point).
2. Set **gamma** (risk aversion) to 1.0 for a balanced recommendation.
3. Set channel constraints if needed (e.g., "TV cannot go below $20,000/week").
4. Click **Optimize**.

The optimizer will recommend a reallocation that maximizes expected revenue given the [response curves](../core-concepts/saturation-curves.md) and your constraints. Compare the "Current" vs "Optimized" allocation to see where the model suggests moving budget.

---

## What You've Learned

In this tutorial, you:

1. Uploaded marketing data in the correct format
2. Validated data quality with the Data Validator
3. Fitted a Bayesian MMM with Smart Defaults
4. Read channel contributions, ROAS, and response curves
5. Ran a what-if scenario
6. Generated an optimized budget recommendation

---

## Next Steps

**Ready to use your own data?**
- [Data Requirements](../data/data-requirements.md) — what format your data needs to be in
- [Data Preparation](../data/data-preparation.md) — how to clean and format your data
- [Exporting Data from Ad Platforms](../data/exporting-from-platforms.md) — how to get data out of Google Ads, Meta, etc.

**Want to customize the model?**
- [Model Configuration](../platform-guide/model-configuration.md) — adjust priors, adstock, and saturation
- [Priors and Distributions](../core-concepts/priors-and-distributions.md) — understand what each prior does

**Something not working?**
- [Troubleshooting](../platform-guide/troubleshooting.md) — common issues and fixes
- [FAQ](../faq/README.md) — frequently asked questions
