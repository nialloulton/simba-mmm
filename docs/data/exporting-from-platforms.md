# Exporting Data from Ad Platforms

Simba needs time-series marketing data in CSV format. This guide covers how to export the right data from common advertising platforms and prepare it for upload.

For the target format, see [Data Requirements](./data-requirements.md). For cleaning and formatting, see [Data Preparation](./data-preparation.md).

---

## General Principles

Regardless of platform, you need:

- **Weekly or daily granularity** — one row per time period per channel
- **Consistent date ranges** — all channels should cover the same time period
- **Spend and/or impressions** — at minimum, the amount spent per period
- **Campaign-level or channel-level aggregation** — Simba models at the channel level, not the individual ad level

> **Tip:** Export at least 2 years (104 weeks) of data when possible. More data gives the model more signal to separate [seasonality](../core-concepts/seasonality.md) from media effects.

---

## Google Ads

**What to export:** Campaign-level spend and impressions, aggregated weekly.

1. Go to **Google Ads → Reports → Predefined Reports → Basic → Campaign**
2. Set the date range to cover your full modeling period (2+ years ideal)
3. Add columns: **Campaign**, **Cost**, **Impressions**, **Clicks** (optional)
4. Set segmentation to **Week** (not day, unless you want daily granularity)
5. Download as CSV

**What to use in Simba:**
- Use **Cost** as your spend column (e.g., `google_ads_spend`)
- Or use **Impressions** if you prefer impression-based modeling
- Aggregate campaigns into a single `google_ads_spend` column unless you want to model campaigns separately (e.g., branded vs. generic search)

**Watch out for:**
- Google Ads reports cost in your account currency — ensure it matches your revenue currency
- If you have multiple accounts, export and combine them
- Exclude DSA (Dynamic Search Ads) or Shopping campaigns if you want to model them separately

---

## Meta Ads Manager (Facebook / Instagram)

**What to export:** Ad set or campaign-level spend and impressions, aggregated weekly.

1. Go to **Ads Manager → Campaigns**
2. Set the date range to your full modeling period
3. Click **Reports → Export Table Data**
4. Select columns: **Campaign Name**, **Amount Spent**, **Impressions**, **Reach** (optional)
5. Set breakdown to **Time → Week**
6. Export as CSV

**What to use in Simba:**
- Use **Amount Spent** as your spend column (e.g., `facebook_spend` or `meta_spend`)
- Or use **Impressions** for impression-based modeling
- Combine Facebook and Instagram into one column, or keep them separate if you want separate attribution

**Watch out for:**
- Meta reports spend in the ad account's currency — check it matches your revenue data
- "Amount Spent" includes all campaign types — filter out non-media campaigns (e.g., lead gen forms) if they don't contribute to your KPI

---

## Google Analytics 4 (GA4)

GA4 is typically used for the **revenue / KPI column**, not for media spend.

**What to export:** Weekly revenue or conversions.

1. Go to **GA4 → Explore → Free Form** (or use the API / BigQuery export)
2. Set dimensions: **Date** (week granularity)
3. Set metrics: **Purchase Revenue**, **Transactions**, or your key conversion metric
4. Set the date range to match your media data
5. Export as CSV

**What to use in Simba:**
- Use **Purchase Revenue** as your `revenue` column (target KPI)
- Or use transaction count / conversion count if revenue is not available

**Watch out for:**
- GA4 revenue is based on web/app tracking — it may not capture all sales channels (e.g., in-store, phone orders). If you have a separate sales system, use that for total revenue instead.
- GA4 attribution models may pre-allocate revenue to channels — Simba needs **total** revenue, not channel-attributed revenue

---

## TikTok Ads

**What to export:** Campaign-level spend, aggregated weekly.

1. Go to **TikTok Ads Manager → Campaign**
2. Set the date range and select **Weekly** view
3. Export columns: **Campaign Name**, **Cost**, **Impressions**
4. Download as CSV

Use **Cost** as `tiktok_spend` in Simba.

---

## DV360 / Google Campaign Manager

**What to export:** Insertion order or line item-level spend and impressions.

1. In **DV360 → Reports**, create a custom report
2. Dimensions: **Date** (week), **Insertion Order** or **Line Item**
3. Metrics: **Revenue (Media Cost)**, **Impressions**
4. Set the date range and export as CSV

Aggregate to a single `display_spend` or `programmatic_spend` column for Simba, or split by channel type (display, video, native).

---

## TV (Linear and Connected)

TV data typically comes from your media agency or buying platform, not from a self-serve export.

**What you need:**
- **Weekly GRPs** (Gross Rating Points) — the standard TV activity metric
- Or **weekly spend** if GRPs are not available
- Broken out by **network type** if you want separate channels (e.g., `linear_tv_spend`, `ctv_spend`)

**Common sources:**
- Nielsen / Comscore reports (for GRPs)
- Your media agency's reporting (for spend and GRPs)
- Connected TV platforms (Roku, Hulu, YouTube TV) for CTV-specific data

**Watch out for:**
- TV data is often reported on a different calendar (broadcast weeks) — align to the same week definition as your other data
- GRPs and spend measure different things — use GRPs if available, as they better reflect actual media delivery

---

## Out-of-Home (OOH) and Audio

OOH and audio data typically come from your media agency.

**What you need:**
- **Weekly spend** or **weekly impressions/impacts**
- For OOH: face count, panel count, or estimated impressions
- For audio (radio, podcasts, Spotify): impressions or spend

These channels typically have longer [adstock](../core-concepts/adstock-effects.md) decay — Simba's Smart Defaults account for this.

---

## Combining Everything into One CSV

Once you have exports from each platform:

1. **Align date ranges** — all channels must cover the same time period
2. **Aggregate to the same granularity** — weekly (recommended) or daily
3. **Use one row per date** — each row has the date, revenue, and all channel spend columns
4. **Fill missing periods with 0** — if a channel was inactive for a week, enter 0 (not blank)
5. **Save as CSV** with UTF-8 encoding

Your final CSV should look like:

| date | revenue | tv_spend | facebook_spend | google_ads_spend | ... |
|------|---------|----------|----------------|------------------|-----|
| 2022-01-03 | 185000 | 45000 | 22000 | 35000 | ... |
| 2022-01-10 | 192000 | 48000 | 21000 | 33000 | ... |

See [Data Requirements](./data-requirements.md) for the full specification and [Data Preparation](./data-preparation.md) for cleaning steps.

---

## Next Steps

- [Data Requirements](./data-requirements.md) — column types, date formats, variable classification
- [Data Preparation](./data-preparation.md) — cleaning, missing values, unit alignment
- [Data Validation](./data-validation.md) — what the Data Validator checks
- [Your First Model](../getting-started/first-model-tutorial.md) — build a model with sample data
