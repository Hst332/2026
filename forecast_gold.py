import pandas as pd
from datetime import datetime
import metals_bundle

# Lade Daten
df = metals_bundle.load_gold()
last = df.iloc[-1]

last_date = last.name.strftime("%Y-%m-%d")
close = float(last["Close"])
prob_up = float(last["prob_up"])

# Handelslogik
if 0.53 <= prob_up < 0.55:
    signal = "YES"
    position = "50 %"
elif prob_up >= 0.55:
    signal = "YES"
    position = "100 %"
else:
    signal = "NO_TRADE"
    position = "0 %"

# Result-Dictionary
gold_result = {
    "asset": "GOLD",
    "date": last_date,
    "close": close,
    "prob_up": prob_up,
    "signal": signal,
    "position": position,
    "signal_rules": {"yes50":0.53, "yes100":0.55},
    "strategy_lines": [
        "0.53–0.55 → YES50",
        "≥ 0.55 → YES100",
        "No Short | Lev ≤ 5"
    ]
}
