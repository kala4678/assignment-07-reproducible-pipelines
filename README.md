# Reproducible event pipeline

Install dependencies with `uv sync`, then run `uv run dvc repro` from the repository root. The pipeline cleans the raw events, derives dates, and calculates event duration in minutes and weekday. Run `uv run marimo edit notebooks/report.py` to view the report.

The allowed event types belong in `event_types.txt`, one per line. This file is a dependency of the cleaning stage, so changing it causes DVC to rerun the pipeline. Raw data is committed to Git; derived CSVs are managed by DVC's local cache. No DVC remote is required.
