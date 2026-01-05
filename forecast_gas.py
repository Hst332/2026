def gas_result():
    last_date = "2026-01-05"
    close = 3.49
    prob_up = 0.4599

    strategy = [
        "≥ 56 % → LONG",
        "≤ 44 % → SHORT",
        "Lev ≤ 10 | SL −20 %"
    ]

    signal = "NO"

    return {
        "asset": "NATURAL GAS",
        "date": last_date,
        "close": close,
        "prob_up": prob_up,
        "signal": signal,
        "strategy_lines": strategy,
        "forecast_1_5": "-",
        "forecast_2_3w": "-"
    }
