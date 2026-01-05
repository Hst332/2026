from forecast_utils import forecast_rating
import metals_bundle

df = metals_bundle.load_gold()
last = df.iloc[-1]

prob_up = float(last["prob_up"])
close = float(last["Close"])
date = last.name.strftime("%Y-%m-%d")

if prob_up >= 0.55:
    signal = "YES100"
    position = "100 %"
elif prob_up >= 0.53:
    signal = "YES50"
    position = "50 %"
else:
    signal = "NO_TRADE"
    position = "0 %"

fc_short, fc_mid = forecast_rating(prob_up)

gold_result = {
    "asset": "GOLD",
    "date": date,
    "close": close,
    "prob_up": prob_up,
    "signal": signal,
    "position": position,
    "fc_short": fc_short,
    "fc_mid": fc_mid,
    "strategy_lines": [
        "0.53–0.55 → YES50",
        "≥ 0.55 → YES100",
        "No Short | Lev ≤ 5"
    ]
}
