import metals_bundle

def forecast_silver():
    df = metals_bundle.load_silver()
    last = df.iloc[-1]

    date = last.name.strftime("%Y-%m-%d")
    close = round(last["Close"], 2)
    prob = float(last["prob_up"])

    if prob >= 0.96:
        signal = "LONG"
        size = "100 %"
    else:
        signal = "NO_TRADE"
        size = "0 %"

    return (
        "--------- SILVER ---------\n"
        f"Data date : {date}\n"
        f"Close     : {close}\n"
        f"Prob UP   : {prob:.2%}\n"
        "Strategie:\n"
        "≥ 0.96 → LONG\n"
        "LONG only | Max Hebel 15\n"
        "Stop-Loss -20 %\n"
        f"Signal    : {signal}\n"
        f"Position  : {size}\n\n"
    )
