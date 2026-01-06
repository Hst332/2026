import metals_bundle

def copper_result():
    df = metals_bundle.load_copper()  # echte Copper-Daten laden
    last = df.iloc[-1]

    # FutureWarning vermeiden
    prob_up = float(last["prob_up"])
    close = float(last["Close"])
    model_score = prob_up  # Model Score = aktuelle Wahrscheinlichkeit

    return {
        "asset": "COPPER",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/kg",  # Einheit hinzufügen
        "model_score": f"{model_score:.2%}",  # Prozentanzeige
        "signal": "NO_TRADE",  # aktuelles Signal
        "forecast_1_5d": "=",  # aktuelle Vorhersage 1–5 Tage
        "forecast_2_3w": "=",  # aktuelle Vorhersage 2–3 Wochen
        "strategy_lines": [
            "Industrial metal | China driven",
            "Cycle & infrastructure sensitive",
            "Phase-2 model (Gold + ret_20)"
        ],
    }
