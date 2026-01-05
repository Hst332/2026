# forecast_silver.py

def forecast_silver_2026(df):
    last = df.iloc[-1]

    prob = float(last["prob_up"])
    close = float(last["Close"])
    date = last.name.strftime("%Y-%m-%d")

    if prob >= 0.96:
        signal = "LONG (HIGH CONVICTION)"
    else:
        signal = "NO_TRADE"

    return {
        "date": date,
        "close": close,
        "prob_up": prob,
        "signal": signal
    }
