import metals_bundle

df = metals_bundle.load_gold()

last = df.iloc[-1]

prob_up = float(last["prob_up"])
close = float(last["Close"])
date = last.name.strftime("%Y-%m-%d")

# Strategie
if prob_up >= 0.55:
    signal = "LONG"
    position = "100 %"
elif prob_up >= 0.53:
    signal = "LONG"
    position = "50 %"
else:
    signal = "NO_TRADE"
    position = "0 %"

gold_result = {
    "asset": "GOLD",
    "date": date,
    "close": close,
    "prob_up": prob_up,
    "signal": signal,
    "position": position,
    "strategy_lines": [
        "0.53–0.55 → 50 %",
        "≥ 0.55 → 100 %",
        "No Short | Lev ≤ 5"
    ]
}
