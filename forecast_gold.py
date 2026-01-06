import metals_bundle

def gold_result():
    df = metals_bundle.load_gold()
    last = df.iloc[-1]

    prob_up = float(last["prob_up"])
    close = float(last["Close"])
    model_score = prob_up  # für die Spalte MODEL SCORE

    return {
        "asset": "GOLD",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/oz",
        "model_score": f"{model_score:.2%}",
        "signal": "NO_TRADE",
        "forecast_1_5d": "=",
        "forecast_2_3w": "=",
        "strategy_lines": [
            "0.53–0.55 → YES50",
            "≥ 0.55 → YES100",
            "No Short | Lev ≤ 5",
        ],
    }
