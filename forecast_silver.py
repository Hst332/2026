import pandas as pd
from datetime import datetime
import metals_bundle

# Lade Daten
df = metals_bundle.load_silver()
last = df.iloc[-1]

last_date = last.name.strftime("%Y-%m-%d")
close = float(last["Close"])
prob_up = float(last["prob_up"])

# Handelslogik
if prob_up >= 0.96:
    signal = "YES"
    position = "100 %"
elif prob_up >= 0.90:
    signal = "YES"
    position = "50 %"
else:
    signal = "NO_TRADE"
    position = "0 %"

# Result-Dictionary
silver_result = {
    "asset": "SILVER",
    "date": last_date,
    "close": close,
    "prob_up": prob_up,
    "signal": signal,
    "position": position,
    "signal_rules": {"yes100":0.96, "yes50":0.90},
    "strategy_lines": [
        "≥ 0.96 → LONG",
        "0.90–0.96 → LONG 50 %",
        "Long only | Lev ≤ 15 | SL −20 %"
    ]
}
