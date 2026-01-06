import yfinance as yf
from datetime import datetime

def copper_result():
    # Copper Futures (HG=F) in USD/lb
    df = yf.download("HG=F", period="60d", progress=False)

    last = df.iloc[-1]
    date = last.name.strftime("%Y-%m-%d")

    # Preis von USD/lb → USD/kg
    price_lb = float(last["Close"])
    price_kg = price_lb * 2.20462

    return {
        "asset": "COPPER",
        "date": date,
        "close_str": f"{price_kg:.2f} USD/kg",
        "signal": "NO_TRADE",
        "forecast_1_5d": "=",
        "forecast_2_3w": "=",
        "strategy_lines": [
            "0.54–0.56 → LONG ",
            "No Short; only Long",
        ],
    }
