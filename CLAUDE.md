# Claude Code Rules — Simba Documentation Process

## Repository Layout

- **Application codebase (READ ONLY)**: `C:/Users/iamni/OneDrive/Documents/simba/` — the private Simba app repo. Read component files here to verify UI elements, labels, icons, logic. **Never write to this repo.**
- **Documentation repo (WRITE HERE)**: `C:/Users/iamni/OneDrive/Documents/simba-doc/` — this repo. All documentation edits, charts, screenshots, and markdown changes happen here.
- **Remote**: `https://github.com/nialloulton/simba-mmm` (public GitHub Pages) — push branches and PRs here.

> **Workflow**: Read from the app codebase → Write to this docs repo → Push to GitHub.

## Documentation Update Process

### 1. Setup

```bash
# You are already in the docs repo (simba-doc)
# Always start from latest main
git fetch origin main
git checkout -b docs/<descriptive-branch-name> origin/main
```

> **Windows path note**: When generating charts or screenshots with Python, save to `C:\tmp\` then copy into the docs repo. Bash `/tmp/` maps to `C:\Users\iamni\AppData\Local\Temp\` which is different from Python's `C:\tmp\`.

### 2. Cross-Reference Against the Application Codebase

Every documentation page MUST be validated against the actual application code. Check for these known terminology issues:

| Wrong Term | Correct Term | Where to verify |
|---|---|---|
| "glass-box" | "fully transparent" | grep codebase — zero hits for glass-box |
| "AI Data Auditor" | "Data Validator" | `client/shared/components/skills/DataValidatorModal.tsx` |
| "Budget Intelligence" | "Budget Optimizer" | Nav tabs: `client/shared/components/NavTabsV2/TABS.tsx` |
| "workspaces" | "projects" | `src/dashboard/models.py` — table is called `projects` |
| "Sandbox" plan | "Trial" plan | `src/subscription/tier_config.py` |
| "14-day trial" | "28-day trial" | `src/subscription/tier_config.py` line 30: `TRIAL_DURATION_DAYS = 28` |
| "90% credible interval" or "95% CI" | "94% HDI (3%-97%)" | `src/ai_model/simba/results.py` — uses `hdi_3%` and `hdi_97%` |
| "Audit, Measure, Predict, Optimize" workflow | Navigation is: Model Warehouse, Active Model, Optimization, Scenario Planner | `client/shared/components/NavTabsV2/TABS.tsx` |
| Lift tests as "priors" | Lift tests as "likelihood observations" | `src/ai_model/simba/core.py` — method `add_lift_test_measurements` |
| "power law adstock" | Does NOT exist — only geometric and delayed | `src/ai_model/simba/transforms.py` |
| Saturation formula "tanh(spend / scale)" (one param) | `tanh(x / (scalar * alpha))` — two params: scalar (fixed from data max) + alpha (estimated, Gamma mu=1.7) | `src/ai_model/simba/transforms.py` — `tanh` method; `src/ai_model/simba/priors.py` line 245 |
| UI distributions: "Beta", "HalfNormal", "LogNormal" | UI only offers: Normal, InverseGamma, TruncatedNormal, TVP | `AGGridPriorTable.tsx` — dropdown has `['normal', 'truncatednormal', 'inversegamma', 'tvp']` |
| InverseGamma "for variance/scale params" | InverseGamma is the **default for media channel coefficients** | `calculateSmartPriors.ts` — all media channels get InverseGamma |
| Saturation uses single "scale" parameter | Two parameters: scalar (max activity, fixed) + alpha (shape, Gamma prior mu=1.7, sigma=alpha_sd) | `src/ai_model/simba/priors.py` — alpha prior; `core.py` — scalar from max |
| Order of operations "typically" adstock first | Definitively: adstock → saturation → coefficient (always) | `src/ai_model/simba/transforms.py` — `adstock_with_saturation` method |
| Events as "binary or weighted variables" | GP-smoothed one-hot indicators with hierarchical Normal weights and Matern32 kernel | `src/ai_model/simba/core.py` — `event_dummies` method (lines 741-766) |
| Seasonality "same approach as Prophet" | PyMC's own Fourier implementation (inspired by Prophet, not using it) | `src/ai_model/simba/core.py` — `fourier_series_positive` and `seasonality_model` |
| Trend as simple "gradual shifts" | UI only exposes `smooth_lltrend` (HSGP Matern52). Backend also has `lltrend` (GRW) and `changepoint` but these are NOT in UI | `src/ai_model/simba/core.py` — `trend_model`; `client/.../ModelDetails/store/state.ts` — `t_type: 'smooth_lltrend'` hardcoded |
| Weekly seasonality always available | Weekly seasonality **only for daily data**, disabled by default, opt-in via checkbox, default n=3 | `src/ai_model/simba/core.py` — `seasonality_model` checks `periodicity == 'daily'`; `AdvancedOptions.tsx` |
| Seasonality default "n=10 Fourier terms" | Frontend defaults to **n=2** (backend default of 10 is overridden). Range 1-25 | `client/.../constants.ts` line 92; `AdvancedOptions.tsx` lines 174-181 |
| Seasonality and trend "always enabled" | Both are **opt-in** — disabled by default, enabled via checkboxes | `AdvancedOptions.tsx` — `seasonality` and `trend` checkboxes |
| Upload accepts "CSV and Excel (.xlsx)" | **CSV only** (50MB max). Excel not supported | `src/core/file_validator.py` — CSVFileValidator class |
| "AI Data Auditor" or "Data Auditor" | **"Data Validator"** (10 validation categories) | `client/shared/components/skills/DataValidatorModal.tsx`; `src/skills/definitions/data-validator/` |
| VAR as generic "Vector AutoRegression" | **Bayesian VAR** with PyMC, Minnesota prior shrinkage (lambda=0.2, own-lag mu=0.9), LKJ Cholesky covariance | `src/ai_model/var_model.py`; `src/ai_model/services/var_fitter.py` |
| VAR lag selection "automatic" | **User-configured** only, no AIC/BIC auto-selection. Min data = lags + 10 | `var_fitter.py` — `_check_data_sufficiency()` |
| Enterprise tier for VAR | Not in tier_config.py — only Trial, Analyst(no), Pro, Scale defined | `src/subscription/tier_config.py` |

### Key codebase locations for verification

| Feature | Where to check |
|---|---|
| **Model fitting / Bayesian core** | `src/ai_model/simba/core.py` |
| **Transforms (adstock, saturation)** | `src/ai_model/simba/transforms.py` — uses `tanh` saturation |
| **Smart priors** | `client/pages/warehouse/tabs/configuration/components/PriorBuilder/utils/calculateSmartPriors.ts` |
| **Semantic channel matching** | `client/pages/warehouse/tabs/configuration/components/VariableSelection/semanticMatcher.ts` |
| **Prior distributions available** | `client/pages/warehouse/tabs/configuration/components/PriorBuilder/components/AGGridPriorTable.tsx` |
| **Data Validator** | `src/skills/definitions/data-validator/SKILL.md` and `src/skills/definitions/data-validator/validators/` |
| **Halo channels** | `client/pages/activeModel/utils/haloHelpers.ts`, `calculateSmartPriors.ts` (0.005 fixed coeff) |
| **Trademark channels** | `client/pages/activeModel/utils/trademarkHelpers.ts`, `calculateSmartPriors.ts` (25% reduction) |
| **Portfolio optimizer** | `src/budget_optimizer/services/portfolio_optimizer.py` |
| **Optimizer objective** | `src/ai_model/simba/optimizer_objective.py` |
| **Subscription tiers** | `src/subscription/tier_config.py` |
| **Navigation / UI structure** | `client/shared/components/NavTabsV2/TABS.tsx` |
| **Lift test integration** | `src/ai_model/simba/core.py` — `add_lift_test_measurements` method |
| **Model statuses** | `src/ai_model/services/simba_fitter.py` |
| **VAR modeling (fitter)** | `src/ai_model/services/var_fitter.py` — orchestrates fit, IRF, FEVD, long-run effects extraction |
| **VAR model (core)** | `src/ai_model/var_model.py` — Bayesian VAR with Minnesota priors, IRF, FEVD, long-run Psi_inf = (I-A_sum)^{-1} |
| **VAR prior checker** | `src/ai_model/services/var_prior_checker.py` — prior predictive checking (disabled by default) |
| **VAR-MMM linking UI** | `client/pages/warehouse/tabs/portfolios/components/LinkVARDialog.tsx` — smart matching (100%/80%/50%/0%) |
| **Prior application (distribution_map)** | `src/ai_model/simba/priors.py` — maps distribution names to PyMC classes, alpha Gamma(mu=1.7), decay Beta |
| **Response curve generation** | `src/ai_model/simba/plotting.py` — vectorized tanh eval with all posterior samples |
| **Saturation function (tanh)** | `src/ai_model/simba/transforms.py` — `tanh(x / (scalar * alpha + 1e-9))`, clipped to [-20, 20] |
| **Seasonality (Fourier)** | `src/ai_model/simba/core.py` — `seasonality_model()`, default n=10 terms, prior_scale=10, weekly only for daily data |
| **Trend modeling** | `src/ai_model/simba/core.py` — `trend_model()`, three types: smooth_lltrend (HSGP, default), lltrend (GRW), changepoint |
| **Event/holiday effects** | `src/ai_model/simba/core.py` — `event_dummies()`, GP-smoothed Matern32, hierarchical Normal weights |
| **Holiday selector UI** | `client/pages/warehouse/tabs/configuration/components/HolidaySelector/` — `date-holidays` library, country codes |
| **Periodicity detection** | `src/ai_model/simba/core.py` — `determine_periodicity()`, infers daily/weekly/monthly/irregular from date gaps |
| **Advanced options (seasonality/trend UI)** | `client/pages/warehouse/tabs/configuration/components/ModelDetails/components/AdvancedOptions.tsx` — seasonality_n default=2, weekly_seasonality_n default=3, trend/seasonality opt-in checkboxes |
| **Model config initial state** | `client/pages/warehouse/tabs/configuration/constants.ts` — `seasonality_n: 2`; `client/.../ModelDetails/store/state.ts` — `t_type: 'smooth_lltrend'` |
| **File upload/validation** | `src/core/file_validator.py` — CSVFileValidator, 50MB limit, MIME type checks |
| **Date parsing** | `src/ai_model/simba/utils.py` — `parse_dates()`, 10 date formats + pandas fallback |
| **Semantic channel matching** | `client/pages/warehouse/tabs/configuration/components/VariableSelection/semanticMatcher.ts` — 13 channel categories, 8 metric types |
| **Data Validator validators** | `src/skills/definitions/data-validator/validators/` — 10 categories: schema, frequency, alignment, multiplier, controls, coverage, outlier, multicollinearity, leakage, documentation |

### 3. Charts and Visual Assets

Every documentation page that explains a concept should include relevant charts. Generate charts using Python/matplotlib with this consistent style:

```python
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Arial', 'DejaVu Sans'],
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 12,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': '#FAFBFC',
    'axes.facecolor': '#FAFBFC',
    'axes.edgecolor': '#D0D7DE',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.color': '#D0D7DE',
    'legend.framealpha': 0.9,
    'legend.edgecolor': '#D0D7DE',
})

