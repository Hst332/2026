import metals_bundle

def gas_result():
    df = metals_bundle.load_gas()
    last = df.iloc[-1]

    prob_up = float(last["prob_up"])
    close = float(last["Close"])
    model_score = prob_up

    return {
        "asset": "NATURAL GAS",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/MMBtu",
        "model_score": f"{model_score:.2%}",
        "signal": "NO_TRADE",
        "forecast_1_5d": "=",
        "forecast_2_3w": "=",
        "strategy_lines": [
            "≥ 56 % → LONG",
            "≤ 44 % → SHORT",
            "Lev ≤ 10 | SL −20 %",
        ],
    }
