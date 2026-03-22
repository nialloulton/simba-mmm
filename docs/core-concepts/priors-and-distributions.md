# Priors and Distributions --- Configuring Bayesian Priors in Simba

Priors are one of the most powerful features of Bayesian modeling. They let you tell the model what you already know --- or believe --- about a parameter before it sees any data. In Simba, priors are fully configurable through the UI, giving you control over every aspect of the model while providing sensible defaults that work out of the box.

---

## What Are Priors and Why Do They Matter?

In [Bayesian modeling](./bayesian-modeling.md), every parameter starts with a **prior distribution** --- a probability distribution that represents your beliefs about the parameter before observing data. The model then combines this prior with the observed data (via the likelihood) to produce the **posterior distribution** --- your updated beliefs.

Priors matter for several reasons:

### 1. Encoding Domain Knowledge

If a lift test showed that paid search ROAS is between 2x and 4x, you can add this as a calibration observation in the Model Details step. The model will use this experimental evidence as additional likelihood data alongside the time-series data, producing more accurate and stable estimates.

### 2. Regularization

Priors prevent the model from arriving at implausible parameter values. For example, a prior that constrains a channel's effect to be positive prevents the model from estimating that spending more on a profitable channel decreases sales --- a result that sometimes occurs in frequentist regression due to multicollinearity or noise.

### 3. Handling Sparse Data

When a channel was only active for a few weeks, the data alone may not be sufficient to estimate its effect reliably. A prior provides a starting point that keeps the estimate reasonable until more data accumulates.

### 4. Transparency

Because Simba is a fully transparent platform, every prior is visible and inspectable. Stakeholders can review the assumptions encoded in the model and challenge them if needed. This is far more transparent than the implicit assumptions buried in frequentist model specifications.

---

## Types of Distributions in Simba

Simba supports several probability distributions for specifying priors. Each distribution has different properties that make it suitable for different types of parameters.

### Normal

The **Normal** (Gaussian) distribution is the most common prior distribution, defined on the entire real line. It is symmetric and bell-shaped.

**When Simba uses Normal:**
- Default prior for channel coefficients and other unconstrained parameters
- Parameters where both positive and negative values are plausible

**Key parameters:**
- **mu (mean)** --- The center of the distribution, representing your best guess for the parameter value.
- **sigma (standard deviation)** --- How uncertain you are. Larger sigma means a wider, more uncertain prior.

### InverseGamma

The **InverseGamma** distribution is commonly used as a prior for variance and scale parameters. It is defined on positive real numbers and has a right-skewed shape.

