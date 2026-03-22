# Smart Defaults --- Auto-Generated Model Starting Points

Smart Defaults are Simba's automatically generated prior configurations for each channel in your model. They provide a data-informed starting point so you can run a model without manually setting every parameter, while still producing reasonable results.

## What Smart Defaults Are

When you load data into Simba and proceed to [Model Configuration](./model-configuration.md), the platform auto-generates a complete set of priors for every channel variable: distribution type, mean, saturation, and decay. These are the smart defaults.

They are not arbitrary starting values. Each default is computed from a combination of:

- **Your historical data**: Spend levels, variance, response patterns, and time series characteristics specific to your dataset.
- **Industry benchmarks**: Aggregated, anonymized patterns from similar channels and verticals that inform reasonable ranges for saturation and decay when your data alone is insufficient.

Smart defaults aim to be close enough to the true values that the Bayesian model converges quickly and produces reliable results, while remaining broad enough that the data can pull the posterior away from the prior if the evidence is strong.

## How They Are Generated

The auto-generation process runs during the [Data Validator](./data-auditor.md) step and is refined when you enter the model configuration screen. The process involves:

1. **Spend analysis**: The system examines each channel's spend distribution --- its mean, variance, range, and temporal pattern. Channels with high variance relative to their mean are easier to measure, which influences the prior width.

2. **Response curve estimation**: A lightweight preliminary fit estimates approximate saturation and decay parameters for each channel. These rough estimates seed the smart defaults.

3. **Industry benchmark matching**: The channel name and data characteristics are matched against benchmark tables that encode typical parameter ranges for common media types (TV, paid search, paid social, display, OOH, radio, print, and others). If your channel data is sparse, benchmarks carry more weight; if your data is rich, your data dominates.

4. **Distribution selection**: The system selects a distribution type (typically InverseGamma) and sets the concentration parameter so the prior is informative but not overly restrictive. The goal is a prior that rules out implausible values (negative effects, impossibly large effects) without forcing the model to a specific answer.

The result is a fully populated configuration grid that you can use as-is or modify.

## When to Use Defaults vs Custom Configuration

**Use defaults when:**

- You are running your first model and do not yet have strong priors from experiments or domain expertise.
- Your data has good coverage: at least 52 weeks of data with meaningful spend variation across channels.
- You want to establish a baseline model quickly before iterating on configuration.
- The channel mix is standard (common digital and traditional channels) and likely to match industry benchmarks well.

**Switch to custom configuration when:**

- You have lift test results or experimental evidence that should inform specific channels. See [Model Configuration](./model-configuration.md) for how to translate lift test results into prior settings.
- A channel is new or unusual and does not match standard benchmarks (for example, a podcast sponsorship, influencer partnership, or niche platform).
- The model's posterior distributions are very close to the priors, suggesting the data is not strong enough to update the defaults. In this case, the defaults are effectively becoming your answer, so they need to be set with care.
- You are modeling a market or category with dynamics that differ significantly from typical benchmarks (for example, luxury goods with very long purchase cycles, or fast-moving consumer goods with extremely short cycles).

## Fine-Tuning with Domain Expertise

Smart defaults and domain expertise are complementary. The recommended approach is:

1. **Start with defaults.** Run the model and review the results.
2. **Identify channels where results conflict with your knowledge.** If the model attributes very high lift to a channel you believe is ineffective (or vice versa), check whether the prior is too loose or too tight for that channel.
3. **Adjust selectively.** Override only the channels where you have strong reason to believe the default is wrong. Leave the rest at their default values.
4. **Re-run and compare.** After adjusting, re-run the model and compare the new results to the baseline. If the adjusted model produces better fit diagnostics and more plausible attribution, keep the changes. If not, revert.

Avoid the temptation to override every channel simultaneously. Each change interacts with the others, and making many changes at once makes it difficult to understand what improved (or worsened) the results.

## Auto-Generate Workflow

The end-to-end workflow for using smart defaults:

1. **Upload data** and run the [Data Validator](./data-auditor.md) to validate quality.
2. **Enter the model configuration screen.** Smart defaults are pre-populated in the configuration grid.
3. **Review the defaults.** Check that the distribution types, means, saturation, and decay values look reasonable given what you know about your channels.
4. **Run the model.** The model uses the defaults as priors and updates them with your data to produce posterior estimates.
5. **Evaluate results.** Review [Incremental Measurement](./measurement.md) outputs. If results are plausible and model fit is good, proceed to [Scenario Planning](./scenario-planning.md) and [Budget Optimization](./budget-optimization.md).
6. **Iterate if needed.** If results are implausible or fit is poor, return to configuration, adjust specific channels, and re-run.

Smart defaults are designed to make step 3 fast and step 6 rare. For most datasets with adequate coverage, the defaults produce a credible first model without manual intervention.
