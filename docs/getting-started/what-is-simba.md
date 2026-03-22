# What is Simba? — Bayesian Marketing Mix Modeling Platform

Simba is a no-code Bayesian Marketing Mix Modeling (MMM) platform built on [PyMC-Marketing](../core-concepts/bayesian-modeling.md), the leading open-source Bayesian marketing science framework. [Simba](https://getsimba.ai) makes advanced econometric modeling accessible to marketers, analysts, and agencies without requiring programming skills or a PhD in statistics.

Marketing Mix Modeling answers the fundamental question every marketer faces: **which channels are actually driving results, and how should I allocate my budget?** Simba gives you those answers with full statistical transparency, uncertainty quantification, and actionable optimization recommendations.

---

## The Problems Simba Solves

### Attribution is broken
Last-click and multi-touch attribution models rely on user-level tracking that is increasingly unreliable. Privacy regulations like GDPR, the deprecation of third-party cookies, and platform signal loss (iOS App Tracking Transparency, for example) have made digital attribution less and less trustworthy. MMM sidesteps these issues entirely by working with aggregated data — no cookies, no pixels, no user-level tracking required.

### Black-box tools erode trust
Many marketing analytics platforms produce a single point estimate with no explanation of how they arrived at it. When a tool tells you that paid search drove 23% of revenue but cannot explain its assumptions, confidence intervals, or methodology, you are making million-dollar decisions on faith. Simba is a **glass-box** platform: every model assumption, prior distribution, and posterior result is visible and auditable.

### Traditional MMM is slow and expensive
Classic marketing mix modeling engagements involve months of consulting work, custom R or Python code, and six-figure price tags. Simba compresses this into a self-serve workflow that takes days, not months, while preserving the statistical rigor that makes MMM valuable.

### Optimization is disconnected from measurement
Most measurement tools stop at telling you what happened. Simba carries the analysis forward into [scenario planning](../workflow/scenario-planning.md) and [budget optimization](../workflow/budget-optimization.md), so you move from insight to action in a single platform.

---

## Who Simba is Built For

### Brand Marketers and Marketing Leaders
You need to justify spend, report on channel effectiveness, and make budget decisions with confidence. Simba gives you clear, defensible answers without requiring you to learn Python or Bayesian statistics. Smart defaults and the AI Data Auditor guide you through every step.

### Agencies and Consultancies
You manage multiple clients, each with unique data and channel mixes. Simba's workspace model and the Scale plan are designed for multi-client management. You can deliver rigorous MMM results to clients faster, with transparent methodology that builds trust.

### Data Science and Analytics Teams
You understand the statistics but want to move faster than building custom PyMC-Marketing pipelines from scratch. Simba gives you a configurable UI for setting [priors](../model-configuration/setting-priors.md), [saturation curves](../model-configuration/saturation-curves.md), and [adstock transformations](../model-configuration/adstock-settings.md) while the PyMC-Marketing engine handles the inference. You get the rigor without the boilerplate.

### Performance Marketing Teams
You need to understand the incremental impact of each channel, including those that digital attribution consistently overvalues or undervalues. Simba quantifies true incrementality with Bayesian credible intervals, giving you a statistically grounded basis for optimization.

---

## How Simba Differs from Traditional MMM Tools

| Aspect | Traditional MMM | Simba |
|---|---|---|
| **Methodology** | Frequentist regression, often opaque | Bayesian inference via PyMC-Marketing, fully transparent |
| **Uncertainty** | Single point estimates | Full posterior distributions with credible intervals |
| **Prior knowledge** | Ignored or ad hoc | Formally incorporated via configurable prior distributions |
| **Coding required** | Yes (R, Python, SAS) | No — complete no-code interface |
| **Time to results** | Weeks to months | Days |
| **Model transparency** | Black box or consultant-dependent | Glass box — every assumption visible |
| **Optimization** | Separate tool or manual process | Built-in scenario planning and budget optimization |
| **Data validation** | Manual QA | AI Data Auditor automates checks |
| **Updates** | Expensive re-engagement | Re-run models as new data arrives |

---

## The PyMC-Marketing Foundation

Simba is built on [PyMC-Marketing](../core-concepts/bayesian-modeling.md), the open-source Bayesian marketing science library maintained by the PyMC Labs team. This means:

- **Proven methodology.** PyMC-Marketing implements peer-reviewed Bayesian media mix modeling techniques used by leading data science teams worldwide.
- **Active development.** The underlying engine benefits from continuous improvements by a global open-source community.
- **No vendor lock-in.** The statistical methodology is open-source and transparent. Simba adds the no-code interface, workflow automation, AI-driven defaults, security infrastructure, and optimization engine on top.
- **Extensibility.** For teams that want to go deeper, the PyMC-Marketing foundation means your models are compatible with the broader PyMC ecosystem.

Learn more about the Bayesian approach in [Bayesian Modeling in Marketing](../core-concepts/bayesian-modeling.md).

---

## Key Capabilities

### 1. AI Data Auditor (Audit)
Before you build a model, Simba's AI Data Auditor examines your dataset for issues that could compromise results. It checks for missing values, outliers, multicollinearity, stationarity concerns, and data formatting problems. You get a clear report with actionable recommendations before any modeling begins.

Read more: [AI Data Auditor](../workflow/ai-data-auditor.md)

### 2. Incremental Measurement (Measure)
The core modeling step builds a Bayesian marketing mix model from your data. Simba estimates the incremental contribution of each marketing channel to your KPI, accounting for [adstock effects](../model-configuration/adstock-settings.md) (how marketing impact carries over time) and [saturation](../model-configuration/saturation-curves.md) (diminishing returns at higher spend levels). Results include full posterior distributions, not just point estimates.

Read more: [Incremental Measurement](../workflow/incremental-measurement.md)

### 3. Scenario Planning (Predict)
Once your model is built, Scenario Planning lets you ask "what if" questions. What happens if you shift 20% of TV budget to paid social? What is the expected outcome if you increase total spend by 15%? Simba simulates the scenarios using your fitted model and shows the predicted impact with uncertainty bands.

Read more: [Scenario Planning](../workflow/scenario-planning.md)

### 4. Budget Intelligence (Optimize)
Budget Intelligence takes optimization further by algorithmically searching for the budget allocation that maximizes (or targets) your chosen KPI. Instead of manually testing scenarios, you define constraints and objectives, and Simba recommends the optimal channel mix backed by the full Bayesian model.

Read more: [Budget Optimization](../workflow/budget-optimization.md)

### Smart Defaults
Simba auto-generates intelligent default configurations — priors, adstock parameters, saturation settings — from your historical data. This means you can run a credible model immediately, then refine settings as you learn more. Smart defaults lower the barrier to entry without sacrificing rigor.

Read more: [Smart Defaults](../model-configuration/smart-defaults.md)

### Security and Compliance
Your data is protected with AES-256 encryption at rest, TLS 1.3 in transit, isolated AWS S3 storage buckets per workspace, and compliance with GDPR and Cyber Essentials certification standards.

Read more: [Security and Compliance](../platform/security-and-compliance.md)

---

## How Simba Fits Into Your Marketing Stack

Simba is not a replacement for your ad platforms, analytics tools, or BI dashboards. It sits alongside them as your **strategic measurement and optimization layer**:

- **Ad platforms** (Google Ads, Meta, etc.) tell you what happened inside their walled gardens.
- **Web analytics** (GA4, Adobe Analytics) track on-site behavior.
- **Simba** tells you the true incremental impact of each channel on your business KPIs, accounts for offline and external factors, and optimizes your budget allocation across all channels.

Simba works with aggregated, time-series data — typically weekly or daily summaries of spend, impressions, and KPIs. You do not need to connect APIs or share user-level data.

---

## Next Steps

Ready to get started? Head to the [Quick Start Guide](quick-start-guide.md) and build your first marketing mix model in minutes.

Or, if you want to set up your account and workspace first, see [Account Setup](account-setup.md).

---

## Related Documentation

- [Quick Start Guide](quick-start-guide.md) — Build your first model step by step
- [Platform Overview](platform-overview.md) — Navigate the Simba interface
- [Bayesian Modeling in Marketing](../core-concepts/bayesian-modeling.md) — Understand the methodology
- [Data Requirements](../data-preparation/data-requirements.md) — What data you need to get started
- [Pricing and Plans](https://getsimba.ai) — Visit getsimba.ai for current pricing details
