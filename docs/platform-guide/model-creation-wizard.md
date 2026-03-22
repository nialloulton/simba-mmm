# Model Creation Wizard --- Step-by-Step Model Setup

The Warehouse configuration tab guides you through a five-step wizard to create and configure a new marketing mix model. This guide walks through each step in detail.

---

## Step 1: Source Configuration

Upload your data and configure the data source.

### File Upload

- **Drag and drop** a CSV or Excel file onto the upload area, or click to browse your file system.
- Simba parses the file and displays a preview of detected columns with data types and sample values.
- Supported formats: CSV (.csv) and Excel (.xlsx).

### Pipeline Output

Alternatively, select an output from a [Data Pipeline](./data-pipelines.md) as your data source. This links the model to a specific pipeline version for full traceability.

### Data Transformation

Basic transformation options are available at upload time to prepare the data before it enters the modeling pipeline.

---

## Step 2: Variable Selection

Categorize each column in your dataset by its role in the model.

### Variable Categories

| Category | Description |
|---|---|
| **Date** | The time period column (weekly or daily dates). |
| **Target KPI** | The business outcome you want to model (revenue, conversions, leads, etc.). |
| **Media Channel** | Marketing activity variables (spend, impressions, GRPs, clicks). |
| **Cost Variable** | Spend data associated with media channels (used for ROI calculations). |
| **Control Variable** | Non-media factors that influence the target (pricing, promotions, weather, competitors). |
| **Hierarchy Variable** | For multi-brand or multi-region models, the column that defines the split (e.g., brand name, region). |

### AI-Powered Semantic Matching

Simba uses AI to automatically suggest categorizations based on column names:

- The system analyzes variable names and metadata patterns.
- Each suggestion includes a **confidence score** indicating how certain the AI is about the categorization.
- High-confidence suggestions (60%+) are highlighted for quick acceptance.
- You can accept individual suggestions or use **auto-categorize** to apply all suggestions at once.

### Halo and Trademark Channels

During variable selection, you can mark channels as halo channels or trademark channels for multi-brand portfolio analysis. Simba's semantic detection will suggest candidates automatically. See [Halo and Trademark Channels](./halo-trademark-channels.md) for details.

---

## Step 3: Prior Builder

Configure Bayesian priors for each media channel variable. Priors encode your beliefs about each channel's effectiveness before the model sees the data.

### Visual Distribution Editor

- See the **shape of your prior distribution** as you adjust parameters in real time.
- The visual preview updates instantly, showing how changes to the mean, standard deviation, or distribution type affect the prior.

### Decay Curve Visualization

- Preview how the **adstock decay curve** will distribute each channel's effect over time.
- Adjust the decay rate and see the implied half-life and carryover pattern.

### Configuration Options

For each channel, set:

- **Distribution type**: InverseGamma or TruncatedNormal.
- **Mean**: Your best estimate of the channel's effect size.
- **Saturation**: The half-saturation point controlling where diminishing returns begin.
- **Decay**: The adstock retention rate controlling carryover.

### Smart Defaults

Click **Smart Defaults** to auto-generate sensible priors based on your data patterns and industry benchmarks. This is the recommended starting point for most users. See [Smart Defaults](./smart-defaults.md).

---

## Step 4: Model Setup

Configure advanced model settings.

### Model Type

Select between:

- **Standard MMM**: Single-equation model for channel attribution and optimization (default).
- **VAR**: Vector AutoRegression for understanding inter-channel dynamics. See [VAR Models](./var-models.md).

### Adstock Type

Choose the adstock function for each channel:

- **Geometric** (default): Immediate peak with exponential decay.
- **Delayed**: Peak occurs after a configurable delay, then decays.

See [Adstock Effects](../core-concepts/adstock-effects.md) for detailed explanations.

### Seasonality

Configure Fourier-based seasonality terms:

- **Monthly seasonality**: Captures annual patterns (number of Fourier terms controls smoothness).
- **Weekly seasonality**: For daily data, captures within-week patterns.
- Higher numbers of Fourier terms capture more complex seasonal patterns but risk overfitting.

### Variable Transformations

Apply mathematical transformations to variables:

- **Identity** (default), **Log**, **Log-Log**, **Power**, **Box-Cox**.
- See [Model Configuration](./model-configuration.md) for guidance on when to use each transformation.

---

## Step 5: Model Details

Finalize the model configuration and start fitting.

### Lift Test Calibration

If you have experimental results (geo-lift tests, conversion lift studies, holdout tests):

1. Enter the channel, the measured lift, and the confidence interval.
2. Simba incorporates these as Bayesian priors, strengthening the model's attribution for calibrated channels.
3. Lift test calibration is optional but recommended when available.

### Final Review

- Review the complete model summary: all selected variables, their categories, prior configurations, adstock settings, and model type.
- Name your model and add optional notes for future reference.

### Start Fitting

Click **Fit Model** to begin Bayesian inference. The model enters the task queue.

---

## After the Wizard

Once submitted, the model progresses through these statuses:

| Status | Description |
|---|---|
| **Pending** | Queued, waiting for compute resources. |
| **Under Way** | Bayesian inference is actively running with a progress indicator. |
| **Complete** | Results are available for review. |
| **Failed** | An error occurred. Check the error message for guidance. |
| **Revoked** | Cancelled by the user before completion. |
| **Time Exceeded** | Exceeded maximum computation time. Simplify the model and retry. |

You can navigate away during fitting and return when it completes. Check status from the Warehouse or Dashboard.

---

## Next Steps

- [Model Configuration](./model-configuration.md) --- Detailed prior and parameter configuration
- [Smart Defaults](./smart-defaults.md) --- How auto-generated defaults work
- [Incremental Measurement](./measurement.md) --- Interpreting your model results
- [VAR Models](./var-models.md) --- VAR-specific model creation
