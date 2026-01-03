from forecast_energy import forecast_energy_2026
from metals_bundle import forecast_metals_2026
from macro_regime import detect_macro_regime
from regime_adjustment import adjust_metals_for_regime
from macro_output import macro_regime_output

def run():
    gas = forecast_energy_2026()
    metals = forecast_metals_2026()["metals"]

    regime = detect_macro_regime(
        gas=gas,
        copper=next(m for m in metals if m["commodity"] == "Copper"),
        gold=next(m for m in metals if m["commodity"] == "Gold")
    )

    metals = adjust_metals_for_regime(metals, regime)
    macro = macro_regime_output(regime, gas, metals)

    with open("forecast_output.txt", "w", encoding="utf-8") as f:
        f.write("MACRO REGIME 2026\n")
        f.write("=================\n\n")
        f.write(f"Regime: {macro['macro_regime']}\n")
        f.write(f"Confidence: {macro['confidence']}\n\n")
        f.write(f"Interpretation:\n{macro['interpretation']}\n")

if __name__ == "__main__":
    run()
