def model_score(df):
    """
    Simple momentum-based score (0–1)
    """
    last = df["Close"].iloc[-1]
    past = df["Close"].iloc[-21]
    r = (last - past) / past

    # normalize to 0–1
    score = 0.5 + max(min(r * 5, 0.5), -0.5)
    return float(score)


def forecast_trend(df, days):
    last = df["Close"].iloc[-1]
    past = df["Close"].iloc[-days]
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
        return "0"


def trade_signal(score):
    if score >= 0.60:
        return "LONG"
    elif score <= 0.40:
        return "SHORT"
    else:
        return "NO_TRADE"
