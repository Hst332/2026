# =======================
# GOLD TRADING SIGNAL
# =======================

def gold_trading_signal(df):
    last_row = df.iloc[-1]

    date = last_row.name.strftime("%Y-%m-%d")
    close = round(float(last_row["Close"]), 1)
    prob = float(last_row["prob_up"])

    # Signal-Logik
    if prob >= 0.55:
        signal = "LONG (100 % Position)"
    elif prob >= 0.53:
        signal = "LONG (50 % Position)"
    else:
        signal = "NO_TRADE"

    # Ausgabe
    print("\n--------- GOLD ---------")
    print(f"Data date : {date}")
    print(f"Close     : {close}")
    print(f"Prob UP   : {prob*100:.1f}%\n")

    print("Handelsstrategie:")
    print("0.53–0.55 Prob Up → 50 % Positionsgröße")
    print("≥ 0.55           → 100 % Positionsgröße")
    print("Kein Short | Max. Hebel 5\n")

    print(f"Signal    : {signal}")

    return {
        "date": date,
        "close": close,
        "prob_up": prob,
        "signal": signal
    }


# =======================
# CALL SIGNAL
# =======================
gold_signal = gold_trading_signal(df)
