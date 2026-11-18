from pathlib import Path

import pandas as pd

events = pd.read_csv("data/transformed/events.csv", dtype={"user_id": "string"})
events["duration_minutes"] = events["duration_seconds"] / 60
events["weekday"] = pd.to_datetime(events["date"]).dt.day_name()
destination = Path("data/features/events.csv")
destination.parent.mkdir(parents=True, exist_ok=True)
events.to_csv(destination, index=False)
