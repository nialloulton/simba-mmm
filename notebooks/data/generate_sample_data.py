"""Generate synthetic marketing datasets for the notebook series."""
import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)

# --- Single-brand weekly dataset (104 weeks) ---
n_weeks = 104
dates = pd.date_range("2023-01-02", periods=n_weeks, freq="W-MON")

# Media spend (realistic weekly budgets)
tv_spend = np.random.lognormal(mean=10.5, sigma=0.4, size=n_weeks).clip(5000, 150000)
facebook_spend = np.random.lognormal(mean=9.5, sigma=0.5, size=n_weeks).clip(2000, 80000)
google_spend = np.random.lognormal(mean=9.8, sigma=0.3, size=n_weeks).clip(3000, 100000)
radio_spend = np.random.lognormal(mean=8.5, sigma=0.6, size=n_weeks).clip(500, 30000)
print_spend = np.random.lognormal(mean=8.0, sigma=0.7, size=n_weeks).clip(0, 20000)

# Some weeks have zero spend for certain channels
tv_spend[np.random.random(n_weeks) < 0.15] = 0
radio_spend[np.random.random(n_weeks) < 0.3] = 0
print_spend[np.random.random(n_weeks) < 0.4] = 0

# Simple adstock function for data generation
def geometric_adstock(x, alpha=0.7, l_max=8):
    weights = alpha ** np.arange(l_max)
    result = np.convolve(x, weights)[:len(x)]
    return result

# Apply adstock to get "effective" media
tv_effect = geometric_adstock(tv_spend, alpha=0.85, l_max=12) * 0.00015
fb_effect = geometric_adstock(facebook_spend, alpha=0.4, l_max=4) * 0.00025
google_effect = geometric_adstock(google_spend, alpha=0.3, l_max=3) * 0.00030
radio_effect = geometric_adstock(radio_spend, alpha=0.6, l_max=6) * 0.00012
print_effect = geometric_adstock(print_spend, alpha=0.7, l_max=8) * 0.00008

# Apply saturation
def tanh_saturation(x, alpha=1.0):
    scalar = x.max() if x.max() > 0 else 1.0
    return np.tanh(x / (scalar * alpha))

tv_saturated = tanh_saturation(tv_effect, alpha=1.5) * 85000
fb_saturated = tanh_saturation(fb_effect, alpha=1.2) * 45000
google_saturated = tanh_saturation(google_effect, alpha=1.0) * 55000
radio_saturated = tanh_saturation(radio_effect, alpha=1.8) * 15000
print_saturated = tanh_saturation(print_effect, alpha=2.0) * 8000

# Seasonality (annual)
week_idx = np.arange(n_weeks)
seasonality = (15000 * np.sin(2 * np.pi * week_idx / 52)
              + 8000 * np.cos(4 * np.pi * week_idx / 52))

# Trend
trend = 2000 * week_idx / n_weeks

# Base sales
base = 350000

# Events / holidays (Black Friday, Christmas, Easter)
events = np.zeros(n_weeks)
# Black Friday weeks (late November)
for yr_offset in [0, 1]:
    bf_week = 47 + yr_offset * 52
    if bf_week < n_weeks:
        events[bf_week] = 80000
        if bf_week + 1 < n_weeks:
            events[bf_week + 1] = 40000
# Christmas
for yr_offset in [0, 1]:
    xmas_week = 51 + yr_offset * 52
    if xmas_week < n_weeks:
        events[xmas_week] = 60000

# Control variables
temperature = 15 + 10 * np.sin(2 * np.pi * (week_idx - 10) / 52) + np.random.normal(0, 2, n_weeks)
competitor_spend = np.random.lognormal(mean=10.0, sigma=0.3, size=n_weeks)

# Revenue
revenue = (base + trend + seasonality + events
          + tv_saturated + fb_saturated + google_saturated
          + radio_saturated + print_saturated
          - competitor_spend * 0.002
          + temperature * 500
          + np.random.normal(0, 12000, n_weeks))

revenue = revenue.clip(min=100000)

df = pd.DataFrame({
    "date": dates,
    "revenue": np.round(revenue, 2),
    "tv_spend": np.round(tv_spend, 2),
    "facebook_spend": np.round(facebook_spend, 2),
    "google_search_spend": np.round(google_spend, 2),
    "radio_spend": np.round(radio_spend, 2),
    "print_spend": np.round(print_spend, 2),
    "competitor_spend": np.round(competitor_spend, 2),
    "temperature": np.round(temperature, 1),
    "black_friday": (events > 50000).astype(int),
    "christmas": ((events > 0) & (events <= 60000) & (week_idx % 52 >= 50)).astype(int),
})
df.to_csv(Path(__file__).parent / "sample_mmm_weekly.csv", index=False)
print(f"Created sample_mmm_weekly.csv: {df.shape}")

# --- Multi-brand dataset ---
brands = ["BrandA", "BrandB", "BrandC"]
n_weeks_mb = 78  # 18 months

rows = []
for brand in brands:
    dates_mb = pd.date_range("2023-06-05", periods=n_weeks_mb, freq="W-MON")
    base_rev = {"BrandA": 500000, "BrandB": 300000, "BrandC": 180000}[brand]
    scale = base_rev / 500000

    for i, d in enumerate(dates_mb):
        tv = np.random.lognormal(10.0, 0.5) * scale if np.random.random() > 0.2 else 0
        digital = np.random.lognormal(9.5, 0.4) * scale
        social = np.random.lognormal(9.0, 0.5) * scale
        seas = 10000 * scale * np.sin(2 * np.pi * i / 52)
        rev = base_rev + seas + tv * 0.4 + digital * 0.6 + social * 0.3 + np.random.normal(0, 8000 * scale)
        rows.append({
            "date": d, "brand": brand,
            "revenue": round(max(rev, 50000), 2),
            "tv_spend": round(tv, 2),
            "digital_spend": round(digital, 2),
            "social_spend": round(social, 2),
        })

df_mb = pd.DataFrame(rows)
df_mb.to_csv(Path(__file__).parent / "sample_multi_brand.csv", index=False)
print(f"Created sample_multi_brand.csv: {df_mb.shape}")