**When Simba uses InverseGamma:**
- Noise variance (the model's observation noise parameter)
- Scale parameters where the value must be positive and could be large

**Key parameters:**
- **alpha (shape)** --- Controls how concentrated the distribution is. Larger alpha means a tighter distribution.
- **beta (scale)** --- Shifts the distribution's center. Larger beta moves the mass toward larger values.

**Practical interpretation:** An InverseGamma prior on noise variance says "I expect the unexplained variation in my data to be roughly this large, but I am open to it being somewhat larger."

### TruncatedNormal

The **TruncatedNormal** distribution is a normal (bell-curve) distribution that is cut off at specified lower and/or upper bounds. This is extremely useful in marketing contexts where you know a parameter should fall within a certain range.

**When Simba uses TruncatedNormal:**
- Channel coefficients (effects of media spend on outcome)
- Adstock decay rates
- Saturation parameters

**Key parameters:**
- **mu (mean)** --- The center of the distribution, representing your best guess for the parameter value.
- **sigma (standard deviation)** --- How uncertain you are. Larger sigma means a wider, more uncertain prior.
- **lower** --- The minimum allowed value (e.g., 0 for a parameter that must be positive).
- **upper** --- The maximum allowed value (e.g., 1 for a decay rate).

**Practical interpretation:** A TruncatedNormal(mu=0.5, sigma=0.2, lower=0, upper=1) prior on a decay rate says "I expect the decay rate to be around 0.5 (half-life of about 1 week), but it could reasonably be anywhere from 0.2 to 0.8. It cannot be negative or exceed 1."

### HalfNormal

The **HalfNormal** distribution is a normal distribution folded at zero, keeping only the positive half. It is used for parameters that must be positive but where you do not have a strong expectation about the magnitude.

**When Simba uses HalfNormal:**
- Standard deviation parameters
- Effect sizes where positivity is assumed but the magnitude is uncertain

**Key parameters:**
- **sigma** --- Controls the spread. Larger sigma means the prior allows larger values.

### Beta

The **Beta** distribution is defined on the interval (0, 1), making it a natural choice for parameters that represent probabilities or rates.

**When Simba uses Beta:**
- Adstock decay rates (which must fall between 0 and 1)
- Parameters that represent proportions

**Key parameters:**
- **alpha and beta** --- Shape parameters that control the distribution's center and spread. Equal values center the distribution at 0.5; alpha > beta shifts it toward 1; alpha < beta shifts it toward 0.

### LogNormal

The **LogNormal** distribution is defined on positive real numbers and is right-skewed. It is useful for parameters that are strictly positive and may span several orders of magnitude.

**When Simba uses LogNormal:**
- Saturation scale parameters
- Parameters where the range of plausible values is wide

---

## How to Set Priors in Simba's UI

Simba's model configuration screen exposes prior settings for every parameter in the model. Here is the workflow:

### Step 1: Review the Defaults

When you add a channel or configure a model component, Simba automatically assigns default priors. These defaults are designed to be **weakly informative** --- they constrain parameters to reasonable ranges without imposing strong assumptions.

The UI displays each prior as a distribution curve alongside its parameters, so you can see the shape and range at a glance.

### Step 2: Decide Whether to Customize

For most users and most channels, the defaults are appropriate. Consider customizing priors when:

- You have **lift test results** or **experimental data** for a channel.
- You have **strong domain expertise** about a channel's behavior (e.g., you know from years of experience that TV has a long carryover in your category).
- A channel has **very limited data** and you want to stabilize the estimate.
- You want to **test sensitivity** by running the model with different priors to see how much the results change.

### Step 3: Adjust Parameters

For any parameter, you can modify the distribution type and its parameters directly in the UI. Simba provides:

- **Numeric inputs** for each distribution parameter (mu, sigma, alpha, beta, lower, upper).
- **A live visualization** of the prior distribution that updates as you change values, showing you exactly what your prior implies.
- **Context-sensitive guidance** that explains what each parameter controls and suggests reasonable ranges.

### Step 4: Validate Visually

Before fitting the model, review the prior summary panel. This shows all priors across all channels and parameters in a single view, making it easy to spot inconsistencies or unintended settings.

---

## Smart Defaults vs. Manual Configuration

### When Smart Defaults Are Sufficient

Smart defaults work well when:

- You are building your first model and do not have strong priors.
- Your dataset is reasonably large (1+ years of weekly data).
- You want a quick initial model to establish a baseline.
- You trust the model to learn from the data without much guidance.

### When Manual Configuration Adds Value

Manual configuration is worth the effort when:

- **Lift test calibration.** You have experimental results that should anchor the model. Adding lift test results as calibration observations in the Model Details step is one of the highest-value actions you can take. The lift test data enters the model as additional likelihood terms that constrain the channel response curve.
- **Known channel behavior.** If your media team has deep experience with a channel and can articulate expectations about decay rates or saturation points, encoding that knowledge improves accuracy.
- **Sparse channels.** A channel that was only active for 4 to 6 weeks will have a poorly identified effect from data alone. A reasonable prior keeps the estimate sensible.
- **Sensitivity analysis.** Running the model with different priors helps you understand which results are driven by data and which are driven by assumptions.

---

## When to Adjust Priors: Practical Guidance

### Scenario: You Have a Lift Test Result

Suppose a geo-based lift test for paid social showed a 15% incremental lift with a 95% confidence interval of 10% to 20%.

**Action:** Set a TruncatedNormal prior on the paid social coefficient with mu centered on the lift test estimate and sigma reflecting the confidence interval width. Set the lower bound to 0 (assuming positive effect). This tells the model: "I have experimental evidence that paid social's effect is around this range. Weight the data accordingly."

### Scenario: A Channel Has Limited History

You launched a new CTV (Connected TV) channel three months ago, giving you only 12 weekly observations.

**Action:** Use a moderately informative prior on the CTV coefficient, perhaps based on industry benchmarks for CTV effectiveness or on your TV channel's estimated effect (since CTV is a similar medium). Without this guidance, 12 data points may not be enough for the model to estimate the effect reliably.

### Scenario: A Channel's Effect Seems Implausible

After fitting the model, you notice that email marketing has a suspiciously high coefficient --- higher than all other channels despite modest spend.

**Action:** Check the prior. If it is very wide (weakly informative), the model may have latched onto a spurious correlation. Consider tightening the prior based on your expectations for email's effectiveness, then refit. If the posterior still shows a high effect, the data is strongly supporting it. If it moderates, the original estimate was likely noise-driven.

### Scenario: You Want to Test Sensitivity

You are presenting results to stakeholders and want to show that the conclusions are robust.

**Action:** Run the model with two or three different prior specifications --- for example, the default priors, tighter priors, and wider priors. If the key conclusions (channel rankings, budget allocation recommendations) are stable across prior choices, you can present the results with greater confidence.

---

## Fully Transparent Prior Configuration

One of Simba's core design principles is that every assumption is visible. The prior configuration panel is a key expression of this principle:

- Every prior is displayed with its distribution type and parameters.
- The posterior is shown alongside the prior after model fitting, so you can see how much the data updated your initial beliefs.
- If a posterior looks nearly identical to its prior, it means the data did not provide enough information to update the assumption --- a signal that you may want to collect more data or reconsider the model structure.

This transparency ensures that no assumption is hidden. Stakeholders can review the priors, challenge them, and understand exactly how they influence the results.

---

## Key Takeaways

- Priors encode your beliefs about model parameters before observing data. They are combined with data to produce posterior distributions.
- Simba uses distributions including Normal (for unconstrained parameters), InverseGamma (for variance parameters), TruncatedNormal (for bounded parameters like coefficients and decay rates), HalfNormal, Beta, and LogNormal.
- Smart defaults provide weakly informative priors that work well for most use cases. Customize when you have lift test results, domain expertise, or sparse data.
- Simba's UI provides live visualization and context-sensitive guidance for prior configuration.
- Full transparency means every prior is visible, inspectable, and auditable.

---

## Next Steps

- [Bayesian Modeling](./bayesian-modeling.md) --- Understand the full prior-likelihood-posterior workflow.
- [Saturation Curves](./saturation-curves.md) --- Learn about the parameters that saturation priors control.
- [Adstock Effects](./adstock-effects.md) --- See how priors shape carryover estimation.
