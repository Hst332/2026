# forecast_utils.py

def model_score(df):
    """
    MODEL SCORE = normalisierte Trendstärke der letzten 20 Tage
    """
    if len(df) < 21:
        return 0.5

    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-21])

    r = (last / past) - 1

    # Clamp auf [0,1] um interpretierbar zu bleiben
    score = 0.5 + r
    return max(0.0, min(1.0, score))


def forecast_trend(df, days):
    if len(df) <= days:
        return "="

    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-days])

    r = (last / past) - 1

    if r > 0.02:
        return "++"
    if r > 0.005:
        return "+"
    if r < -0.02:
        return "--"
    if r < -0.005:
        return "-"
    return "="
