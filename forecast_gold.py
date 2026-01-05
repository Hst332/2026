from datetime import datetime
import metals_bundle

def forecast_gold():
    df = metals_bundle.load_gold()
    last = df.iloc[-1]

    date = last.name.strftime("%Y-%m-%d")
    close = round(last["Close"], 2)
    prob = float(last["prob_up"])

    if prob >= 0.55:
        signal = "LONG"
        size = "100 %"
    elif prob >= 0.53:
        signal = "LONG (partial)"
        size = "50 %"
    else:
        signal = "NO_TRADE"
        size = "0 %"

    return (
        "--------- GOLD ---------\n"
        f"Data date : {date}\n"
        f"Close     : {close}\n"
        f"Prob UP   : {prob:.2%}\n"
        "Strategie:\n"
        "0.53–0.55 → 50 % Position\n"
        "≥ 0.55 → 100 % Position\n"
        "Kein Short | Max Hebel 5\n"
        f"Signal    : {signal}\n"
        f"Position  : {size}\n\n"
    )
