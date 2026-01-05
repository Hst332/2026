from forecast_utils import forecast_rating
import metals_bundle

df = metals_bundle.load_gas()
last = df.iloc[-1]

prob_up = float(last["prob_up"])
close = float(last["Close"])
date = last.name.strftime("%Y-%m-%d")

if prob_up >= 0.56:
    signal = "LONG"
    position = "100 %"
elif prob_up <= 0.44:
    signal = "SHORT"
    position = "100 %"
else:
    signal = "NO_TRADE"
    position = "0 %"

fc_short, fc_mid = forecast_rating(prob_up)

gas_result = {
    "asset": "NATURAL GAS",
    "date": date,
    "close": close,
    "prob_up": prob_up,
    "signal": signal,
    "position": position,
    "fc_short": fc_short,
    "fc_mid": fc_mid,
    "strategy_lines": [
        "≥ 56 % → LONG",
        "≤ 44 % → SHORT",
        "Lev ≤ 10 | SL −20 %"
    ]
}
