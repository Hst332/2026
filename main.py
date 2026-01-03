from forecast_energy import forecast_energy_2026
from metals_bundle import forecast_metals_2026 
from macro_regime import detect_macro_regime
from regime_adjustment import adjust_metals_for_regime
from macro_output import macro_regime_output

def run_forecast():
    # Energie (Gas, Öl, etc.)
    energy = forecast_energy_2026()

    # Metalle
    metals_data = forecast_metals_2026()
    metals = metals_data["metals"]

    # Makro-Regime erkennen
    regime = detect_macro_regime(
        gas=energy,
        copper=next(m for m in metals if m["commodity"] == "Copper"),
        gold=next(m for m in metals if m["commodity"] == "Gold")
    )

    # Metalle an Makro-Regime anpassen
    metals = adjust_metals_for_regime(metals, regime)

    # Zusammenfassung erstellen
    macro = macro_regime_output(regime, energy, metals)

    # Forecast in Datei schreiben
    output_file = "forecast_output.txt"  # relative Pfadangabe
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("FORECAST 2026\n")
        f.write("=================\n\n")
        f.write("=== MACRO REGIME ===\n")
        f.write(f"Regime: {macro['macro_regime']}\n")
        f.write(f"Confidence: {macro['confidence']}\n\n")
        f.write(f"Interpretation:\n{macro['interpretation']}\n\n")

        f.write("=== ENERGY FORECAST ===\n")
        for k, v in energy.items():
            f.write(f"{k}: {v}\n")
        f.write("\n")

        f.write("=== METALS FORECAST ===\n")
        for metal in metals:
            f.write(f"{metal['commodity']}: {metal['forecast']}\n")

    print(f"Forecast written to {output_file}")

if __name__ == "__main__":
    run_forecast()
