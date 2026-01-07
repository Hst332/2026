import pandas as pd

def model_score(df):
    """Berechnet Model Score basierend auf letzter Preisänderung."""
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-21])  # 21 Handelstage ~ 1 Monat
    r = (last - past) / past
    score = 0.5 + max(min(r * 5, 0.5), -0.5)
    return score

def forecast_trend(df, days=5):
    """Forecast Trend: '++', '+', '=', '-', '--'"""
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-days])
    r = (last - past) / past
    if r > 0.02:
        return "++"
    elif r > 0.005:
        return "+"
    elif r < -0.02:
        return "--"
    elif r < -0.005:
        return "-"
    else:
        return "="

def trade_signal(score):
    """Signal basierend auf Model Score"""
    if score > 0.65:
        return "LONG"
    elif score < 0.35:
        return "SHORT"
    else:
        return "NO_TRADE"
