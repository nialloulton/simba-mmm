# VAR Modeling --- Vector AutoRegression for Marketing

Vector AutoRegression (VAR) is a multi-equation time series model that captures dynamic interactions between marketing channels. While standard MMM models a single target variable (revenue) as a function of marketing inputs, VAR models the entire system --- every variable predicts and is predicted by every other variable over time.

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

**VAR and standard MMM are complementary.** Use standard MMM for channel attribution and optimization. Use VAR for understanding inter-channel dynamics and system-level effects. Simba supports linking VAR models to standard models for side-by-side comparison.

---

## Key VAR Concepts

### Impulse Response Functions (IRFs)

An IRF traces how a one-unit shock to one variable propagates through the entire system over time. For example, an IRF for TV → Revenue shows the cumulative revenue impact of a one-unit increase in TV spend, accounting for all the indirect pathways (TV → search → revenue, TV → awareness → revenue, etc.).

IRFs capture the full dynamic response, including delayed and indirect effects that a single-equation model would miss.

### Forecast Error Variance Decomposition (FEVD)

FEVD decomposes the forecast uncertainty of each variable into the contributions of shocks from all variables in the system. In marketing terms, FEVD answers: "How much of the uncertainty in my revenue forecast is attributable to changes in TV, search, social, and other factors?"

A channel that explains a large share of revenue forecast variance is systemically important --- its fluctuations have outsized impact on business outcomes.

### Long-Run Effects

While IRFs show the time path of a shock's impact, long-run effects summarize the cumulative impact after the system has fully absorbed the shock. Long-run effects tell you the total eventual impact of a sustained change in one variable on all other variables.

---

## Prior Predictive Checking

Before fitting a VAR model, Simba supports **prior predictive checks** --- a validation step that generates sample forecasts from your prior distributions (before seeing data) to confirm that the priors produce sensible ranges.

If the prior predictive forecasts show unreasonable values (e.g., revenue going negative or exploding to unrealistic levels), you know to adjust your priors before committing to a full model fit. This saves computation time and ensures a well-specified model.

---

## Tier Availability

VAR modeling is available on the following tiers:

| Tier | VAR Available |
|------|---------------|
| Trial | Yes |
| Analyst | No |
| Pro | Yes |
| Scale | Yes |
| Enterprise | Yes |

---

## Next Steps

- [VAR Models in Simba](../platform-guide/var-models.md) --- Practical guide to building and interpreting VAR models
- [Marketing Mix Modeling](./marketing-mix-modeling.md) --- The standard MMM approach
- [Bayesian Modeling](./bayesian-modeling.md) --- The statistical foundation
- [Incrementality](./incrementality.md) --- Causal impact measurement
