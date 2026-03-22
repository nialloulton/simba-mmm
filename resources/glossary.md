# Glossary — Marketing Mix Modeling and Bayesian Statistics Terminology

A comprehensive reference of terms used in marketing mix modeling (MMM), Bayesian statistics, and the Simba platform.

---

## A

### Adstock
The carryover effect of advertising. When a TV ad airs this week, its impact doesn't disappear immediately — it "stocks up" and decays over time. Adstock parameters in Simba control how quickly each channel's impact fades. Also called **carryover** or **lag effect**.

### AES-256
Advanced Encryption Standard with 256-bit key length. The encryption standard used by Simba for data at rest. Considered the gold standard for symmetric encryption, used by financial institutions and government agencies.

### Attribution
The process of assigning credit for business outcomes (e.g., sales) to specific marketing activities. In MMM, attribution is based on statistical modeling of aggregate data, not individual user tracking.

---

## B

### Base Sales
The level of sales or revenue that would occur without any marketing activity. In MMM, base sales represent organic demand driven by brand equity, distribution, pricing, and other non-media factors. Simba separates base sales from media-driven incremental lift.

### Bayesian Inference
A statistical method that updates probability estimates as new data becomes available. Instead of producing a single "best guess" (like frequentist methods), Bayesian inference produces a full probability distribution over possible values, quantifying uncertainty. Simba uses Bayesian inference for all model fitting.

### Bayesian MMM
Marketing mix modeling that uses Bayesian statistical methods. Advantages over traditional (frequentist) MMM include uncertainty quantification, prior knowledge integration, and better performance with limited data. Simba is a Bayesian MMM platform.

---

## C

### Carryover
See **Adstock**. The lagged impact of advertising beyond the period in which it was delivered.

### Causal Attribution
Determining which marketing activities actually *caused* business outcomes, as opposed to merely being correlated with them. Bayesian MMM with proper controls provides causal (not just correlational) attribution.

### Confidence Interval
In frequentist statistics, a range of values that contains the true parameter with a certain probability. In Bayesian statistics, the analogous concept is a **credible interval**, which Simba uses.

### Credible Interval
The Bayesian equivalent of a confidence interval. A 95% credible interval means there is a 95% probability that the true value falls within this range, given the data and model. More intuitive and directly interpretable than frequentist confidence intervals.

### Cyber Essentials
A UK Government-backed security certification scheme. Demonstrates adherence to fundamental cybersecurity standards including firewalls, secure configuration, access control, malware protection, and patch management. Simba is Cyber Essentials certified.

---

## D

### Data Auditor
Simba's AI-powered data validation system. Automatically checks uploaded data for missing values, anomalies, schema issues, and quality problems before modeling. Produces a Data Health Score.

### Data Health Score
A 0–100% score assigned by Simba's Data Auditor indicating the overall quality and completeness of your uploaded data. Higher scores indicate cleaner, more model-ready data.

### Decay Rate
The speed at which the impact of advertising diminishes over time. A high decay rate means the effect fades quickly (typical of digital ads); a low decay rate means the effect persists (typical of TV). Configured per channel in Simba's model settings.

### Diminishing Returns
The phenomenon where additional spend on a channel produces progressively less incremental impact. The first $100K in TV spend may produce significant lift, but the 10th $100K produces much less. Modeled in Simba through **saturation curves**.

### Distribution (Statistical)
A mathematical function describing the probability of different outcomes. In Simba, distributions are used to define **priors** on model parameters. Common distributions include InverseGamma and TruncatedNormal.

---

## G

### GDPR
General Data Protection Regulation. EU regulation governing the collection, processing, and storage of personal data. Simba is fully GDPR compliant.

### Glass-Box
Simba's term for full model transparency — the opposite of a black-box. In a glass-box model, every prior, parameter, assumption, and computation is inspectable and auditable.

### GRP (Gross Rating Point)
A measure of advertising exposure for TV. One GRP represents reaching 1% of the target audience one time. Common input variable for TV in marketing mix models.

---

## I

