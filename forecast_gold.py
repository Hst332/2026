import pandas as pd
from datetime import datetime

# -------------------------------------------------
# Trading-Regeln Gold
# -------------------------------------------------
def gold_trading_signal(df):
    last = df.iloc[-1]
    prob = float(last["prob_up"])
    close = float(last["Close"])
    date = last.name.strftime("%Y-%m-%d")

    if prob >= 0.55:
        signal = "LONG (100 %)"
    elif prob >= 0.53:
        signal = "LONG (50 %)"
    else:
        signal = "NO_TRADE"

    return {
        "date": date,
        "close": close,
        "prob_up": prob,
        "signal": signal
    }


# -------------------------------------------------
# OPTIONAL: nur wenn Datei DIREKT gestartet wird
# -------------------------------------------------
if __name__ == "__main__":
    print("forecast_gold.py ist ein Modul – kein Direktlauf vorgesehen")
