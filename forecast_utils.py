import pandas as pd

def model_score(df, days=21):
    """
    Berechnet den Model Score basierend auf der Rendite der letzten `days` Tage.
    Score liegt zwischen 0 und 1.
    """
    if len(df) < days + 1:
        return 0.5  # fallback, falls zu wenig Daten

    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-days])
    r = (last - past) / past
    score = 0.5 + max(min(r * 5, 0.5), -0.5)
    return round(score, 4)


def forecast_trend(df, days):
    """
    Berechnet den Trend (Forecast) über `days` Tage.
    Rückgabe: '+', '-', '='
    """
    if len(df) < days + 1:
        return "="

    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-days])
    r = (last - past) / past
    if r > 0.002:
        return "++"
    elif r < -0.002:
        return "--"
    else:
        return "="


def trade_signal(score):
    """
    Liefert das Handelssignal basierend auf dem Model Score.
    """
    if score >= 0.65:
        return "LONG"
    elif score <= 0.35:
        return "SHORT"
    else:
        return "NO_TRADE"