### Incrementality
The additional business outcome (revenue, conversions, etc.) that would not have occurred without marketing activity. Simba measures incrementality by isolating the causal impact of each media channel from base sales and other factors.

### InverseGamma Distribution
A continuous probability distribution commonly used as a prior for variance parameters in Bayesian models. In Simba, it's one of the available distribution types for configuring channel priors.

---

## L

### Lift
The incremental increase in a business metric attributable to a specific marketing activity. For example, if TV advertising produces a 15% lift in revenue, it means revenue was 15% higher than it would have been without TV.

### Lift Test
An experiment (often randomized) designed to measure the incremental impact of marketing activity. Simba supports lift test integration to validate model results against experimental data.

### Long-Term Effects
The lasting impact of marketing on brand equity, awareness, and consideration that extends beyond the immediate sales response. Simba's long-term effects model (available on Pro tier and above) captures these sustained impacts.

---

## M

### Media Lift
The incremental revenue or outcome attributable to media spending, separated from base sales. In Simba's measurement view, media lift shows exactly how much value each channel is driving above what would happen organically.

### Media Mix
The combination of marketing channels used in a campaign or marketing plan. Typically includes TV, digital, social, search, OOH, and other channels.

### MMM (Marketing Mix Modeling)
A statistical analysis technique that uses aggregate time-series data to measure the impact of marketing activities on business outcomes. MMM quantifies the contribution of each channel while accounting for saturation, carryover, and seasonality.

### Model Fit
The process of running Bayesian inference on your data to estimate model parameters. In Simba, a "model fit" consumes one of your monthly allocation (depending on your plan tier).

### MTA (Multi-Touch Attribution)
A user-level attribution method that tracks individual customer journeys across touchpoints. Unlike MMM, MTA relies on cookies/device tracking and struggles with iOS privacy changes, walled gardens, and offline channels. MMM and MTA are complementary approaches.

---

## O

### Optimization
The process of determining the ideal budget allocation across channels to maximize ROI (or another objective) subject to constraints. Simba's budget optimizer is risk-adjusted and carryover-aware.

---

## P

### Portfolio Model
A model that spans multiple brands, markets, or clients — enabling cross-entity comparison and optimization. Available on Simba's Scale tier and above.

### Posterior Distribution
In Bayesian statistics, the distribution of a parameter *after* observing data. The posterior combines the prior (what you knew before) with the likelihood (what the data tells you). All of Simba's results are posterior distributions.

### Prior (Prior Distribution)
In Bayesian statistics, a probability distribution representing what you believe about a parameter *before* seeing the data. Priors encode domain knowledge — for example, TV advertising typically has a positive effect on sales. Simba lets you configure priors per channel.

### PyMC
An open-source probabilistic programming library for Python. PyMC is the computational engine behind Bayesian inference in Simba and PyMC-Marketing.

### PyMC-Marketing
The open-source library for Bayesian marketing analytics that Simba is built upon. PyMC-Marketing provides the statistical models for media mix modeling, including saturation, adstock, and Bayesian inference.

---

## R

### ROAS (Return on Ad Spend)
Revenue generated per unit of ad spend. ROAS = Revenue / Spend. In MMM, ROAS typically refers to *incremental* ROAS — the additional revenue attributable to media, divided by spend.

### ROI (Return on Investment)
A broader measure of investment efficiency. ROI = (Gain - Cost) / Cost. In the context of MMM, ROI captures the net return from marketing investment after accounting for the cost.

---

## S

### Saturation
The point at which additional spend on a channel produces diminishing incremental returns. Simba uses mathematical saturation functions (e.g., tanh) to model this non-linear relationship between spend and impact. See **Saturation Curve**.

### Saturation Curve
A mathematical function that models the relationship between media input (spend, impressions) and output (revenue, conversions). Common forms include tanh (hyperbolic tangent) and logistic functions. The saturation parameter in Simba controls how quickly a channel reaches its effectiveness ceiling.

### Scenario Planning
The process of modeling different budget allocation strategies to forecast their likely outcomes. Simba's scenario planner lets you compare aggressive, base case, and conservative projections with uncertainty bands.

