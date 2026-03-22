# Supported Channels — Media Types You Can Model in Simba

Simba supports a wide range of media channels and marketing activities in your marketing mix model. This guide covers all supported channel types, recommended metrics for each, and tips for getting the best results.

## Overview

Simba can model any marketing channel where you have time-series data on spend or activity. The platform's Bayesian framework automatically handles the unique characteristics of each channel — including different saturation rates, decay patterns, and response curves.

## Channel Categories

### Television (TV)

TV remains one of the most impactful (and expensive) media channels. Simba handles both linear and connected TV.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| GRPs | Gross Rating Points | Best for traditional TV |
| Spend | Total media cost | Universal fallback |
| TRPs | Target Rating Points | For targeted buys |
| Impressions | Delivered impressions | For connected/streaming TV |

**Typical characteristics**: High saturation potential, longer decay (ads remembered for weeks), significant carryover effects.

### Digital / Online Display

Programmatic display, native ads, and banner advertising.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Impressions | Ad impressions served | Recommended |
| Spend | Media cost | Good alternative |
| Clicks | Click-throughs | Supplementary |
| Viewable impressions | MRC-viewable impressions | Premium metric |

**Typical characteristics**: Moderate saturation, shorter decay than TV, highly measurable.

### Paid Social

Social media advertising across platforms.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Impressions | Total impressions | Recommended |
| Spend | Media cost | Good alternative |
| Reach | Unique users reached | For awareness campaigns |
| Engagements | Likes, shares, comments | Supplementary |

**Platforms**: Facebook/Meta, Instagram, TikTok, LinkedIn, X (Twitter), Pinterest, Snapchat

**Tip**: Break out platforms individually rather than combining into one "Social" variable. This gives you per-platform ROI and optimization insights.

### Paid Search (SEM)

Search engine marketing including branded and non-branded search.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Spend | Media cost | Recommended |
| Clicks | Search ad clicks | Good alternative |
| Impressions | Search ad impressions | Supplementary |

**Tip**: Separate branded search from non-branded. Branded search often captures existing demand rather than creating it.

### Out-of-Home (OOH)

Billboards, transit ads, street furniture, and digital OOH.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Spend | Media cost | Recommended |
| Impressions | Estimated impressions | Good alternative |
| Panels/Faces | Number of active placements | Supplementary |

**Typical characteristics**: Long decay, high geographic variation, harder to measure precisely.

### Video / YouTube

Online video advertising including pre-roll, mid-roll, and bumper ads.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Impressions | Video ad impressions | Recommended |
| Spend | Media cost | Good alternative |
| Completed views | Full video views | Premium metric |

### Audio / Podcasts / Radio

Audio advertising across radio, streaming, and podcasts.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Spend | Media cost | Recommended |
| Impressions | Estimated listens/impressions | Good alternative |
| GRPs | For traditional radio | Industry standard |

### Email Marketing

Direct email campaigns and newsletters.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Sends | Emails sent | Recommended |
| Opens | Email opens | Supplementary |
| Clicks | Email click-throughs | Supplementary |

### Print

Magazine and newspaper advertising.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Spend | Media cost | Recommended |
| Insertions | Number of ad placements | Good alternative |
| Circulation | Publication circulation | Supplementary |

### Affiliate / Partnerships

Performance-based partnerships and affiliate marketing.

| Metric | Description | Recommended |
|--------|-------------|-------------|
| Spend/Commission | Total cost | Recommended |
| Clicks | Referral clicks | Good alternative |

## Non-Media Variables

In addition to media channels, include these control variables for better model accuracy:

| Variable | Examples |
|----------|----------|
| **Pricing** | Price index, discount depth, promotional flags |
| **Distribution** | Store count, availability score |
| **Seasonality** | Holiday flags, season indicators |
| **Competition** | Competitor spend, share of voice |
| **Economic** | Consumer confidence, unemployment rate |
| **Weather** | Temperature, precipitation |
| **Events** | Major events, cultural moments |

## Best Practices

1. **Use the most granular channel breakdowns available** — "Meta Impressions" is more useful than "Social Spend"
2. **Be consistent** — use the same metric type (spend or impressions) for channels of the same type where possible
3. **Include zero-spend periods** — these help the model isolate the impact of active spend
4. **Don't combine dissimilar channels** — TV and digital have very different decay and saturation characteristics
5. **Include at least 3 channels** — models with more channels produce richer attribution insights

→ **Next**: [Data Requirements](data-requirements.md) | [Model Configuration](../platform-guide/model-configuration.md)

---

*See also: [Data Preparation](data-preparation.md) | [Saturation Curves](../core-concepts/saturation-curves.md) | [Adstock Effects](../core-concepts/adstock-effects.md)*
