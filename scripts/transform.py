from pathlib import Path

import pandas as pd

events = pd.read_csv("data/clean/events.csv", dtype={"user_id": "string"})
events["date"] = pd.to_datetime(events["timestamp"]).dt.strftime("%Y-%m-%d")
destination = Path("data/transformed/events.csv")
destination.parent.mkdir(parents=True, exist_ok=True)
events.to_csv(destination, index=False)
