import datetime

# ---------------- 1️⃣ Makro-Regime ----------------
macro_regime = {
    "Regime": "Reflation",
    "Confidence": "niedrig",
    "Interpretation": "Wachstum und Inflation steigen gemeinsam."
}

# ---------------- 2️⃣ Markt-Forecast ----------------
market_forecast = [
    {"name": "NATURAL GAS", "date": "2026-01-02", "close": 3.62, "model_cv": "50.44% ± 1.67%", "prob_up": 53.78, "prob_down": 46.22, "signal": "NO_TRADE"},
    {"name": "OIL (BRENT/WTI)", "date": "2026-01-02", "close": 60.75, "prob_up": 47.00, "prob_down": 53.00, "signal": "NO_TRADE"},
    {"name": "GOLD", "date": "2026-01-02", "close": 4314.40, "model_cv": "0.00% ± 0.00%", "prob_up": 50.00, "prob_down": 50.00, "signal": "NO_TRADE"},
    {"name": "SILVER", "date": "2026-01-02", "close": 70.56, "model_cv": "0.00% ± 0.00%", "prob_up": 50.00, "prob_down": 50.00, "signal": "NO_TRADE"},
    {"name": "COPPER", "date": "2026-01-02", "close": 5.64, "model_cv": "0.00% ± 0.00%", "prob_up": 50.00, "prob_down": 50.00, "signal": "NO_TRADE"},
    {"name": "SP500", "date": "2026-01-02", "close": 6858.47, "model_cv": "0.00% ± 0.00%", "prob_up": 50.00, "prob_down": 50.00, "signal": "NO_TRADE"},
    {"name": "DAX", "date": "2026-01-02", "close": 24539.34, "model_cv": "0.00% ± 0.00%", "prob_up": 50.00, "prob_down": 50.00, "signal": "NO_TRADE"}
]

# ---------------- 3️⃣ Anlageklassen-Tabelle ----------------
anlageklassen = [
    {
        "name": "Öl (WTI)",
        "date": "2026-01-03",
        "1-5T": {"Steigt": 50, "Bleibt": 30, "Fällt": 20, "Einschätzung": "Handeln nur wenn >xx%"},
        "2-3W": {"Steigt": 52, "Bleibt": 28, "Fällt": 20, "Einschätzung": "Mittelfristig gestützt durch OPEC."},
        "Diff_1-5": 30,
        "Diff_2-3W": 32
    },
    {
        "name": "Kaffee (Coffee C)",
        "date": "2026-01-03",
        "1-5T": {"Steigt": 45, "Bleibt": 35, "Fällt": 20, "Einschätzung": "Saisonale Stärke, Angebotsrisiko."},
        "2-3W": {"Steigt": 50, "Bleibt": 30, "Fällt": 20, "Einschätzung": ""},
        "Diff_1-5": None,
        "Diff_2-3W": None
    }
]

# ---------------- 4️⃣ Datei schreiben ----------------
output_file = "forecast_output.txt"

with open(output_file, "w", encoding="utf-8") as f:
    # Makro-Regime
    f.write("MACRO REGIME 2026\n")
    f.write("=================\n\n")
    f.write(f"Regime: {macro_regime['Regime']}\n")
    f.write(f"Confidence: {macro_regime['Confidence']}\n\n")
    f.write("Interpretation:\n")
    f.write(f"{macro_regime['Interpretation']}\n\n")

    # Markt-Forecast
    f.write("===================================\n")
    f.write("   MARKET FORECAST – DAILY UPDATE\n")
    f.write("===================================\n")
    f.write(f"Run time (UTC): {datetime.datetime.utcnow():%Y-%m-%d %H:%M:%S} UTC\n\n")

    for market in market_forecast:
        f.write(f"--------- {market['name']} ---------\n")
        f.write(f"Data date : {market['date']}\n")
        f.write(f"Close     : {market['close']}\n")
        if "model_cv" in market:
            f.write(f"Model CV  : {market['model_cv']}\n")
        f.write(f"Prob UP   : {market['prob_up']}%\n")
        f.write(f"Prob DOWN : {market['prob_down']}%\n")
        f.write(f"Signal    : {market['signal']}\n\n")

    # Anlageklassen-Tabelle
    f.write("===================================\n")
    f.write("Anlageklasse\tDatum\t1-5T_Steigt\t1-5T_Bleibt\t1-5T_Fällt\tEinschätzung_1-5T\t2-3W_Steigt\t2-3W_Bleibt\t2-3W_Fällt\tEinschätzung_2-3W\tDiff_1-5\tDiff_2-3W\n")
    for asset in anlageklassen:
        f.write(
            f"{asset['name']}\t{asset['date']}\t"
            f"{asset['1-5T']['Steigt']}\t{asset['1-5T']['Bleibt']}\t{asset['1-5T']['Fällt']}\t{asset['1-5T']['Einschätzung']}\t"
            f"{asset['2-3W']['Steigt']}\t{asset['2-3W']['Bleibt']}\t{asset['2-3W']['Fällt']}\t{asset['2-3W']['Einschätzung']}\t"
            f"{asset['Diff_1-5'] if asset['Diff_1-5'] is not None else ''}\t{asset['Diff_2-3W'] if asset['Diff_2-3W'] is not None else ''}\n"
        )

print(f"Forecast written to {output_file}")
