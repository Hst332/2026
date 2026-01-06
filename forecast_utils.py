def forecast_trend(df, days):
    # kumulierte Rendite über Zeitraum
    r = (df["Close"].iloc[-1] / df["Close"].iloc[-days] - 1)

    if r > 0.002:
        return "↑"
    elif r < -0.002:
        return "↓"
    else:
        return "="
