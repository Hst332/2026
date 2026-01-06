import metals_bundle

def copper_result():
    df = metals_bundle.load_copper()  # Aktuelle Copper-Daten laden
    last = df.iloc[-1]

    # ACHTUNG: float auf Series-Element korrekt, um FutureWarning zu vermeiden
    prob_up = float(last["prob_up"])
    close = float(last["Close"])

    # Model Score direkt aus prob_up, analog zu den anderen Metallen
    model_score = prob_up

    return {
        "asset": "COPPER",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/kg",
        "prob_up": f"{prob_up:.2%}",          # Aktueller Wert der Vorhersage, z.B. 53.5 %
        "signal": "NO_TRADE",
        "position": "0 %",
        "strategy_lines": [
            "Industrial metal | China driven",
            "Cycle & infrastructure sensitive",
            "Phase-2 model (Gold + ret_20)",
        ],
        "forecast_short": "=",
        "forecast_mid": "=",
        "model_score": f"{model_score:.2%}",  # Echte Model Score
    }
