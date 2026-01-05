# forecast_gold.py
from datetime import datetime

def gold_result():
    # HIER nutzt du DEIN echtes df
    last_date = "2026-01-05"
    close = 4458.20
    prob_up = 0.5023

    strategy = [
        "0.53–0.55 → YES50",
        "≥ 0.55 → YES100",
        "No Short | Lev ≤ 5"
    ]

    if prob_up >= 0.55:
        signal = "YES100"
    elif prob_up >= 0.53:
        signal = "YES50"
    else:
        signal = "NO"

    return {
        "asset": "GOLD",
        "date": last_date,
        "close": close,
        "prob_up": prob_up,
        "signal": signal,
        "strategy_lines": strategy,
        "forecast_1_5": "=",
        "forecast_2_3w": "+"
    }
