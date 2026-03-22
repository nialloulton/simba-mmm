# Data Pipelines --- Visual Data Pipeline Builder

Data Pipelines is Simba's visual, node-based pipeline builder for creating repeatable data preparation workflows. Instead of manually preparing CSV files externally, you can build visual ETL pipelines that combine data sources, apply transformations, and produce versioned datasets ready for modeling.

---

## Overview

A pipeline is a directed graph of **nodes** connected by **edges**. Data flows from source nodes (connectors) through transform nodes and produces an output dataset. Once built, a pipeline can be re-executed as new data becomes available, producing versioned snapshots that maintain a complete history of your data preparation.

---

## The Visual Canvas

The pipeline canvas is a drag-and-drop workspace where you construct your data flow:

- **Nodes** represent data sources or transformations. Drag them from the Node Palette onto the canvas.
- **Edges** connect nodes to define the flow of data. Drag from one node's output port to another node's input port.
- **Selection** --- Click any node to view and edit its configuration in the Config Panel on the right.

The canvas supports zooming, panning, and standard selection interactions for managing complex pipelines.

---

## Node Palette

The Node Palette provides the building blocks for your pipeline, organized into two categories:

### Connectors (Data Sources)

Connectors bring data into the pipeline:

- **CSV File** --- Upload a CSV file as a data source. The file is stored securely and can be reused across pipeline runs.
- **Excel File** --- Upload an Excel (.xlsx) file. Select the specific sheet to use.
- **External Connectors** --- Connect to external data sources such as Meteostat (weather data) and other third-party APIs. External connectors pull data automatically based on your configuration.

### Transforms

Transforms process data as it flows through the pipeline:

- **Filter** --- Remove rows based on conditions (e.g., date range, value thresholds).
- **Merge** --- Combine two data sources by joining on a shared key column (e.g., date).
- **Aggregate** --- Group data by one or more columns and compute summary statistics (sum, mean, count, etc.).
- **Calculate** --- Create new columns using formulas and expressions.
- **Column Operations** --- Rename, reorder, drop, or reshape columns.

---

## Config Panel

Click any node on the canvas to open its configuration in the right-side panel. Each node type has specific settings:

- **Connector nodes**: Select the source file, configure column mappings, set date parsing options.
- **Transform nodes**: Define filter conditions, join keys, aggregation functions, or calculation expressions.
- **Preview button**: See a sample of the node's output data without running the full pipeline.

---

## Data Preview

Before committing to a full pipeline run, you can preview data at any point in the pipeline:

- Click a node and use the **Preview** option to see its output.
- Preview the final pipeline output to confirm the dataset is ready for modeling.
- Preview shows column names, data types, row counts, and sample rows.

---

## Pipeline Execution

To produce a dataset from your pipeline:

1. Click **Run Pipeline** to execute all nodes in dependency order.
2. The pipeline progresses through statuses: **Pending** → **Running** → **Completed** (or **Failed** / **Cancelled**).
3. On successful completion, a new **version** is created containing the output dataset.
4. If the pipeline fails, check the execution logs for error details and adjust your node configuration.

---

## Version Management

Each successful pipeline execution creates a versioned snapshot of the output:

- **Version list** --- View all versions with timestamps, row counts, column counts, and data checksums.
- **Compare versions** --- Select two versions and compare them side by side to understand what changed between runs (new rows, modified values, schema changes).
- **Download** --- Download any version as a CSV file for use outside Simba.
- **Metadata** --- Each version records execution parameters and data statistics for auditability.

Versioning ensures full reproducibility --- you can always trace back to the exact data that was used for any model.

---

## Date Range Extension

When new data becomes available, you do not need to rebuild your pipeline from scratch:

1. Open an existing pipeline.
2. Use the **Extend** option to specify a new date range.
3. The pipeline re-executes with the extended range and produces a new version.

This is useful for monthly data refreshes where you want to append new periods to an existing dataset.

---

## File Management

Manage the source files used by your pipeline connectors:

- **Upload files** --- Add new CSV or Excel files to your file library.
- **Preview files** --- View file contents, column types, and summary statistics before using them in a pipeline.
- **Delete files** --- Remove files you no longer need.
- Files are encrypted at rest using the same AES-256 encryption as all Simba data.

---

## Using Pipeline Output for Modeling

Pipeline outputs integrate directly with the model creation workflow:

1. Build and run your pipeline to produce a clean, versioned dataset.
2. In the Warehouse, when creating a new model, select a pipeline output as your data source instead of uploading a file manually.
3. The pipeline version is linked to the model, so you always know exactly which data version was used.

---

## Best Practices

- **Start simple** --- Begin with a single connector and add transforms incrementally, previewing at each step.
- **Use version comparison** --- After extending a date range or modifying transforms, compare the new version against the previous one to catch unexpected changes.
- **Name pipelines clearly** --- Use descriptive names that indicate the brand, market, or data combination (e.g., "UK Revenue + Media + Weather Weekly").
- **Reuse pipelines** --- Once a pipeline is built and validated, re-execute it monthly as new data arrives rather than rebuilding each time.

---

## Next Steps

- [Data Requirements](../data/data-requirements.md) --- Understand what data Simba needs for modeling
- [Data Validation](../data/data-validation.md) --- How the AI Data Auditor validates your data
- [Model Creation Wizard](./model-creation-wizard.md) --- Use your pipeline output to build a model
