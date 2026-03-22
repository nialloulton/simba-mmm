# AI Assistant --- Interactive Analysis with Claude

The AI Assistant is an interactive, chat-based analysis tool powered by Claude AI. Available within the Active Model results page, it lets you ask questions about your model results in natural language and generates custom interactive dashboards with charts, tables, and analyses.

---

## How It Works

The AI Assistant uses a two-panel layout:

- **Left panel: Chat interface** --- Type your analysis questions in natural language.
- **Right panel: Interactive dashboard** --- The AI generates and renders a fully interactive Marimo notebook with your requested analysis.

When you submit a query, the system goes through several stages:

1. **Loading results** --- The model's data and results are prepared for analysis.
2. **Generating analysis with Claude** --- Claude AI writes the analysis code based on your query.
3. **Validating code** --- The generated code is validated for correctness and safety.
4. **Executing notebook** --- The Marimo notebook is executed to produce visualizations and results.
5. **Rendering** --- The interactive dashboard is rendered in the right panel.

Progress indicators show which stage the generation is currently in, so you know exactly what is happening.

---

## What You Can Ask

The AI Assistant can generate a wide range of analyses from your model results. Example queries:

### Channel Analysis
- "Show me a waterfall chart of channel contributions"
- "Compare ROAS across all channels with credible intervals"
- "Which channels have the highest and lowest incremental contribution?"
- "Create a contribution breakdown by month"

### Response and Efficiency
- "Plot the saturation response curves for all channels on one chart"
- "Show me the marginal return curves --- where are the diminishing returns kicking in?"
- "Compare the adstock decay curves across channels"

### Spend Analysis
- "Analyze the relationship between TV spend and revenue"
- "Show me a scatter plot of spend vs incremental contribution for each channel"
- "Which channels are overspending relative to their contribution?"

### Custom Analysis
- "Create a summary table of all key model metrics"
- "Show the seasonal decomposition of base sales"
- "Compare the prior and posterior distributions for each channel"

---

## Interactive Dashboards

The generated outputs are fully interactive Marimo notebooks, not static images:

- **Hover** over chart elements to see exact values.
- **Zoom and pan** on charts to explore specific time periods or data ranges.
- **Interactive tables** support sorting and filtering.
- Charts and visualizations respond to your specific data and model results.

---

## Tips for Getting the Most Out of the AI Assistant

- **Be specific** --- "Show me a bar chart of ROAS by channel" produces better results than "analyze my channels."
- **Iterate** --- If the first result is not quite right, refine your query. The chat history provides context for follow-up questions.
- **Ask for comparisons** --- The assistant excels at comparative analyses: channel vs channel, period vs period, prior vs posterior.
- **Request specific chart types** --- If you want a particular visualization (waterfall, heatmap, scatter, bar), mention it in your query.

---

## Availability

The AI Assistant is available on all subscription tiers within the Active Model results page.

---

## Next Steps

- [Incremental Measurement](./measurement.md) --- Understanding the model results that the AI Assistant analyzes
- [Exports and Reporting](./exports-reporting.md) --- Export your analyses as PDF reports or CSV data
- [Model Configuration](./model-configuration.md) --- Configure the model that produces the results
