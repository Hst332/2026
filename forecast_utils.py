def forecast_trend(df, days: int) -> str:
    if len(df) < days + 1:
        return "="

    last = df["Close"].iloc[-1]
    past = df["Close"].iloc[-days]
    r = (last / past) - 1

    if r > 0.01:
        return "++"
    if r > 0.003:
        return "+"
    if r < -0.01:
        return "--"
    if r < -0.003:
        return "-"
    return "="


def trade_signal(score: float) -> str:
    if score >= 0.60:
        return "LONG"
    if score <= 0.40:
        return "SHORT"
    return "NO_TRADE"
