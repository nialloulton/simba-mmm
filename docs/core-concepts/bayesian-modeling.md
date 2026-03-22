# Bayesian Modeling --- The Statistical Foundation Behind Simba

Simba is built on Bayesian statistics. This page explains what that means, why it matters for marketing measurement, and how it works in practice --- all without assuming a statistics background.

---

## What Is Bayesian Inference?

Bayesian inference is a method of learning from data. It starts with a **belief** about how something works, observes new **evidence**, and then updates that belief to produce a more informed conclusion.

Here is the intuition: imagine you are evaluating a new paid social campaign. Before seeing any results, you have some expectation about how effective it will be --- maybe based on past campaigns, industry benchmarks, or your own experience. That initial expectation is your **prior belief**. Once the campaign runs and you observe actual performance data, you combine that data with your prior belief to form an **updated belief** --- your **posterior**.

This is exactly what Bayesian inference does, but with mathematical precision.

---

## The Three-Step Workflow: Prior, Likelihood, Posterior

Every Bayesian model follows the same logical structure:

### Step 1: Define the Prior

The **prior** represents what you believe about a parameter before seeing the data. In Simba, priors describe your expectations about things like:

- How effective each channel is at driving conversions
- How quickly the impact of an ad decays over time ([adstock](./adstock-effects.md))
- How steeply a channel's response saturates ([saturation curves](./saturation-curves.md))

Priors can be **informative** (expressing strong expectations, such as results from a lift test) or **weakly informative** (expressing only broad constraints, like "this parameter should be positive"). Simba provides smart default priors that work well for most use cases, and you can adjust them when you have domain knowledge. See [Priors and Distributions](./priors-and-distributions.md) for a full guide.

### Step 2: Define the Likelihood

The **likelihood** describes how the observed data relates to the model parameters. In an MMM context, the likelihood encodes the relationship between channel spend (after saturation and adstock transformations), control variables, seasonality, and the outcome variable. It answers the question: "Given a specific set of parameter values, how probable is the data we actually observed?"

You do not need to define the likelihood manually in Simba. The platform constructs it automatically from your data and model configuration.

### Step 3: Compute the Posterior

The **posterior** is the result of combining the prior and the likelihood using Bayes' theorem:

> **Posterior is proportional to Prior multiplied by Likelihood**

In plain language: your updated belief equals your initial belief, adjusted by the evidence. If the data strongly supports a particular parameter value, the posterior will concentrate there regardless of the prior. If the data is weak or ambiguous, the posterior will stay closer to the prior.

The posterior is not a single number --- it is a **distribution**. It tells you the full range of plausible values for each parameter, along with how probable each value is. This is the foundation of Bayesian uncertainty quantification.

---

## Why Bayesian Beats Frequentist for Marketing Measurement

Traditional (frequentist) regression --- the approach used in legacy MMM tools --- produces point estimates and p-values. Bayesian modeling produces full probability distributions. Here is why that difference matters in marketing:

### Uncertainty You Can Actually Use

A frequentist model might tell you that TV drives $2.1M in incremental revenue with a confidence interval of $1.5M to $2.7M. But what does that interval actually mean? In frequentist statistics, it means "if we repeated this analysis infinitely many times, 95% of the intervals would contain the true value." That is a statement about a hypothetical procedure, not about your specific estimate.

A Bayesian credible interval is far more intuitive: "Given our data and assumptions, there is a 94% probability that TV's true incremental contribution is between $1.5M and $2.7M." This is the statement marketers actually want to make.

### Incorporating What You Already Know

Frequentist regression treats every analysis as if you have zero prior knowledge. But in marketing, you almost always know something:

- A channel with positive ROAS is more likely than one with negative ROAS.
- A lift test showed paid search drives between 8% and 12% incremental lift.
- TV campaigns in your category typically have a half-life of two to four weeks.

Bayesian modeling lets you encode this knowledge directly through priors, leading to more accurate and stable estimates --- especially when data is limited.

### Graceful Handling of Sparse Data

Marketing datasets are often short. You may have only 52 to 104 weekly observations, with some channels active for only part of that period. Frequentist regression can produce wildly unstable estimates in these conditions. Bayesian priors act as principled regularization, keeping estimates reasonable even when data is scarce.

### No p-Value Theater

