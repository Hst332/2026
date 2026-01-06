# =======================
# COPPER FORECAST
# =======================

import yfinance as yf
from datetime import datetime

# =======================
# CONFIG
# =======================
SYMBOL = "HG=F"              # Copper Futures (USD/lb)
LB_TO_KG = 2.2046226218

# Phase-2 Kupfer Levels (USD/kg)
LEVEL_LONG_50 = 11.0
LEVEL_LONG_75 = 11.6
LEVEL_LONG_100 = 12.0

# =======================
# DATA
# =======================
def load_copper_price():
    df = yf.download(SYMBOL, period="5d", interval="1d", progress=False)
    close_lb = float(df["Close"].iloc[-1])
    close_kg = close_lb * LB_TO_KG
    return round(close_kg, 2)


# =======================
# SIGNAL LOGIC
# =======================
def copper_signal(price):
    if price >= LEVEL_LONG_100:
        return "LONG", "100 %"
    elif price >= LEVEL_LONG_75:
        return "LONG", "75 %"
    elif price >= LEVEL_LONG_50:
        return "LONG", "50 %"
    else:
        return "NO_TRADE", "0 %"

# =======================
# RESULT (EXPORT)
# =======================

def copper_result():
    price = load_copper_price()
    signal, position = copper_signal(price)

        return {
        "asset": "COPPER",
        "date": last_date,
        "close_str": f"{price_usd_kg:.2f} USD/kg",
        "signal": "NO_TRADE",
        "forecast_1_5d": "=",
        "forecast_2_3w": "=",
        "strategy_lines": [
            "Industrial metal | China driven",
            "Macro & cycle sensitive",
            "Phase-1 model (Gold-features)"
        ]
    }
