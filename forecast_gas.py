import pandas as pd
from datetime import datetime
import metals_bundle

# Lade Daten
df = metals_bundle.load_gas()
last = df.iloc[-1]

last_date = last.name.strftime("%Y-%m-%d")
close = float(last["Close"])
prob_up = float(last["prob_up"])

# Handelslogik
if prob_up >= 0.56:
    signal = "YES"
    position = "100 %"
elif prob_up <= 0.44:
    signal = "YES"
    position = "SHORT"
else:
    signal = "NO_TRADE"
    position = "0 %"

# Result-Dictionary
gas_result = {
    "asset": "NATURAL GAS",
    "date": last_date,
    "close": close,
    "prob_up": prob_up,
    "signal": signal,
    "position": position,
    "signal_rules": {"long":0.56, "short":0.44},
    "strategy_lines": [
        "≥ 56 % → LONG",
        "≤ 44 % → SHORT",
        "Lev ≤ 10 | SL −20 %"
    ]
}
