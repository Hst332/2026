def _close_series(df):
    """
    Ensure Close is always a 1D float Series
    """
    close = df["Close"]

    # yfinance MultiIndex fallback
    if hasattr(close, "columns"):
        close = close.iloc[:, 0]

    return close.astype(float)


def model_score(df):
    close = _close_series(df)

    if len(close) < 21:
        return 0.5

    last = close.iloc[-1]
    past = close.iloc[-21]

    r = (last - past) / past

    # normalize to 0–1
    score = 0.5 + max(min(float(r) * 5, 0.5), -0.5)
    return float(score)


def forecast_trend(df, days):
    close = _close_series(df)

    if len(close) < days:
        return "0"

    last = close.iloc[-1]
    past = close.iloc[-days]

    r = (last - past) / past
    r = float(r)

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
