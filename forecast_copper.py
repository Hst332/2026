import metals_bundle

def copper_result():
    df = metals_bundle.load_copper()
    last = df.iloc[-1]

    prob_up = float(last["prob_up"])
    close = float(last["Close"])
    model_score = prob_up

    return {
        "asset": "COPPER",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/kg",
        "model_score": f"{model_score:.2%}",
        "signal": "NO_TRADE",
        "forecast_1_5d": "=",
        "forecast_2_3w": "=",
        "strategy_lines": [
            "Industrial metal | China driven",
            "Cycle & infrastructure sensitive",
            "Phase-2 model (Gold + ret_20)",
        ],
    }