# Standard color palette
COLORS = ['#2563EB', '#F97316', '#10B981', '#EF4444', '#8B5CF6', '#EC4899']
```

**Chart guidelines:**
- Save to `docs/core-concepts/images/` (or appropriate section's `images/` dir)
- Use `dpi=180` and `bbox_inches='tight'`
- Always include captions in markdown: `![Alt text](./images/name.png)\n*Caption text*`
- On Windows, Python saves to `C:\tmp\` but git repo is in MSYS2 `/tmp/` — copy files between them
- Chart types that work well:
  - **Stacked area** for revenue decomposition / contributions
  - **Side-by-side panels** for before/after or comparison views
  - **Horizontal bar** for channel comparisons
  - **Violin / density** for posterior distributions
  - **Flow diagrams** for workflows and processes (use `FancyBboxPatch` + `annotate`)
  - **Line charts** for decay curves and time series

### 4. Platform Guide — UI Mockup Process

Platform guide pages document the step-by-step workflow within Simba. Every platform guide page MUST include **pixel-accurate UI mockups** that reproduce the actual application interface, with numbered annotation callouts explaining each element.

#### When to use UI mockups (platform-guide/) vs. matplotlib charts (core-concepts/)

| Section | Visual type | Tool |
|---|---|---|
| `docs/core-concepts/` | Statistical/conceptual charts (curves, distributions, decompositions) | Python/matplotlib |
| `docs/platform-guide/` | UI mockups that match the actual Simba interface | HTML/Tailwind + preview screenshot |
| `docs/data/` | Workflow diagrams + data format examples | Python/matplotlib |
| `docs/use-cases/` | Summary visuals, case study cards | Python/matplotlib |

#### Simba Design Token Reference

Source: `client/shared/design-tokens.ts`

```
Primary gradient:    from-blue-500 to-purple-600
Cards:               bg-white rounded-lg border-2 border-slate-200 p-8
Stepper active:      gradient blue-purple circle, scale-110, shadow-lg
Stepper complete:    green-500 circle with checkmark
Stepper pending:     slate-200 circle, slate-500 text
Buttons primary:     bg-gradient-to-r from-blue-500 to-purple-600 text-white shadow-lg
Strategy cards:      border-2 rounded-xl, selected = border-blue-500 bg-blue-50 shadow-lg scale-105
Typography:          H1=text-4xl bold slate-900, H2=text-3xl semibold slate-800, Body=text-base slate-600
Semantic colors:     info=blue-50/blue-700, success=emerald, warning=amber, purple for halo
Halo badge:          purple-100 text-purple-700
Trademark badge:     amber-100 text-amber-700
Background:          slate-50
Borders:             slate-200
```

#### UI Mockup Creation Process — Exact Frontend Recreation

The goal is to **exactly recreate the frontend** — not approximate it. Every label, icon, color, layout, toggle, input, badge, and conditional element must match the actual React components. The mockups should be indistinguishable from screenshots of the real application (except for annotation callouts).

**Step 1: Read EVERY component file for the feature**

Before writing a single line of HTML, read the actual React/TypeScript component files. For each component, extract:

- **Every JSX element**: inputs, buttons, sliders, toggles, dropdowns, tables, cards, badges, icons
- **Exact label text**: copy strings verbatim from the TSX (e.g., `"Warm Start"`, not "Enable Warm Start")
- **Exact icon names**: from Lucide imports (e.g., `<i data-lucide="trending-up">`, not a generic arrow)
- **Conditional rendering**: what shows/hides based on state (e.g., laydown step skipped for single period)
- **Default values**: initial state from store files or constants (e.g., gamma defaults, preset bounds)
- **Tailwind classes**: copy the actual `className` strings from the components
- **Grid layouts**: exact `grid-cols-N`, `gap-N`, padding, margin values
- **AG Grid columns**: column definitions, pinned columns, cell renderers, formatters
- **InfoBox variants**: `variant="info"`, `variant="warning"`, `variant="success"`, `variant="purple"` — each has distinct colors
- **Badge styles**: halo = `purple-100 text-purple-700`, trademark = `amber-100 text-amber-700`, etc.
- **Button variants**: `primary` (gradient), `outline` (border), `outlineBlue`, `primaryLarge`

Use the Explore agent with "very thorough" to read all component files for a feature. Report every element found.

**Step 2: Create a standalone HTML mockup**

```html
<script src="https://cdn.tailwindcss.com"></script>
<script src="https://unpkg.com/lucide@latest"></script>
```

Build each wizard step or page section as a separate `<section>` with a unique ID. For every element:

- Use the **exact same Tailwind classes** from the component source
- Use the **exact same Lucide icon names** from the imports
- Use the **exact same text strings** from the JSX
- Use **realistic marketing data** in inputs/tables (channel names like "TV", "Facebook", "Google Ads"; budgets like $500,000; CPMs like $12.50)
- Reproduce **every conditional state**: selected/unselected cards, enabled/disabled toggles, active/pending stepper steps
- Include **badges and special indicators**: "ADVANCED", "FASTEST", "🌟 Halo", "👑 Trademark", "Excluded from optimization"

**Step 3: Add numbered annotation callouts**

Colored circles (1, 2, 3...) positioned with `position: absolute` over key UI elements:

```css
.anno { position:absolute; width:28px; height:28px; border-radius:50%;
        display:flex; align-items:center; justify-content:center;
        font-weight:700; font-size:13px; color:#fff; z-index:50;
        box-shadow:0 2px 6px rgba(0,0,0,0.3); }
