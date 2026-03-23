# Core Concepts

Welcome to the Simba core concepts library. These pages explain the statistical and marketing foundations behind Simba's Bayesian Marketing Mix Modeling platform. Whether you are a marketing analyst building your first model or a data scientist fine-tuning priors, these guides will give you the conceptual grounding you need.

---

## Concept Guides

### [Marketing Mix Modeling (MMM)](./marketing-mix-modeling.md)
What Marketing Mix Modeling is, how it differs from multi-touch attribution, and why Bayesian MMM is the gold standard for measuring media effectiveness across channels.

### [Bayesian Modeling](./bayesian-modeling.md)
The statistical engine behind Simba. Learn how Bayesian inference works, why it outperforms traditional regression for marketing measurement, and how uncertainty quantification gives you confidence in every decision.

### [Incrementality](./incrementality.md)
How Simba separates organic demand from media-driven lift so you can measure the true causal impact of every marketing dollar.

### [Saturation Curves](./saturation-curves.md)
Understanding diminishing returns in media spend, how the tanh saturation function works, and how to interpret and configure saturation parameters in Simba.

### [Adstock Effects](./adstock-effects.md)
How advertising impact carries over time, why different channels have different decay rates, and how to configure carryover parameters for accurate measurement.

### [Priors and Distributions](./priors-and-distributions.md)
A practical guide to Bayesian priors in Simba, including the distribution types available (InverseGamma, TruncatedNormal, and more), smart defaults, and when to bring your own domain expertise.

### [VAR Modeling](./var-modeling.md) 
What Vector AutoRegression (VAR) is, how it differs from standard MMM, and when to use it for understanding inter-channel dynamics and system-level marketing effects.### [Halo Effects](./halo-effects.md)How advertising for one brand can lift sales of related brands in a portfolio, and how Simba models cross-brand marketing impact through halo channels and trademark channels.

### [Seasonality](./seasonality.md)
How seasonal patterns influence marketing measurement and how Simba accounts for holidays, cyclical demand, and time-based trends automatically.

---

## How These Concepts Fit Together

Simba's four-step workflow --- **Audit, Measure, Predict, Optimize** --- draws on every concept above:

1. **Audit** --- Your data is validated and prepared. Seasonality patterns and baseline trends are identified.
2. **Measure** --- A Bayesian model is fitted using the priors, saturation curves, and adstock structures you configure. The result is a full posterior distribution over every parameter, giving you incrementality estimates with calibrated uncertainty.
3. **Predict** --- The fitted model forecasts future outcomes under different spend scenarios, respecting saturation limits and carryover dynamics.
4. **Optimize** --- Simba's optimizer recommends budget allocations that maximize incremental return, informed by every concept on this page.

Each concept page is self-contained, but reading them in the order listed above will give you the most coherent understanding of the platform.
