import metals_bundle

df = metals_bundle.load_silver()

last = df.iloc[-1]

prob_up = float(last["prob_up"])
close = float(last["Close"])
date = last.name.strftime("%Y-%m-%d")

if prob_up >= 0.96:
    signal = "LONG"
    position = "100 %"
else:
    signal = "NO_TRADE"
    position = "0 %"

silver_result = {
    "asset": "SILVER",
    "date": date,
    "close": close,
    "prob_up": prob_up,
    "signal": signal,
    "position": position,
    "strategy_lines": [
        "≥ 0.96 → LONG",
        "Long only",
        "Lev ≤ 15 | SL −20 %"
    ]
}
