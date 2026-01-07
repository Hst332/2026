def model_score(df):
    return float(df["prob_up"].iloc[-1])


def forecast_trend(df, days):
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-days])

    r = (last / past) - 1

    if r > 0.01:
        return "++"
    elif r > 0.002:
        return "+"
    elif r < -0.01:
        return "--"
    elif r < -0.002:
        return "-"
    else:
        return "="


def trade_signal(score):
    if score >= 0.55:
        return "LONG"
    elif score <= 0.45:
        return "SHORT"
    else:
        return "NO_TRADE"