.anno-blue { background:#2563EB; }
.anno-orange { background:#F97316; }
.anno-green { background:#10B981; }
.anno-purple { background:#8B5CF6; }
```

**Step 4: Serve and screenshot with Playwright**

Serve the HTML via `preview_start` (`.claude/launch.json` config for `python -m http.server`), then capture full-element screenshots using Playwright:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': 1280, 'height': 900})
    page.goto('http://localhost:3847/index.html')
    page.wait_for_load_state('networkidle')
    page.wait_for_timeout(2000)  # wait for Lucide icons

    for section_id, filename in SECTIONS:
        el = page.locator(f'#{section_id}')
        el.screenshot(path=f'C:/tmp/opt-screenshots/{filename}')

    browser.close()
```

This produces clean, full-element screenshots without viewport clipping.

**Step 5: Visually verify every screenshot**

Read each PNG file back and check:
- Layout matches the component source
- All text is readable, no overlap
- Annotations don't obscure important content
- Icons rendered correctly (Lucide loaded)
- Colors match design tokens exactly

**Step 6: Copy to docs and write documentation**

Copy screenshots to `docs/platform-guide/images/` and write the markdown with annotation tables.

#### Mockup Quality Checklist

- [ ] **Read the actual component source** before building (never guess at labels, icons, or layout)
- [ ] Every interactive element (buttons, sliders, toggles, dropdowns, AG Grid tables) is reproduced
- [ ] **Labels and text match verbatim** — copied from the TSX, not paraphrased
- [ ] **Icons match exactly** — same Lucide icon names as the component imports
- [ ] **Tailwind classes match** — same colors, spacing, borders, shadows as the real components
- [ ] **Conditional states shown correctly** — selected/unselected, enabled/disabled, active/pending
- [ ] **Badges reproduced** — ADVANCED, FASTEST, Halo (purple), Trademark (amber), Excluded
- [ ] Annotation callouts are visible and don't obscure content
- [ ] Legend below each screenshot explains every numbered callout
- [ ] Realistic marketing data in all inputs/tables
- [ ] Screenshots captured at 1280px width via Playwright (not viewport-clipped browser screenshots)
- [ ] No UI elements that don't exist in the actual app (verify against codebase)
- [ ] Hidden/commented-out features are NOT shown (e.g., AI Assistant tab is hidden)
- [ ] **Visually verified** — each screenshot read back and inspected before committing

#### Platform Guide Documentation Structure

Each platform guide page should follow this structure:

```markdown
# Feature Name --- One-Line Description

Brief intro paragraph (2-3 sentences max).

---

## The [Feature] Wizard / Workflow

### Step N: Step Title

![Step N mockup](./images/feature-stepN.png)
*Caption describing what this step does.*

**① Annotation 1** --- Explanation of the first callout.

**② Annotation 2** --- Explanation of the second callout.

[Repeat for each step]

---

## How It Works (Technical Detail)

[Explain the underlying mechanics — algorithm, constraints, etc.]

---

## Interpreting Results

[How to read and act on the output]

---

## Next Steps

**Platform guides:**
[Links to related platform guide pages]

**Core concepts:**
[Links to the underlying theory pages that explain the mechanics]
```

### 4b. Cross-Referencing Rules

Every documentation page MUST cross-reference related pages. This is mandatory, not optional.

**General rules:**
- First mention of a core concept (saturation, adstock, Bayesian, priors, halo, incrementality, optimization) MUST be hyperlinked to its core concepts page.
- Subsequent mentions in the same section do not need links (avoid link fatigue).
- Technical terms in annotation tables should link to their concept page when they appear for the first time.
- Next Steps sections MUST be split into "Platform guides" and "Core concepts" subsections.

**Platform guide → Core concepts links (required):**

| When you mention... | Link to... |
|---|---|
| Saturation, diminishing returns, response curves | `../core-concepts/saturation-curves.md` |
| Adstock, carryover, decay, lag effects | `../core-concepts/adstock-effects.md` |
| Bayesian, posterior, prior, credible interval, HDI | `../core-concepts/bayesian-modeling.md` |
| Prior distributions, InverseGamma, TruncatedNormal | `../core-concepts/priors-and-distributions.md` |
| Halo effects, trademark channels, cross-brand | `../core-concepts/halo-effects.md` |
| Incrementality, causal attribution, base sales | `../core-concepts/incrementality.md` |
| Gamma, risk-aversion, efficient frontier, marginal curves | `../core-concepts/optimization.md` |
| Seasonality, Fourier, trend, holidays | `../core-concepts/seasonality.md` |
| VAR, impulse response, FEVD, long-run effects | `../core-concepts/var-modeling.md` |

**Core concepts → Platform guide links (recommended):**

| When you mention... | Link to... |
|---|---|
| Model configuration, wizard, setup | `../platform-guide/model-configuration.md` |
| Budget optimization, optimizer | `../platform-guide/budget-optimization.md` |
| Scenario planning, what-if | `../platform-guide/scenario-planning.md` |
| Measurement, results, contributions | `../platform-guide/measurement.md` |
| Data validation, Data Validator | `../platform-guide/data-auditor.md` or `../data/data-validation.md` |
| Portfolio analysis, cross-brand optimization | `../platform-guide/portfolio-analysis.md` |

**Core concepts → Core concepts links (required):**
- Cross-link between related concepts (e.g., saturation page links to adstock, priors links to bayesian-modeling).

### 5. Commit and PR Process

```bash
# Stage specific files (never use git add -A)
git add docs/path/to/changed-file.md docs/path/to/images/*.png

# Commit with descriptive message
git commit -m "docs: <what changed>

<details of changes>

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>"

# Push and create PR
git push -u origin docs/<branch-name>
gh pr create --title "docs: <short title>" --body "$(cat <<'EOF'
## Summary
<bullet points of changes>

## Codebase files referenced
<list of source files checked>

## Test plan
- [ ] Verify charts render on GitHub
- [ ] Cross-reference implementation details with codebase
- [ ] Check all internal links resolve

🤖 Generated with [Claude Code](https://claude.com/claude-code)
EOF
)"
```

**Branch naming**: Always use `docs/` prefix (e.g., `docs/adstock-charts`, `docs/fix-lift-test-mechanism`, `docs/halo-effects-rewrite`)

### 6. Internal Link Conventions

All docs use relative paths within the docs directory:

```markdown
<!-- Within same section -->
[Saturation Curves](./saturation-curves.md)

<!-- Cross-section -->
[Budget Optimization](../platform-guide/budget-optimization.md)
[Bayesian Modeling](../core-concepts/bayesian-modeling.md)
```

**Known broken link patterns to avoid:**
- `../workflow/` — does not exist, use `../platform-guide/`
- `../model-configuration/` — does not exist, use `../platform-guide/`
- `../results/` — does not exist, use `../platform-guide/`
- `../platform/` — does not exist, use `../security/`
- `../data-preparation/` — does not exist, use `../data/`

### 7. Docs Structure

```
docs/
├── getting-started/     # quick-start, account-setup, platform-overview
├── core-concepts/       # mmm, bayesian, incrementality, saturation, adstock, priors, seasonality, halo
│   └── images/          # all chart PNGs for core concepts
├── platform-guide/      # data-auditor, measurement, scenario-planning, budget-optimization, model-config, smart-defaults, long-term-effects
├── data/                # data-requirements, data-preparation, data-validation, supported-channels
├── use-cases/           # brand-marketers, agencies, portfolio-modeling, retail
├── security/            # overview, encryption, infrastructure, compliance, sovereignty
├── faq/
resources/
sales/
```

### 8. Review Checklist

When reviewing any documentation page:

**All pages:**
- [ ] All terminology matches the codebase (see table in section 2)
- [ ] All internal links resolve to existing files
- [ ] Feature descriptions match actual UI behavior
- [ ] Plan names: only Enterprise and Managed (self-serve tiers coming soon, not documented)
- [ ] Statistical concepts match implementation (94% HDI, tanh saturation, geometric/delayed adstock)
- [ ] Lift tests described as likelihood observations, not priors
- [ ] No "glass-box", "AI Data Auditor", "Budget Intelligence", "workspaces", "Sandbox", "power law adstock", or "AI Assistant"
- [ ] No features documented that are hidden/commented out in the UI
- [ ] Contact email is `info@1749.io` (not `support@simba-mmm.com`)
- [ ] Reference to PyMC-Marketing as the foundation is accurate and present where appropriate

**Core concepts pages (additionally):**
- [ ] Charts included for key concepts using matplotlib standard style and color palette
- [ ] Charts generated at `dpi=180` with `bbox_inches='tight'`
- [ ] Charts visually verified (text readable, no overlap, appropriate spacing)

**Platform guide pages (additionally):**
- [ ] UI mockups included for every wizard step / major screen
- [ ] Mockups use Simba design tokens (blue-purple gradient, slate palette, rounded-lg cards)
- [ ] Numbered annotation callouts on each mockup with legend below
- [ ] All UI labels and field names verified against actual component source code
- [ ] Mockups do not show features that are hidden in the frontend

**Cross-referencing (all pages):**
- [ ] First mention of each core concept is hyperlinked to its concept page (see table in section 4b)
- [ ] Platform guide pages link to relevant core concepts for underlying theory
- [ ] Core concepts pages link to platform guide pages where the feature is configured
- [ ] Next Steps sections split into "Platform guides" and "Core concepts" subsections
- [ ] No orphan pages — every page is linked to from at least one other page

---

## STRICT ENFORCEMENT: Platform Guide Rewrite Process

> **IMPORTANT**: Enter plan mode before doing anything. Do NOT write any code or make any changes until the plan is approved.

When rewriting any platform guide page (`docs/platform-guide/[filename].md`), the following phased process is **mandatory**. No shortcuts, no skipping phases.

**Context for every rewrite:**
- **Read from**: App codebase at `C:/Users/iamni/OneDrive/Documents/simba/` (read-only, never write here)
- **Write to**: This docs repo at `C:/Users/iamni/OneDrive/Documents/simba-doc/`
- **Push to**: `nialloulton/simba-mmm` on GitHub
- Windows paths: bash `/tmp/` = `C:\Users\iamni\AppData\Local\Temp`, Python `/tmp/` = `C:\tmp`
- Read this `CLAUDE.md` first — it has the full terminology table, design tokens, cross-referencing rules, and the exact UI mockup process to follow.

### Phase 1: Deep Codebase Exploration (do this in plan mode)

Read **every single file** in the key component paths for the feature. For each file report:

- Every JSX element, exact label string, exact Lucide icon import
- Every Tailwind className
- Every conditional render (`{condition && <Component/>}`)
- Every default value, every constant, every store initial state
- Every AG Grid column definition
- Every InfoBox variant, every badge style, every button variant

For every chart/visualization component, extract:

- Library used (Plotly.js or Recharts)
- Exact trace type (e.g. `type: 'scatter'`, `mode: 'lines+markers'`, `<BarChart>`, `<AreaChart>`)
- Exact color values (hex codes from the component, not approximations)
- Fill/opacity settings (e.g. `fill: 'tozeroy'`, `opacity: 0.3`)
- Axis configuration (title, range, tickformat, gridcolor)
- Layout config (margin, legend position, showlegend, hovermode)
- Data shape and column names used
- Any conditional rendering (e.g. different chart for MMM vs VAR)

Cross-reference the existing `[filename].md` against what you found. **List every inaccuracy.**

### Phase 2: Plan the Mockups (do this in plan mode)

For each screen/wizard step/tab, plan:

- Exact HTML structure matching the component tree
- Which Tailwind classes to use (copied from source)
- What realistic data to show in inputs/tables

**CRITICAL — Chart Recreation Rule:** Every chart in the mockup MUST use the same library as the real component:

- If the component uses **Plotly.js** → use `<script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>` and `Plotly.newPlot()` with the exact same trace type, colors, fill, layout config from the source
- If the component uses **Recharts** → use Recharts via CDN or recreate with Chart.js using the exact same chart type, colors, and data shape
- Copy the **exact hex color values** from the component source
- Match axis labels, legend format, grid styling
- Use realistic synthetic data that looks like real model output
- Do **NOT** substitute matplotlib PNGs or generic placeholder charts

Plan where to place annotation callouts and what each explains.

### Phase 3: Plan the Documentation Structure (do this in plan mode)

Map out every section of the rewritten `.md`:

- Which screenshots go where
- Which annotation table follows each screenshot
- Where each core concept cross-reference goes (first mention only):

| When you mention... | Link to... |
|---|---|
| Saturation, diminishing returns, response curves | `../core-concepts/saturation-curves.md` |
| Adstock, carryover, decay, lag effects | `../core-concepts/adstock-effects.md` |
| Bayesian, posterior, prior, credible interval, HDI | `../core-concepts/bayesian-modeling.md` |
| Prior distributions, InverseGamma, TruncatedNormal | `../core-concepts/priors-and-distributions.md` |
| Seasonality, Fourier, trend, holidays | `../core-concepts/seasonality.md` |
| Halo effects, trademark channels, cross-brand | `../core-concepts/halo-effects.md` |
| VAR, impulse response, FEVD, long-run effects | `../core-concepts/var-modeling.md` |
| Optimization, gamma, efficient frontier, marginal curves | `../core-concepts/budget-optimization.md` |
| Incrementality, causal attribution, base sales | `../core-concepts/incrementality.md` |

### Phase 4: Exit plan mode, then execute

Only after plan approval:

1. Build the HTML mockup with real Plotly.js / Recharts charts (not matplotlib substitutes)
2. Serve and screenshot with Playwright at 1280px width
3. Visually verify every screenshot — read each PNG back, check layout/text/icons/charts render correctly
4. Rewrite the markdown with screenshots + annotation tables
5. Commit, push, create PR

### Enforcement Rules

- **No code before plan approval.** Any attempt to write HTML, generate charts, or edit markdown before exiting plan mode is a violation.
- **No guessing UI elements.** Every label, icon, color, and layout must be verified against the actual component source code.
- **No matplotlib in platform guides.** Platform guide mockups use HTML/Tailwind + the same charting library as the real app (Plotly.js or Recharts). Matplotlib is only for `core-concepts/` statistical charts.
- **No skipping visual verification.** Every screenshot must be read back and inspected before committing.
- **No undocumented features.** If a feature is hidden or commented out in the frontend, it must not appear in the mockup or documentation.
