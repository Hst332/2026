import metals_bundle

def silver_result():
    df = metals_bundle.load_silver()
    last = df.iloc[-1]

    prob_up = float(last["prob_up"])
    close = float(last["Close"])
    model_score = prob_up

    return {
        "asset": "SILVER",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/oz",
        "model_score": f"{model_score:.2%}",
        "signal": "NO_TRADE",
        "forecast_1_5d": "=",
        "forecast_2_3w": "=",
        "strategy_lines": [
            "≥ 0.96 → LONG",
            "0.90–0.96 → LONG 50 %",
            "Long only | Lev ≤ 15 | SL −20 %",
        ],
    }
