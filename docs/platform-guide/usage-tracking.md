# Usage Tracking --- Understanding Plan Limits and Usage

Simba tracks usage of key platform actions against your plan's monthly limits. Understanding how usage is tracked helps you plan your modeling activities and avoid hitting limits at critical moments.

---

## What Is Tracked

Simba meters the following actions:

| Resource | Description |
|---|---|
| **Saved models** | Total number of completed models retained in your workspace (not per-period). |
| **Model fits** | Each new model fitting run. Counts toward your per-period allocation. |
| **Optimizations** | Each budget optimization run (single-brand or portfolio). |
| **Scenarios** | Each scenario planning simulation. |
| **Refits** | Re-running an existing model with updated data or configuration. Counted separately from new model fits. |
| **VAR models** | VAR model creation counts toward model fit limits. VAR availability is tier-dependent. |
| **Portfolios** | Total number of portfolios (not per-period). |

---

## Limits

Usage limits vary by plan. Enterprise and Managed plans have full access across all features. The free trial provides generous limits for evaluation. Self-service tiers with specific usage limits are coming soon --- see [Pricing](../pricing/README.md) for updates.

---

## Billing Periods

Usage counters for per-period resources (model fits, optimizations, scenarios, refits) reset at the start of each billing period. Your billing period aligns with your subscription start date.

---

## Trial Details

### 28-Day Free Trial

Every new account starts with a 28-day trial that includes generous limits:

- 10 saved models, 10 model fits, 10 optimizations, 10 scenarios.
- VAR models are enabled.
- Full platform access including Data Validator and Smart Defaults.
- No credit card required.

### 3-Day Grace Period

When your 28-day trial expires, you enter a **3-day grace period**:

- You can **view** existing models and results.
- You **cannot** create new models, run optimizations, or execute scenarios.
- All data and model configurations are preserved.

After the grace period, upgrade to a paid plan to restore full access. Your data and models are retained.

---

## Checking Your Usage

To view your current usage:

1. Navigate to **Settings > Billing**.
2. The usage dashboard shows each metered resource with:
   - Current usage count.
   - Plan limit.
   - Remaining allocation for the current period.
   - Next reset date.

---

## Overage Behavior

When you reach a limit:

- The platform **prevents additional actions** of that type. For example, if you have used all your model fits for the period, clicking "Fit Model" will show a message indicating you have reached your limit.
- You can still use other features that are within their limits.
- Usage resets automatically at the start of your next billing period.
- Alternatively, **upgrade your plan** to immediately increase your limits.

---

## Tips for Managing Usage

- **Use Smart Defaults and prior predictive checks** to validate your configuration before using a model fit. This reduces wasted fits on misconfigured models.
- **Save optimization runs** for when you have finalized your model. Run scenarios first to explore "what if" questions before committing to a formal optimization.
- **Clone models** instead of creating new ones from scratch when iterating on configurations.
- **Archive completed models** you no longer need to free up saved model slots.
- **Monitor your usage** periodically via Settings > Billing, especially mid-period when you may need to pace your remaining allocations.

---

## Next Steps

- [Pricing and Plans](../pricing/README.md) --- Full plan comparison and pricing details
- [Account Setup](../getting-started/account-setup.md) --- Upgrading and managing your subscription
