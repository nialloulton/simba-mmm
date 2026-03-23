# Frequently Asked Questions

## General

### What is marketing mix modeling (MMM)?

Marketing mix modeling is a statistical analysis technique that measures the impact of marketing activities on sales and other business outcomes. Unlike digital attribution (which tracks individual user journeys), MMM uses aggregate time-series data to determine how much each marketing channel contributes to your business results.

Simba uses **Bayesian MMM** powered by PyMC-Marketing, which provides causal attribution while accounting for saturation effects, adstock (carryover), and seasonality.

→ [Learn more about MMM](../core-concepts/marketing-mix-modeling.md)

### How is Simba different from other MMM tools?

Simba is built on the open-source [PyMC-Marketing](https://www.pymc-marketing.io/) framework — meaning **full transparency, no black boxes**. You can inspect every prior, every model parameter, and every assumption behind your results.

Key differentiators:
- **Fully transparent** — inspect the actual Bayesian models driving your ROI
- **No-code interface** — configure complex Bayesian models without writing code
- **Data Validator** — automated data validation before modeling
- **Scenario planning** — test budget decisions with uncertainty bands before spending
- **Risk-adjusted optimization** — budget allocation that accounts for diminishing returns and carryover

→ [Why Simba?](../../sales/why-simba.md)

### Who is Simba for?

Simba is built for:
- **Brand marketers** who need to measure and optimize marketing ROI
- **Marketing agencies** managing multiple client accounts and brands
- **Data and analytics teams** who want rigorous statistical modeling without the coding overhead
- **CMOs and marketing leaders** who need transparent, defensible measurement

→ [Use Cases](../use-cases/README.md)

## Getting Started

### Do I need coding or statistics experience?

No. Simba's interface lets you configure Bayesian models, set priors, and run optimizations without writing any code. **Smart defaults** and an **Data Validator** guide you through the process, so you can build reliable models even if you're new to marketing science.

For teams that want deeper statistical control, the platform exposes all model parameters for fine-tuning.

→ [Quick Start Guide](../getting-started/quick-start-guide.md)

### What data do I need to get started?

At minimum, you need:
- A **target KPI** time series (e.g., weekly revenue or conversions)
- **Media spend or activity data** for each channel you want to measure
- At least **1 year of weekly data** (2+ years recommended)

→ [Data Requirements](../data/data-requirements.md)

### Can I try Simba before committing?

Yes — Simba offers a **28-day free trial** where you can explore the full platform with your own data. The trial includes 10 saved models, 10 optimizations, and 10 scenarios.

→ [Start Free Trial](https://getsimba.ai)

## Platform & Technical

### What is Bayesian modeling and why does it matter?

Bayesian modeling is a statistical approach that combines observed data with prior knowledge to produce probability distributions over possible outcomes — rather than single-point estimates. This means you get:

- **Uncertainty quantification** — know how confident you should be in each result
- **Domain knowledge integration** — encode what you know about your business into the model
- **Better performance with limited data** — priors help stabilize estimates when data is sparse

→ [Bayesian Modeling Explained](../core-concepts/bayesian-modeling.md)

### What is PyMC-Marketing?

PyMC-Marketing is the leading open-source library for Bayesian marketing analytics. Simba is built on top of PyMC-Marketing, which means:

- The modeling methodology is **open-source and peer-reviewed**
- You benefit from **continuous community improvements**
- There's **no vendor lock-in** — your modeling logic is built on open foundations
- Full **scientific rigor** backed by decades of Bayesian statistics research

→ [PyMC-Marketing & Simba](../../resources/pymc-marketing.md)

### How does the Data Validator work?

The Data Auditor is an intelligent agent that runs automatically when you upload data. It validates your data structure, detects anomalies and missing values, checks schema integrity, and assigns a **Data Health Score** (0–100%) so you know exactly how reliable your inputs are before modeling.

→ [Data Auditor Guide](../platform-guide/data-auditor.md)

### What channels does Simba support?

Simba can model any marketing channel where you have time-series data: TV, digital display, paid social, paid search, OOH, video, audio/radio, email, print, and affiliate marketing.

→ [Supported Channels](../data/supported-channels.md)

## Security & Privacy

### How secure is my marketing data?

Simba is **Cyber Essentials certified** and fully **GDPR compliant**. Your data is:

- Encrypted at rest with **AES-256**
- Encrypted in transit with **TLS 1.3**
- Stored in **isolated AWS S3 buckets** (not shared with other customers)
- Protected by **zero-retention logging** and strict data minimization

→ [Security Overview](../security/README.md)

### Is Simba GDPR compliant?

Yes. Simba is fully compliant with GDPR and the UK Data Protection Act. We practice strict data minimization, provide full data subject rights (access, rectification, erasure, portability), and use Standard Contractual Clauses for any international data transfers.

→ [Compliance Details](../security/compliance.md)

### Where is my data stored?

Data is stored in secure AWS infrastructure with per-customer isolation. Enterprise customers can discuss dedicated hosting arrangements for specific data residency requirements.

→ [Data Sovereignty](../security/data-sovereignty.md)

## Pricing & Plans

### What plans are available?

Simba currently offers **Enterprise** (full platform with dedicated support) and **Managed** (done-for-you modeling by PhD statisticians). Self-service tiers for individual analysts and smaller teams are coming soon.

→ [Pricing & Plans](../pricing/README.md)

### Is there a free trial?

Yes — a 28-day free trial with full platform access, 10 saved models, 10 optimizations, and 10 scenarios. No setup fees.

### Can I cancel anytime?

Yes. All plans can be cancelled at any time with no cancellation fees.

## Support

### How do I get help?

- **Documentation**: Browse this repository for guides and tutorials
- **GitHub Issues**: [Report a bug](../../../issues/new?template=bug_report.yml) or [ask a question](../../../issues/new?template=support_question.yml)
- **Email**: support@simba-mmm.com
- **Website**: [getsimba.ai](https://getsimba.ai)

---

*Can't find what you're looking for? [Ask us a question](../../../issues/new?template=support_question.yml) or email support@simba-mmm.com.*
