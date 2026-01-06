import pandas as pd
import metals_bundle  # Bestehendes Modul für Gold, Silber, Gas etc.

def load_copper():
    """
    Lädt Copper-Daten aus CSV oder aus metals_bundle.
    Erwartet Spalten: 'Close', 'prob_up'
    """
    # Variante 1: CSV-Datei (falls vorhanden)
    try:
        df = pd.read_csv("data/copper.csv", index_col=0, parse_dates=True)
        return df
    except FileNotFoundError:
        pass  # CSV existiert nicht, probiere metals_bundle

    # Variante 2: metals_bundle, falls Funktion existiert
    if hasattr(metals_bundle, "load_all_metals"):
        all_metals = metals_bundle.load_all_metals()
        if "COPPER" in all_metals:
            return all_metals["COPPER"]

    raise ValueError("Copper-Daten konnten nicht gefunden werden. Bitte CSV oder metals_bundle prüfen.")


def copper_result():
    df = load_copper()
    last = df.iloc[-1]

    # float-Umwandlung wie empfohlen (float(ser.iloc[0]))
    prob_up = float(last["prob_up"])
    close = float(last["Close"])
    model_score = prob_up  # für MODEL SCORE Spalte

    return {
        "asset": "COPPER",
        "date": last.name.strftime("%Y-%m-%d"),
        "close": f"{close:.2f} USD/kg",        # formatiert wie bei dir gewünscht
        "model_score": f"{model_score:.2%}",   # echte Wahrscheinlichkeit
        "signal": "NO_TRADE",
        "forecast_1_5d": "=",
        "forecast_2_3w": "=",
        "strategy_lines": [
            "Industrial metal | China driven",
            "Cycle & infrastructure sensitive",
            "Phase-2 model (Gold + ret_20)"
        ],
    }