### Seasonality
Regular, predictable patterns in business outcomes that repeat over time — such as holiday shopping spikes, summer slowdowns, or back-to-school periods. Simba models seasonality automatically to separate its effect from media impact.

### Smart Defaults
Simba's auto-generated model starting points. Based on your historical data and industry benchmarks, smart defaults provide sensible initial values for priors, saturation, and decay parameters — which you can then fine-tune with domain expertise.

---

## T

### TLS 1.3
Transport Layer Security version 1.3. The latest and most secure version of the TLS protocol, used by Simba for encrypting data in transit between your browser and the platform.

### TruncatedNormal Distribution
A normal (Gaussian) distribution that is truncated to a specific range. Used as a prior distribution in Bayesian models when you want to constrain a parameter to positive values or a specific range. Available in Simba's model configuration.

---

## U

### Uncertainty Quantification
The process of expressing how confident you are in a result. In Bayesian MMM, every estimate comes with a full probability distribution — not just a single number. This allows you to understand the range of plausible outcomes and make risk-aware decisions.

---

## W

### What-If Analysis
A form of scenario planning where you change one or more input variables (e.g., "what if I increase TV spend by 20%?") and observe the predicted impact on outcomes. Simba's scenario planner supports what-if analysis with full uncertainty quantification.

---

*Missing a term? [Let us know](../../../issues/new?template=support_question.yml) and we'll add it.*

*See also: [Core Concepts](../docs/core-concepts/README.md) | [FAQ](../docs/faq/README.md)*

---

## Data Pipeline
A visual, node-based workflow in Simba for preparing data before modeling. Pipelines combine data source connectors (CSV, Excel, external APIs) with transform nodes (filter, merge, aggregate) to create repeatable, versioned data preparation processes.

### Delayed Adstock
An adstock formulation where the peak effect does not occur immediately but builds to a maximum after a configurable delay, then decays. Used for channels where impact takes time to materialize, such as brand-building TV campaigns or sponsorships. See **Adstock**.

---

## F

### FEVD (Forecast Error Variance Decomposition)
A statistical technique used in VAR (Vector AutoRegression) models that decomposes the forecast uncertainty of one variable into the contributions of shocks from all variables in the system. In marketing, FEVD shows how much of the uncertainty in revenue forecasts is attributable to changes in each marketing channel. See **VAR**.

---

## H

### Halo Effect
In marketing, the phenomenon where advertising for one brand or product generates incremental lift for related brands or products in the same portfolio. Simba models halo effects through halo channels and trademark channels, enabling cross-brand optimization that accounts for portfolio-wide marketing impact.

### Half-Life
The number of time periods it takes for a channel's adstock (carryover) effect to decay to 50% of its initial value. A channel with a half-life of 2 weeks retains half its impact after two weeks and a quarter after four weeks. A more intuitive alternative to the raw decay rate parameter.

---

## P


### Prior Predictive Check
A validation step for Bayesian models where sample forecasts are generated from the prior distributions (before seeing data) to confirm that the priors produce sensible ranges. Used in VAR modeling to validate that prior configurations are reasonable before committing to a full model fit.

---

## T

### Trademark Channel
A virtual channel in Simba that represents masterbrand, portfolio-level, or corporate advertising benefiting multiple brands simultaneously. Unlike halo channels (which are brand-specific), trademark channels are always global and affect all brands in the portfolio equally. Three types exist: masterbrand, portfolio, and corporate. See **Halo Effect**.

### Two-Factor Authentication (2FA)
An additional security layer that requires a time-based one-time password (TOTP) from an authenticator app in addition to your email and password when logging in. Supported in Simba for enhanced account security.

---

## V

### VAR (Vector AutoRegression)
A statistical model where each variable in the system is modeled as a function of its own past values and the past values of all other variables. Unlike standard MMM (which models a single target as a function of inputs), VAR models the entire system of interactions between marketing channels and outcomes simultaneously. Available on Trial, Pro, and Scale tiers in Simba.
