from pathlib import Path

import pandas as pd

source = Path("data/raw/events.csv")
destination = Path("data/clean/events.csv")
columns = ["user_id", "timestamp", "event_type", "duration_seconds"]
valid_types = {line.strip() for line in Path("event_types.txt").read_text().splitlines() if line.strip() and not line.startswith("#")}
if not valid_types:
    raise ValueError("Add the dataset's valid event types to event_types.txt")

events = pd.read_csv(source, dtype={"user_id": "string", "timestamp": "string", "event_type": "string"})
events = events[columns].dropna()
for column in ("user_id", "timestamp", "event_type"):
    events[column] = events[column].str.strip()
events = events[(events[["user_id", "timestamp", "event_type"]] != "").all(axis=1)]
events["duration_seconds"] = pd.to_numeric(events["duration_seconds"], errors="coerce")
events["timestamp"] = pd.to_datetime(events["timestamp"], format="mixed", errors="coerce", utc=True)
events = events[events["event_type"].isin(valid_types) & (events["duration_seconds"] > 0) & events["timestamp"].notna()].copy()
events["timestamp"] = events["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")
destination.parent.mkdir(parents=True, exist_ok=True)
events.to_csv(destination, index=False)
