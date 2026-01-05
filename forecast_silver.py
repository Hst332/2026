import metals_bundle
from forecast_utils import forecast_rating

df = metals_bundle.load_silver()
last = df.iloc[-1]

prob_up = float(last["prob_up"])
close = float(last["Close"])
date = last.name.strftime("%Y-%m-%d")

if prob_up >= 0.96:
    signal = "YES100"
    position = "100 %"
elif prob_up >= 0.90:
    signal = "YES50"
    position = "50 %"
else:
    signal = "NO_TRADE"
    position = "0 %"

fc_short, fc_mid = forecast_rating(prob_up)

silver_result = {
    "asset": "SILVER",
    "date": date,
    "close": close,
    "prob_up": prob_up * 100,
    "signal": signal,
    "position": position,
    "fc_short": fc_short,
    "fc_mid": fc_mid,
    "strategy_lines": [
        "≥ 0.96 → LONG",
        "0.90–0.96 → LONG 50 %",
        "Long only | Lev ≤ 15 | SL −20 %"
    ]
}
