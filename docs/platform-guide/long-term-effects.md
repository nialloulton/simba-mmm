# Long-Term Effects --- Modeling Lasting Brand Impact

Standard Marketing Mix Models measure short-term media impact: the incremental revenue generated within a few weeks of spend. But some marketing activities --- brand campaigns, sponsorships, sustained awareness efforts --- produce effects that persist for months or longer. The Long-Term Effects module captures this extended impact.

> **Availability**: Long-Term Effects is available on the **Pro tier and above**.

## What Long-Term Effects Are

Marketing impact operates on two timescales:

- **Short-term (performance)**: A paid search ad drives a click and a purchase this week. A promotional email generates orders within days. These effects are captured by the standard adstock decay parameters in [Model Configuration](./model-configuration.md).
- **Long-term (brand building)**: A TV brand campaign gradually shifts consumer perception, making them more likely to purchase in future months. A sponsorship increases unaided awareness that compounds over quarters. These effects extend well beyond the standard adstock window and are not captured by short-term decay parameters alone.

The Long-Term Effects module adds a second, slower-decaying component to the model for channels where brand-building impact is expected. This lets Simba attribute revenue to both the immediate performance effect and the lasting brand equity contribution of each channel.

## How Simba Captures Long-Term Impact

The standard Simba model applies a single adstock transformation per channel, with a decay rate typically between 0.1 and 0.7 (effects lasting days to a few weeks). The Long-Term Effects module extends this by adding:

1. **A dual-component response function**: Each eligible channel gets two response pathways --- a short-term component (standard adstock) and a long-term component (slow decay over weeks to months). The model estimates the relative contribution of each pathway.

2. **Separate saturation curves**: The short-term and long-term components can have different saturation characteristics. Performance channels may saturate quickly in the short term but continue building brand equity at higher spend levels.

3. **Stock variable for brand equity**: The model maintains a latent brand equity variable that accumulates from brand-building spend and decays slowly over time. This stock variable influences base sales, capturing the mechanism by which sustained marketing investment lifts the revenue baseline.

The result is a more complete picture of each channel's total contribution --- not just what it delivered this quarter, but how it is building (or eroding) the foundation for future revenue.

## Behavioral Response Modeling

Long-term effects are grounded in how consumers actually respond to marketing over time:

- **Memory formation and retrieval**: Advertising creates memory traces that influence future purchase decisions. Repeated exposure strengthens these traces. The model captures this through the accumulating brand equity stock.
- **Consideration set dynamics**: Sustained marketing keeps a brand in the consumer's consideration set. Reducing spend allows competitors to displace the brand. The long-term component models the gradual entry and exit from consideration.
- **Habit formation**: For repeat-purchase categories, marketing can shift habitual buying behavior over time. Once a habit forms, it persists even after marketing is reduced --- but only up to a point. The decay rate of the long-term component captures how quickly habits erode without reinforcement.

## Memory Decay Curves and Seasonal Patterns

The Long-Term Effects module estimates a **memory decay curve** for each channel's brand-building component. This curve describes how quickly the accumulated brand impact fades after spend is reduced or stopped.

- **Fast memory decay** (half-life of 4--8 weeks): Typical for digital brand campaigns, online video, and social media awareness efforts. These channels need sustained investment to maintain their long-term contribution.
- **Slow memory decay** (half-life of 3--6 months): Typical for TV brand campaigns, major sponsorships, and out-of-home advertising. These channels build durable brand equity that persists for months after the campaign ends.

**Seasonal patterns** are handled automatically. The model separates seasonal demand fluctuations from long-term brand effects, so a holiday sales spike is attributed to seasonality rather than falsely inflating the brand equity estimate. Similarly, seasonal campaigns (back-to-school, summer) are decomposed into their immediate performance contribution and any lasting brand residue.

## Interpreting Long-Term vs Short-Term Results

When the Long-Term Effects module is active, the [Incremental Measurement](./measurement.md) results page adds new dimensions:

### Revenue Decomposition

The decomposition now shows three layers instead of two:

- **Base sales**: Organic demand unrelated to current or past marketing (as before).
- **Short-term media lift**: Incremental revenue driven by recent marketing activity within the standard adstock window.
- **Long-term media lift**: Incremental revenue attributable to accumulated brand equity from past marketing investment.

### Channel-Level Breakdown

For each channel, you see:

- **Short-term contribution**: Revenue generated within the standard decay window. This is the same metric as the standard model.
- **Long-term contribution**: Revenue generated through the brand equity pathway. This may be attributed to spend that occurred weeks or months ago.
- **Total contribution**: The sum of short-term and long-term effects. This is the channel's complete impact.

Some channels may show a small short-term effect but a large long-term effect (brand-building channels), while others may show the opposite (performance channels). This distinction is critical for budget decisions: cutting a channel with strong long-term effects saves money immediately but erodes future revenue over the following months.

### Implications for Budget Optimization

When Long-Term Effects is active, the [Budget Optimization](./budget-optimization.md) module incorporates brand equity dynamics into its recommendations:

- Channels with strong long-term effects receive higher recommended spend than a short-term-only model would suggest, because their full return is realized over a longer horizon.
- The optimizer may recommend maintaining baseline spend on brand-building channels even when short-term ROI appears low, because the long-term brand equity contribution justifies the investment.
- Scenario comparisons in [Scenario Planning](./scenario-planning.md) show both the immediate revenue impact and the projected brand equity trajectory under each scenario, allowing you to evaluate short-term revenue against long-term brand health.

Understanding the balance between short-term performance and long-term brand building is essential for sustainable marketing investment. The Long-Term Effects module makes this balance visible and quantifiable rather than leaving it to intuition.
