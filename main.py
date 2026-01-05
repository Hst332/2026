from forecast_writer import init_forecast_file, finalize_forecast
from forecast_gold import forecast_gold
from forecast_silver import forecast_silver
from forecast_energy import forecast_gas

def main():
    init_forecast_file()

    forecast_gold()
    forecast_silver()

    # Gas – Beispielwerte aus Modell
    forecast_gas(
        date="2026-01-05",
        close=3.51,
        prob_up=0.4599
    )

    finalize_forecast()
    print("[OK] forecast_output.txt written")

if __name__ == "__main__":
    main()
