import marimo

__generated_with = "0.11.0"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd
    from pathlib import Path
    return Path, mo, pd, plt


@app.cell
def _(Path, pd):
    path = Path("data/features/events.csv")
    if not path.exists():
        path = Path("../data/features/events.csv")
    events = pd.read_csv(path)
    return events, path


@app.cell
def _(events, plt):
    fig, ax = plt.subplots()
    ax.hist(events["duration_minutes"], bins=20, edgecolor="white")
    ax.set(title="Distribution of event durations", xlabel="Duration (minutes)", ylabel="Number of events")
    fig
    return ax, fig


if __name__ == "__main__":
    app.run()
