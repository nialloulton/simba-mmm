# Smart Defaults --- Auto-Generated Model Starting Points

Smart Defaults are Simba's automatically generated prior configurations for each channel in your model. They provide a data-informed starting point so you can run a model without manually setting every parameter, while still producing reasonable results.

## What Smart Defaults Are

When you enter the [Model Configuration](./model-configuration.md) screen and open the Prior Builder, Simba can auto-generate a complete set of priors for every media and control variable: distribution type, coefficient mean and sigma, decay ranges, effect period, and saturation scalar. These are the smart defaults.

They are not arbitrary starting values. Each default is computed from a combination of:

- **Your historical data**: Spend levels, cost shares, channel activation patterns, and average impression/GRP values specific to your dataset.
- **Industry benchmarks**: Research-based estimates of total media effect for your industry vertical (e.g., FMCG channels typically drive around 6% of total KPI, while E-Commerce channels can drive over 20%).
- **Semantic channel detection**: Automatic recognition of channel types from variable names to set appropriate adstock decay ranges.

Smart defaults aim to be close enough to the true values that the Bayesian model converges quickly and produces reliable results, while remaining broad enough that the data can pull the posterior away from the prior if the evidence is strong.

## How They Are Generated

The smart default computation runs when you click the smart defaults button in the Prior Builder on the model configuration screen. The process involves several steps:

### 1. Cost Share Analysis

The system calculates each channel's share of total media spend. For example, if TV accounts for 40% of total spend and paid search for 15%, those cost shares drive how the total expected media effect is allocated across channels. Channels with higher spend shares receive proportionally larger prior coefficients.

### 2. Industry Benchmark Allocation

You select your industry from the benchmark selector (FMCG, Retail, TelCo, Financial Services, E-Commerce, or Other). Each industry has a calibrated estimate of total media effect --- the percentage of the dependent variable that all media channels collectively drive. This total effect is then distributed to individual channels proportional to their cost share.

The available industry benchmarks are:

| Industry | Expected Total Media Effect |
|---|---|
| FMCG | ~6% |
| Retail | ~9% |
| TelCo | ~30% |
| Financial Services | ~19% |
| E-Commerce | ~22% |
| Other | ~12% |

### 3. Dynamic Saturation Parameter Calculation

For each channel, the system computes a saturation shape parameter (alpha) based on:

- **Spend deviation**: How the channel's cost share compares to the average across all channels. Higher-share channels get slightly different saturation assumptions.
- **Spend variability**: The standard deviation of spend relative to total spend, which adjusts the saturation curve shape.
- **Activation frequency**: The proportion of time periods where the channel had non-zero spend. Channels that are "always on" get tighter saturation priors; intermittently active channels get slightly wider uncertainty.

The coefficient is then adjusted for the saturation curve using a tanh-based formula that accounts for the relationship between average and maximum spend levels.

### 4. Semantic Channel Type Detection

Simba parses variable names to detect channel types using a comprehensive ontology covering 15 channel categories: TV, Digital, Social, Search, Video, Radio, Print, OOH, Email, Influencer, Affiliate, Direct, Mobile, Cinema, and Sponsorship. Each channel type has a calibrated decay range reflecting its typical carryover characteristics:

- **Fast decay** (e.g., Social, Mobile, Email): Effects dissipate within 1-2 weeks.
- **Medium decay** (e.g., Digital, Video, Search): Effects carry over for 3-4 weeks.
- **Slow decay** (e.g., TV, Print, OOH, Sponsorship): Effects persist for 6-10 weeks.

### 5. Saturation Scalar Auto-Fill

Each channel's saturation scalar is set to the average value of that channel's data across all time periods. This anchors the saturation curve at a realistic operating point.

### 6. Control Variable Detection

For control variables, Simba uses semantic matching to detect common types and apply appropriate priors:

- **Price variables**: Detected by keywords like "price", "pricing", or "discount". Assigned a TruncatedNormal distribution constrained to negative values (price increases typically reduce sales).
- **Promotion variables**: Detected by keywords like "promo", "campaign", or "voucher". Assigned an InverseGamma distribution with positive mean (promotions typically increase sales).
- **Distribution variables**: Detected by keywords like "distribution", "availability", or "coverage". Assigned an InverseGamma distribution with positive mean.

### 7. Special Channel Handling

- **Halo channels**: Channels flagged as halo (brand awareness / cross-brand effects) receive fixed small coefficients rather than cost-share-based priors, with higher uncertainty.
- **Trademark channels**: Channels flagged as trademark or portfolio-level campaigns receive 25% of the calculated coefficient, reflecting that their effect is shared across brands.

### 8. Distribution Selection

All media channels use the **InverseGamma** distribution by default, which naturally constrains coefficients to positive values (media should have a positive effect on the KPI). The sigma is set to twice the mu value based on the industry benchmark, providing an informative but not overly restrictive prior.

## When to Use Defaults vs Custom Configuration

**Use defaults when:**

- You are running your first model and do not yet have strong priors from experiments or domain expertise.
- Your data has good coverage with meaningful spend variation across channels.
- You want to establish a baseline model quickly before iterating on configuration.
- The channel mix is standard (common digital and traditional channels) and likely to match the semantic channel detection well.

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

1. **Upload data** and optionally run the [Data Validator](./data-auditor.md) to check quality.
2. **Enter the model configuration screen.** Open the Prior Builder.
3. **Select your industry** from the benchmark selector to set the expected total media effect.
4. **Click the smart defaults button.** Priors are computed and populated in the configuration grid.
5. **Review the defaults.** Check that the distribution types, means, decay ranges, and saturation scalars look reasonable given what you know about your channels.
6. **Build the model.** The model uses the defaults as priors and updates them with your data to produce posterior estimates.
7. **Evaluate results.** Review [Incremental Measurement](./measurement.md) outputs. If results are plausible and model fit is good, proceed to [Scenario Planning](./scenario-planning.md) and [Budget Optimization](./budget-optimization.md).
8. **Iterate if needed.** If results are implausible or fit is poor, return to configuration, adjust specific channels, and re-run.

Smart defaults are designed to make step 5 fast and step 8 rare. For most datasets with adequate coverage, the defaults produce a credible first model without manual intervention.
