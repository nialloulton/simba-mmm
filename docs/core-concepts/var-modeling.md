# VAR Modeling --- Bayesian Vector AutoRegression for Marketing

Vector AutoRegression (VAR) is a multi-equation time series model that captures dynamic interactions between business outcomes and brand metrics. While standard MMM models a single target variable (revenue) as a function of marketing inputs, VAR models a system of interacting variables --- revenue, brand awareness, brand search, and other brand equity metrics --- while treating media spend as exogenous inputs.

Simba implements a **Bayesian VAR** using PyMC, with Minnesota prior shrinkage, configurable priors, and full posterior inference.

---

## What Is VAR?

In a standard MMM, the model estimates one equation:

> Revenue = f(TV, Search, Social, Controls, ...)

VAR models a system of **endogenous variables** (business outcomes and brand metrics that influence each other) driven by **exogenous inputs** (media spend that you control):

> Revenue(t) = f(Revenue(t-1), Awareness(t-1), BrandSearch(t-1), ...) + g(TV_spend, Social_spend, ...)
> Awareness(t) = f(Revenue(t-1), Awareness(t-1), BrandSearch(t-1), ...) + g(TV_spend, Social_spend, ...)
> BrandSearch(t) = f(Revenue(t-1), Awareness(t-1), BrandSearch(t-1), ...) + g(TV_spend, Social_spend, ...)

The endogenous variables interact through **feedback loops** (e.g., brand awareness drives brand search, which drives revenue, which funds more media). Media spend enters as exogenous inputs --- it affects the system but is not predicted by it.

![VAR structure: exogenous inputs and endogenous system](./images/var-exog-endog-structure.png)
*Media spend (TV, social, display, YouTube) enters as exogenous one-way inputs. Revenue, brand awareness, and brand search form the endogenous system with feedback loops between them.*

![Standard MMM vs Bayesian VAR](./images/var-mmm-comparison.png)
*Left: standard MMM uses one-way arrows from channels to revenue. Right: Bayesian VAR models the interacting system of business outcomes and brand metrics.*

---

## When to Use VAR

VAR is most valuable when:

- **You have brand equity metrics.** Brand awareness surveys, brand search volume, consideration scores, or NPS data alongside revenue. VAR captures how these metrics interact and how media drives them.
- **You want to understand the system.** VAR answers questions like "If I increase TV spend, what happens to brand awareness, then brand search, then revenue over the next 12 weeks?" --- questions that standard MMM cannot address.
- **You want long-term effects.** Standard MMM captures direct short-term media effects. VAR captures the full chain: media → brand awareness → brand search → revenue, revealing the total long-term multiplier on each channel.

Standard MMM is better when:

- You need direct channel attribution and budget optimization (the primary Simba workflow).
- Your goal is measuring incrementality and allocating budget efficiently.
- You have limited data and want simpler, more robust estimates.

