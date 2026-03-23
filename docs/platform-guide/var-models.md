# VAR Models --- Building and Interpreting VAR Models in Simba

This guide walks you through creating, fitting, and interpreting Vector AutoRegression (VAR) models in Simba. For the conceptual background on what VAR is and when to use it, see [VAR Modeling](../core-concepts/var-modeling.md).

---

## Creating a VAR Model

### Step 1: Start in the Warehouse

From the Warehouse configuration tab, begin the standard model creation wizard. VAR model type selection happens in Step 4 (Model Setup).

### Step 2: Variable Selection

Select the variables you want to include in the VAR system. Unlike standard MMM where you choose a single target and multiple inputs, **all selected variables become endogenous** in a VAR --- each variable predicts and is predicted by all other variables.

Choose variables that you believe form an interconnected system. A typical VAR might include revenue, TV spend, search volume, social media impressions, and website traffic.

### Step 3: Prior Configuration

Use the same prior builder interface as standard models to configure priors for each variable. The priors govern the expected relationships between variables.

### Step 4: Select VAR Model Type

In the Model Setup step, select **VAR** as the model type. Configure additional VAR-specific settings such as the number of lags (how many past periods each variable uses to predict the current period).

### Step 5: Prior Predictive Check (Recommended)

Before committing to a full model fit, run a **prior predictive check**:

1. Click **Run Prior Check** from the model setup screen.
2. The check generates sample forecasts from your prior distributions.
3. Poll for results --- the check runs asynchronously and may take a few minutes.
4. Review the generated forecasts. If they show unreasonable ranges (revenue going negative, explosive growth), adjust your priors.
5. Repeat until the prior predictive forecasts look sensible.

This step is optional but strongly recommended. It catches misconfigured priors before you invest time in a full model fit.

### Step 6: Fit the Model

Click **Run Model** to start Bayesian VAR inference. The model is queued and progresses through the same status lifecycle as standard models (Pending → Under Way → Complete/Failed).

---

## Interpreting VAR Results

Once the model completes, the results page includes VAR-specific analyses:

### Long-Run Effects

The long-run effects table shows the cumulative impact of a sustained unit change in each variable on every other variable. This is presented as a matrix:

| Shock to → | Revenue | TV | Search | Social |
|---|---|---|---|---|
| Revenue | --- | +$X | +$Y | +$Z |
| TV | +A | --- | +B | +C |
| Search | +D | +E | --- | +F |
| Social | +G | +H | +I | --- |

Each cell shows the long-run cumulative effect. Large positive values indicate strong positive relationships; values near zero indicate weak or no long-run connection.

### FEVD (Forecast Error Variance Decomposition)

FEVD shows how much of the forecast uncertainty in each variable is explained by shocks to other variables:

- A channel that explains a large share of revenue FEVD is systemically important.
- If revenue FEVD is dominated by its own shocks, the system is relatively independent.
- If TV explains 30% of revenue FEVD, TV fluctuations are a major driver of revenue uncertainty.

### Transformation Metadata

Details about how variables were transformed for the VAR estimation, including any differencing, scaling, or normalization applied.

---

## Linking VAR to Standard Models

VAR models can be linked to standard MMM models for comparison:

- Build a standard MMM model and a VAR model using the same data.
- Link them from the model management interface.
- Compare channel importance rankings between the two approaches.
- Use standard MMM for attribution and optimization; use VAR for understanding system dynamics.

---

## Availability

VAR modeling is included in the free trial and in Enterprise and Managed plans. For details, see [Pricing](../pricing/README.md).

---

## Next Steps

- [VAR Modeling Concepts](../core-concepts/var-modeling.md) --- Understand the theory behind VAR
- [Model Creation Wizard](./model-creation-wizard.md) --- Full walkthrough of the model setup process
- [Incremental Measurement](./measurement.md) --- Standard MMM results interpretation
