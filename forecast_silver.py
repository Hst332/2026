import metals_bundle

def silver_result():
    df = metals_bundle.load_silver()
    last = df.iloc[-1]

    prob_up = float(last["prob_up"])
    close = float(last["Close"])

    model_score = prob_up  # NEU: für die Spalte MODEL SCORE
    
    return {
        "asset": "SILVER",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": close,
        "model_score": f"{model_score:.2%}",
        "signal": "NO_TRADE",
        "position": "0 %",
        "strategy_lines": [
            "≥ 0.96 → LONG",
            "0.90–0.96 → LONG 50 %",
            "Long only | Lev ≤ 15 | SL −20 %",
        ],
        "forecast_short": "=",
        "forecast_mid": "=",
    }
