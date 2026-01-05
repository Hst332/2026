import metals_bundle

def gold_result():
    df = metals_bundle.load_gold()
    last = df.iloc[-1]

    prob_up = float(last["prob_up"])
    close = float(last["Close"])
    date = last.name.strftime("%Y-%m-%d")

    if prob_up >= 0.55:
        signal = "YES100"
    elif prob_up >= 0.53:
        signal = "YES50"
    else:
        signal = "NO"

    return {
        "asset": "GOLD",
        "date": date,
        "close": close,
        "prob_up": prob_up,
        "signal": signal,
        "strategy_lines": [
            "0.53–0.55 → YES50",
            "≥ 0.55 → YES100",
            "No Short | Lev ≤ 5"
        ],
        "forecast_1_5": "=",
        "forecast_2_3w": "+"
    }
