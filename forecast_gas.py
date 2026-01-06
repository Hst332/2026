import metals_bundle

def gas_result():
    df = metals_bundle.load_gas()
    last = df.iloc[-1]

    prob_up = float(last["prob_up"])
    close = float(last["Close"])

    model_score = prob_up  # NEU: für die Spalte MODEL SCORE
    
   
    return {
        "asset": "NATURAL GAS",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": close,
        "prob_up": prob_up,
        "model_score": f"{model_score:.2%}",
        "signal": "NO_TRADE",
        "position": "0 %",
        "strategy_lines": [
            "≥ 56 % → LONG",
            "≤ 44 % → SHORT",
            "Lev ≤ 10 | SL −20 %",
        ],
        "forecast_short": "=",
        "forecast_mid": "=",
    }
