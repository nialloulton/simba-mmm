# Exports and Reporting --- PDF Reports and CSV Downloads

Simba supports exporting analysis results as PDF reports and CSV data files for offline analysis, stakeholder communication, and integration with other tools.

---

## PDF Report Generation

Generate comprehensive PDF reports from any completed model's results page.

### What Is Included

A PDF report includes all key model outputs in a print-ready format:

- **Channel contribution charts** --- Stacked area and waterfall visualizations showing each channel's incremental contribution over the modeled period.
- **ROAS summary** --- Return on ad spend for each channel with posterior medians and credible intervals.
- **Adstock curves** --- Per-channel carryover decay visualizations.
- **Saturation response curves** --- Per-channel diminishing returns curves showing the relationship between spend and impact.
- **Model fit** --- Actual vs predicted KPI over time.
- **Diagnostics** --- Convergence metrics, posterior predictive checks, and model quality indicators.

### Generating a Report

1. Open a completed model from the Active Model page.
2. Click the **Generate PDF Report** button (or the export/download icon).
3. The report is generated and downloaded to your browser.

### Use Cases

- Share results with executives and stakeholders who do not have Simba access.
- Include in quarterly business reviews and media planning presentations.
- Archive model results for regulatory or audit purposes.

---

## CSV Data Export

Download model results as CSV files for further analysis in spreadsheets, R, Python, or other tools.

### Available Export Types

Multiple CSV export types are available depending on the result component:

- **Contributions** --- Channel-level contribution values over time.
- **Coefficients** --- Estimated model coefficients with posterior statistics.
- **Predictions** --- Model predictions and residuals.
- **Additional model outputs** --- Other result components as applicable.

### Downloading CSVs

1. From the Active Model results dashboard, locate the chart or table you want to export.
2. Click the **Download CSV** button or export icon.
3. Select the specific result type to download.
4. The CSV file is downloaded to your browser.

---

## Chart and Visualization Exports

Individual charts can be exported as images for use in custom presentations:

- Hover over any chart to reveal export options.
- Export as PNG for inclusion in slide decks or documents.
- Charts are exported at high resolution suitable for printing.

---

## Scenario Comparison Exports

Export scenario planning results for stakeholder presentations:

- From the Scenario Planning page, compare multiple scenarios.
- Export the comparison view as a downloadable report.
- Useful for presenting budget options to decision-makers.

---

## Tips

- **Use PDF reports for executive audiences** --- they provide a comprehensive, self-contained summary without requiring platform access.
- **Use CSV exports for further analysis** --- when you need to combine model results with other data sources, perform custom calculations, or feed results into downstream systems.
- **Export charts individually** when building custom presentations that mix Simba results with other content.
- **Keep reports archived** --- generate and save PDF reports after each model iteration to maintain a history of how your understanding evolved.

---

## Next Steps

- [Incremental Measurement](./measurement.md) --- Understanding the results that reports contain
- [Sharing and Collaboration](./sharing-collaboration.md) --- Share results within the platform