**VAR and standard MMM are complementary.** Use standard MMM for channel attribution and optimization. Use VAR for understanding inter-channel dynamics and long-term system effects. Simba supports linking VAR models to MMM models so that VAR long-run multipliers can enhance MMM ROI estimates (see [Linking VAR to MMM](#linking-var-to-mmm) below).

---

## The Bayesian VAR Model

Simba's VAR is a fully Bayesian model fitted with PyMC using NUTS (No U-Turn Sampler). The model equation is:

> **Y(t) = alpha + A1 Y(t-1) + ... + Ap Y(t-p) + X(t) beta + epsilon(t)**

Where:

- **Y(t)** is the k-dimensional vector of endogenous variables --- revenue, brand awareness, brand search, and other brand equity metrics (log-transformed via log1p).
- **alpha** is the intercept vector.
- **A1, ..., Ap** are lag coefficient matrices capturing how endogenous variables predict each other (p = number of lags, user-configured).
- **X(t)** is the vector of exogenous variables --- typically media spend by channel (TV, social, display, etc.). These enter the model as controlled inputs that drive the system but are not predicted by it. Note: brand search can be treated as either endogenous (if it interacts with awareness/revenue) or exogenous depending on your modeling goals.
- **beta** is the exogenous coefficient matrix (media effects on each endogenous variable).
- **epsilon(t)** is multivariate Gaussian noise with covariance Sigma.

### Priors

The Bayesian VAR uses informative priors to regularize estimation:

- **Lag coefficients:** Normal priors with optional **Minnesota prior shrinkage** --- a structured approach where own-lag coefficients are centered near 0.9 (persistence), cross-variable coefficients are shrunk toward zero, and higher lags are shrunk more aggressively. Shrinkage parameters: lambda_overall=0.2, lambda_cross=0.1.
- **Intercepts:** Normal(0, 0.5) or TruncatedNormal with bounds.
- **Exogenous coefficients:** Normal(0, 0.5) with optional sign constraints (e.g., media effects constrained to be positive).
- **Noise covariance:** LKJ Cholesky decomposition (eta=2.0) for multivariate case, or independent HalfNormal per equation for diagonal case.

### Data Transformations

All endogenous variables are automatically transformed via **log1p** (robust to zeros). Exogenous variables default to log1p but support configurable transforms: asinh, log, log_shift, per_k, z-score, min-max, and index100. Results are converted back to percent-per-percent elasticities for interpretability.

### Sampling Configuration

Default sampling parameters:
- **Draws:** 2,000 posterior samples
- **Tune:** 1,000 burn-in samples
- **Chains:** 2 (configurable up to 4)
- **Target accept:** 0.9
- Optional JAX/NumPyro backend for acceleration

---

## Key VAR Concepts

### Impulse Response Functions (IRFs)

An IRF traces how a one-unit shock to one variable propagates through the entire system over time. For example, an IRF for TV → Revenue shows the cumulative revenue impact of a one-unit increase in TV spend, accounting for all the indirect pathways (TV → search → revenue, TV → awareness → revenue, etc.).

![Impulse Response Functions](./images/var-irf-examples.png)
*Three IRF examples. Left: TV spend shock has a strong revenue effect peaking at lag 2-3, then decaying. Center: the same TV shock drives brand search volume with a delayed build. Right: social spend has a fast-decaying revenue effect. Shaded bands show posterior uncertainty.*

Simba computes IRFs with:
- Configurable shock magnitude and forecast horizon.
- Non-orthogonalized shocks by default (identity matrix); Cholesky orthogonalization available.
- Cumulative IRF option for accumulated effects.

### Forecast Error Variance Decomposition (FEVD)

FEVD decomposes the forecast uncertainty of each variable into the contributions of shocks from all variables in the system. In marketing terms, FEVD answers: "How much of the uncertainty in my revenue forecast is attributable to changes in TV, search, social, and other factors?"

![FEVD example](./images/var-fevd-example.png)
*At short horizons, revenue forecast variance is mostly driven by its own history. At longer horizons, media channels explain an increasing share --- revealing which channels are systemically important.*

A channel that explains a large share of revenue forecast variance is systemically important --- its fluctuations have outsized impact on business outcomes.

FEVD can be skipped in fast mode for 2-3x speedup when only IRFs and long-run effects are needed.

### Long-Run Effects

Long-run effects summarize the total cumulative impact after the system has fully absorbed a shock. Simba computes these analytically using the formula:

> **Psi_inf = (I - A_sum)^{-1}**

Where A_sum is the sum of all lag coefficient matrices. This is computationally efficient (one matrix inverse) and produces percent-per-percent elasticities --- for example, "a 1% sustained increase in TV spend produces a 3% long-run increase in revenue."

Long-run effects can also include NPV scenarios and ROI analysis when annual spend and revenue data is provided.

---

## Prior Predictive Checking

Before fitting a VAR model, Simba supports **prior predictive checks** --- a validation step that generates sample forecasts from your prior distributions (before seeing data) to confirm that the priors produce sensible ranges.

This feature is implemented via a dedicated `VarPriorChecker` service. When enabled, it samples only from the prior (skipping posterior inference), allowing you to validate prior plausibility before committing to a full model fit. If the prior predictive forecasts show unreasonable values (e.g., revenue going negative or exploding), you know to adjust your priors.

---

## Linking VAR to MMM

VAR and MMM models can be linked in Simba's portfolio view to combine the strengths of both approaches:

1. **Smart matching:** Simba ranks available VAR models by compatibility with your MMM model --- 100% match (same batch and brand), 80% (same brand), 50% (same batch), or no match.
2. **Long-run multipliers:** Once linked, the VAR's long-run elasticities become channel-specific multipliers applied to MMM coefficients. For example, if the VAR estimates a TV long-run elasticity of 0.03, this translates to a 2.5x long-term multiplier on the MMM's short-term TV ROI.
3. **Toggle view:** The portfolio analysis includes a toggle to switch between short-term (MMM only) and long-term (MMM + VAR multipliers) views.

![Short-term vs long-term ROI by channel](./images/var-longterm-vs-shortterm.png)
*Illustrative example: channels with strong brand-building effects (TV, YouTube) show the largest long-term multipliers when VAR effects are included. The purple labels show the multiplier each channel receives from VAR long-run elasticities.*

This is where VAR adds the most practical value: it reveals that channels which build brand equity (like TV and video) have much larger total effects than their short-term MMM ROI suggests, because they drive brand awareness and brand search which in turn drive revenue over many weeks.

---

## Lag Selection and Data Requirements

### Lag Selection

The number of lags (p) is **user-configured** in the model setup. There is no automatic lag order selection (AIC/BIC). Choose lags based on domain knowledge:

- **1--2 lags** for weekly data with fast-responding channels.
- **3--4 lags** for weekly data with channels that have longer carryover.
- **Higher lags** require proportionally more data.

### Minimum Data

The model requires at least **lags + 10 observations**. For example, a 4-lag model on weekly data needs at least 14 weeks. In practice, 52+ weeks is recommended for reliable estimates.

---

## Tier Availability

VAR modeling is available on the following tiers:

| Tier | VAR Available |
|---|---|
| Trial | Yes |
| Analyst | No |
| Pro | Yes |
| Scale | Yes |

---

## Next Steps

- [Marketing Mix Modeling](./marketing-mix-modeling.md) --- The standard MMM approach for channel attribution.
- [Bayesian Modeling](./bayesian-modeling.md) --- The statistical foundation shared by MMM and VAR.
- [Incrementality](./incrementality.md) --- Causal impact measurement.
