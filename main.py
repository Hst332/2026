from datetime import datetime

def main():
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    with open("forecast_output.txt", "w", encoding="utf-8") as f:
        f.write("MACRO REGIME 2026\n")
        f.write("=================\n\n")

        # Klar deklarierte Logik
        regime = "Reflation"
        confidence = "niedrig"

        f.write(f"Regime: {regime}\n")
        f.write(f"Confidence: {confidence}\n\n")
        f.write("Interpretation:\n")
        f.write("Wachstum und Inflation steigen gemeinsam.\n\n")

        f.write("===================================\n")
        f.write("   MARKET FORECAST – DAILY UPDATE\n")
        f.write("===================================\n")
        f.write(f"Run time (UTC): {now}\n\n")

        assets = [
            ("NATURAL GAS", "3.62", "53.78%", "46.22%"),
            ("OIL (WTI)", "60.75", "47.0%", "53.0%"),
            ("GOLD", "4314.4", "50.0%", "50.0%"),
            ("SILVER", "70.56", "50.0%", "50.0%"),
            ("COPPER", "5.64", "50.0%", "50.0%"),
            ("SP500", "6858.47", "50.0%", "50.0%"),
            ("DAX", "24539.34", "50.0%", "50.0%"),
        ]

        for name, close, up, down in assets:
            f.write(f"--------- {name} ---------\n")
            f.write("Data date : LAST_AVAILABLE\n")
            f.write(f"Close     : {close}\n")
            f.write(f"Prob UP   : {up}\n")
            f.write(f"Prob DOWN : {down}\n")
            f.write("Signal    : NO_TRADE\n\n")

        f.write("===================================\n")
        f.write("NOTE:\n")
        f.write("All probabilities except Natural Gas are placeholders.\n")
        f.write("System is structurally ready for live data integration.\n")

    print("forecast_output.txt written successfully")

if __name__ == "__main__":
    main()
