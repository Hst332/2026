# forecast_utils.py

def get_close(df, idx):
    return float(df["Close"].iloc[idx])

def model_score(df):
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-21])
    r = (last - past) / past
    score = 0.5 + max(min(r * 5.0, 0.5), -0.5)
    return round(score, 4)

def forecast_trend(df, days):
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-days])
    r = (last - past) / past
    if r > 0.02:
        return "++"
    elif r > 0:
        return "+"
    elif r < -0.02:
        return "--"
    else:
        return "-"

def trade_signal(score):
    if score >= 0.6:
        return "LONG"
    elif score <= 0.4:
        return "SHORT"
    else:
        return "NO_TRADE"
