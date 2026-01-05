def silver_result():
    last_date = "2026-01-05"
    close = 76.34
    prob_up = 0.5179

    strategy = [
        "≥ 0.96 → LONG",
        "0.90–0.96 → LONG 50 %",
        "Long only | Lev ≤ 15 | SL −20 %"
    ]

    signal = "YES" if prob_up >= 0.96 else "NO"

    return {
        "asset": "SILVER",
        "date": last_date,
        "close": close,
        "prob_up": prob_up,
        "signal": signal,
        "strategy_lines": strategy,
        "forecast_1_5": "-",
        "forecast_2_3w": "="
    }
