import metals_bundle

def gold_result():
    df = metals_bundle.load_gold()
    last = df.iloc[-1]

    prob_up = float(last["prob_up"])
    close = float(last["Close"])

    return {
        "asset": "GOLD",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": close,
        "prob_up": prob_up,
        "signal": "NO_TRADE",
        "position": "0 %",
        "strategy_lines": [
            "0.53–0.55 → YES50",
            "≥ 0.55 → YES100",
            "No Short | Lev ≤ 5",
        ],
        "forecast_short": "=",
        "forecast_mid": "=",
    }
