# VAR Modeling --- Bayesian Vector AutoRegression for Marketing

Vector AutoRegression (VAR) is a multi-equation time series model that captures dynamic interactions between marketing channels. While standard MMM models a single target variable (revenue) as a function of marketing inputs, VAR models the entire system --- every variable predicts and is predicted by every other variable over time.

Simba implements a **Bayesian VAR** using PyMC, with Minnesota prior shrinkage, configurable priors, and full posterior inference.

---

## What Is VAR?

In a standard MMM, the model estimates one equation:

> Revenue = f(TV, Search, Social, Controls, ...)

VAR replaces this with a system of simultaneous equations where each variable is modeled as a function of its own lagged values and the lagged values of all other variables:

> Revenue(t) = f(Revenue(t-1), TV(t-1), Search(t-1), Social(t-1), ...)
> TV(t) = f(Revenue(t-1), TV(t-1), Search(t-1), Social(t-1), ...)
> Search(t) = f(Revenue(t-1), TV(t-1), Search(t-1), Social(t-1), ...)
> Social(t) = f(Revenue(t-1), TV(t-1), Search(t-1), Social(t-1), ...)

This captures **feedback loops and inter-channel dynamics** that a single-equation model cannot.

![Standard MMM vs Bayesian VAR](./images/var-mmm-comparison.png)
*Left: standard MMM uses one-way arrows from channels to revenue. Right: Bayesian VAR models bidirectional relationships --- every variable predicts every other, capturing cross-channel dynamics and feedback loops.*

---

## When to Use VAR

VAR is most valuable when:

- **Channels influence each other.** TV campaigns drive branded search volume. Social media engagement boosts organic traffic. If your marketing ecosystem has these cross-channel dynamics, VAR captures them explicitly.
- **You want to understand the system.** VAR answers questions like "If I shock TV spend, what happens to search volume three weeks later?" --- questions that standard MMM cannot address.
- **You suspect feedback effects.** Revenue growth may lead to increased marketing budgets, which in turn drives more revenue. VAR models these bidirectional relationships.

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

- **Y(t)** is the k-dimensional vector of endogenous variables (log-transformed via log1p).
- **alpha** is the intercept vector.
- **A1, ..., Ap** are lag coefficient matrices (p = number of lags, user-configured).
- **X(t)** is the vector of exogenous variables (media spend, optional).
- **beta** is the exogenous coefficient matrix.
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
2. **Long-run multipliers:** Once linked, the VAR's long-run elasticities become channel-specific multipliers applied to MMM coefficients. For example, if the VAR estimates a TV long-run elasticity of 0.03, this translates to a 3x long-term multiplier on the MMM's short-term TV ROI.
3. **Toggle view:** The portfolio analysis includes a toggle to switch between short-term (MMM only) and long-term (MMM + VAR multipliers) views.

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
