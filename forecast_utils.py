def model_score(df):
    """
    Aktueller Modell-Score (letzte Wahrscheinlichkeit für UP)
    """
    return float(df["prob_up"].iloc[-1])


def forecast_trend(df, days):
    """
    Trend über Zeitraum (1–5 Tage / 2–3 Wochen)
    """
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-days])

    r = last / past - 1

    if r > 0.002:
        return "↑"
    elif r < -0.002:
        return "↓"
    else:
        return "="



def trade_signal(score, threshold=0.55):
    """
    Einheitliche Trade-Logik
    """
    if score >= threshold:
        return "LONG"
    else:
        return "NO_TRADE"
