import metals_bundle

def forecast_gas():
    df = metals_bundle.load_gas()
    last = df.iloc[-1]

    date = last.name.strftime("%Y-%m-%d")
    close = round(last["Close"], 2)
    prob = float(last["prob_up"])

    if prob >= 0.56:
        signal = "LONG"
    elif prob <= 0.44:
        signal = "SHORT"
    else:
        signal = "NO_TRADE"

    return (
        "--------- NATURAL GAS ---------\n"
        f"Data date : {date}\n"
        f"Close     : {close}\n"
        f"Prob UP   : {prob:.2%}\n"
        "Regeln:\n"
        "≥ 56 % → LONG\n"
        "≤ 44 % → SHORT\n"
        "Max Hebel 10 | SL -20 %\n"
        f"Signal    : {signal}\n\n"
    )