Frequentist analysis encourages a binary "significant or not" framing that is poorly suited to marketing decisions. A channel with a p-value of 0.06 is not meaningfully different from one with a p-value of 0.04, yet the significance threshold treats them completely differently. Bayesian analysis replaces this with continuous probabilities: "There is an 87% probability that this channel has a positive effect." This supports nuanced, risk-aware decision-making.

---

## How Simba Uses PyMC for Bayesian Computation

Simba's statistical engine is powered by **PyMC-Marketing**, an open-source probabilistic programming library maintained by the PyMC development team. PyMC-Marketing is purpose-built for marketing science applications, providing pre-built components for saturation functions, adstock transformations, and time-varying effects.

Under the hood, PyMC uses advanced sampling algorithms --- specifically **Markov Chain Monte Carlo (MCMC)** methods --- to explore the posterior distribution. The core sampler is the No-U-Turn Sampler (NUTS), a state-of-the-art variant of Hamiltonian Monte Carlo that efficiently handles high-dimensional parameter spaces.

You do not need to understand MCMC to use Simba. The platform manages sampling configuration, convergence diagnostics, and chain validation automatically. But if you are a data scientist who wants to go deeper, Simba exposes convergence metrics (R-hat, effective sample size, trace plots) for full diagnostic transparency.

---

## Uncertainty Quantification and Credible Intervals

One of the most powerful features of Bayesian modeling is **uncertainty quantification** --- the ability to assign probabilities to ranges of outcomes.

### What Is a Credible Interval?

A **credible interval** (sometimes called a Bayesian confidence interval) is a range of values that contains the true parameter with a stated probability. For example:

- "There is a 94% probability that paid search ROAS is between 2.1x and 3.8x."
- "There is a 94% probability that TV's incremental contribution last quarter was between $1.2M and $2.0M."

Simba uses **94% credible intervals** by default, which is a common convention in Bayesian analysis (chosen for technical reasons related to the tails of the posterior distribution).

### Why Uncertainty Matters for Decisions

Imagine two channels:

- **Channel A**: estimated ROAS of 3.0x, credible interval 2.5x to 3.5x
- **Channel B**: estimated ROAS of 4.0x, credible interval 0.5x to 8.0x

A naive analysis would favor Channel B because its point estimate is higher. But a risk-aware marketer would recognize that Channel B's wide interval means its true ROAS could easily be below Channel A's. Bayesian analysis gives you the information you need to make this distinction.

### Propagating Uncertainty Through Predictions

When Simba forecasts outcomes or optimizes budgets, it does not plug in point estimates. It samples from the full posterior distribution and propagates uncertainty through every calculation. The result is a predictive distribution --- a range of likely outcomes --- rather than a single number. This means budget recommendations come with honest assessments of upside and downside risk.

---

## Benefits of Bayesian Modeling in Simba

### Incorporate Domain Knowledge
Encode lift test results, industry benchmarks, and expert intuition as informative priors. The model treats this knowledge as evidence, weighting it against the observed data.

### Handle Sparse and Noisy Data
Short time series, channels with limited history, and noisy signals are all handled more robustly than with frequentist regression.

### Full Posterior Access
Every parameter in the model has a full posterior distribution, not just a point estimate. This enables richer analysis, scenario planning, and risk assessment.

### Principled Model Comparison
Bayesian methods offer natural tools for comparing model specifications (e.g., with or without a channel, different saturation functions) without relying on fragile hypothesis tests.

### Fully Transparent
Simba's UI lets you inspect every prior, posterior, and diagnostic. You can see exactly what the model assumed, how the data updated those assumptions, and how confident the final estimates are.

---

## Key Takeaways

- Bayesian inference updates prior beliefs with observed data to produce posterior distributions --- full probability statements about every parameter.
- Bayesian credible intervals are more intuitive and more useful for decision-making than frequentist confidence intervals.
- Priors let you incorporate domain knowledge, stabilize estimation with limited data, and avoid implausible results.
- Simba uses PyMC-Marketing's MCMC sampling engine to compute posteriors automatically, with full diagnostic transparency.
- Uncertainty propagation means Simba's predictions and optimizations are risk-aware by default.

---

## Next Steps

- [Priors and Distributions](./priors-and-distributions.md) --- Learn how to configure priors in Simba's UI.
- [Marketing Mix Modeling](./marketing-mix-modeling.md) --- See how Bayesian inference powers MMM.
- [Incrementality](./incrementality.md) --- Understand how Bayesian posteriors quantify causal impact.
