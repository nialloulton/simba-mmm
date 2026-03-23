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

---

## Why Minnesota Priors Matter

A VAR with k endogenous variables and p lags has k x k x p lag coefficients plus k x m exogenous coefficients. For a modest system of 4 endogenous variables, 6 media channels, and 3 lags, that is already 72 parameters --- far more than a typical marketing dataset (52--104 weeks) can reliably estimate without regularization.

The **Minnesota prior** (originally developed at the Federal Reserve Bank of Minneapolis) solves this by encoding three intuitive beliefs:

### 1. Own Persistence

Each variable's best predictor is its own recent past. The prior centers **own-lag-1 coefficients near 0.9**, expressing the belief that revenue this week is likely close to revenue last week. This encodes the fact that marketing time series are typically persistent and slow-moving.

### 2. Cross-Variable Shrinkage

The effect of *other* variables on a given variable is expected to be small. Cross-variable coefficients are shrunk toward zero with a tighter prior (lambda_cross = 0.1, versus lambda_overall = 0.2 for own effects). This prevents the model from overfitting to spurious correlations between variables --- a major risk with unrestricted VARs.

### 3. Lag Decay

Higher-order lags are less informative than recent lags. The Minnesota prior shrinks coefficients for lag 2, 3, ... progressively more aggressively, following the formula:

> **sigma(i,j,l) = lambda / l^delta x (sigma_yi / sigma_yj) x cross_tightness**

Where l is the lag order and delta = 1.0 controls how fast the shrinkage increases. The ratio sigma_yi / sigma_yj accounts for scale differences between variables.

### Why This Matters for Marketing

Without Minnesota priors, a Bayesian VAR on marketing data would face severe overfitting: too many parameters, too little data, and highly correlated media channels. The Minnesota prior provides principled regularization that:

- Keeps the model stable and interpretable even with limited data.
- Allows the data to override the prior where the evidence is strong (e.g., a clear TV → brand search relationship).
- Produces more reliable impulse response functions and long-run multipliers.

### Other Priors

- **Intercepts:** Normal(0, 0.5) or TruncatedNormal with bounds.
- **Exogenous coefficients:** Normal(0, 0.5) with optional sign constraints (e.g., media effects constrained to be positive).
- **Noise covariance:** LKJ Cholesky decomposition (eta=2.0) for multivariate case, or independent HalfNormal per equation for diagonal case.

---

## Data Transformations

All endogenous variables are automatically transformed via **log1p** (robust to zeros). Exogenous variables default to log1p but support configurable transforms: asinh, log, log_shift, per_k, z-score, min-max, and index100. Results are converted back to percent-per-percent elasticities for interpretability.

---

## Sampling Configuration

Default sampling parameters:
- **Draws:** 2,000 posterior samples
- **Tune:** 1,000 burn-in samples
- **Chains:** 2 (configurable up to 4)
- **Target accept:** 0.9
- Optional JAX/NumPyro backend for acceleration

---

## Key VAR Concepts

### Impulse Response Functions (IRFs)

An IRF traces how a one-unit shock to one variable propagates through the entire system over time. For example, an IRF for TV → Revenue shows the cumulative revenue impact of a one-unit increase in TV spend, accounting for all the indirect pathways (TV → awareness → brand search → revenue, etc.).

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

The number of lags (p) is **user-configured** in the model setup. There is no automatic lag order selection (AIC/BIC). The lag order determines how many past periods each variable uses to predict the current period.

Practical guidance:

- **1--2 lags** for weekly data when you expect effects to materialize quickly (e.g., paid search → conversions).
- **3--4 lags** for weekly data when you expect slower brand-building dynamics (e.g., TV → brand awareness → revenue may take several weeks).
- **Higher lags** capture longer memory but require proportionally more data and increase the number of parameters. With Minnesota priors, the higher-lag coefficients are automatically shrunk, so the risk of overfitting is managed.

### Minimum Data

The model requires at least **lags + 10 observations**. For example, a 4-lag model on weekly data needs at least 14 weeks. In practice, 52+ weeks is recommended for reliable estimates, and 104+ weeks is ideal if you want stable long-run multipliers.

### Choosing Endogenous vs. Exogenous Variables

A key modeling decision is which variables to treat as endogenous (part of the feedback system) and which to treat as exogenous (one-way inputs):

- **Endogenous (typical):** Revenue, brand awareness, brand search volume, consideration, NPS, or any brand equity metric that you believe interacts with other business outcomes.
- **Exogenous (typical):** Media spend by channel (TV, social, display, etc.) --- these are controlled inputs that you set, not outcomes of the system.
- **Flexible:** Brand search can go either way. If branded search volume responds to other media (e.g., TV drives brand search) and also drives revenue, treat it as endogenous. If it is purely a media input you control, treat it as exogenous.

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

## References

- Danaher, P.J. & van Heerde, H.J. (2018). Delusion in attribution: Caveats in using attribution for multimedia budget allocation. *Journal of Marketing Research*, 55(5), 667-685.
- [Bayesian Vector Autoregressive Models for Marketing](https://www.sciencedirect.com/science/article/abs/pii/S0167811621000495) --- Foundational reference on Bayesian VAR applications in marketing, covering long-run effects, impulse responses, and the role of Minnesota priors in marketing systems.

---

## Next Steps

- [Marketing Mix Modeling](./marketing-mix-modeling.md) --- The standard MMM approach for channel attribution.
- [Bayesian Modeling](./bayesian-modeling.md) --- The statistical foundation shared by MMM and VAR.
- [Incrementality](./incrementality.md) --- Causal impact measurement.
