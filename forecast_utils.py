# forecast_utils.py

def model_score(df):
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-21])
    r = (last - past) / past

    score = 0.5 + max(min(r * 5, 0.5), -0.5)
    return round(score * 100, 2)


def forecast_trend(df, days):
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-days])
    r = (last - past) / past

    if r > 0.01:
        return "++"
    elif r < -0.01:
        return "--"
    else:
        return "+"


def trade_signal(score):
    if score >= 70:
        return "LONG"
    elif score <= 30:
        return "SHORT"
    else:
        return "NO_TRADE"
