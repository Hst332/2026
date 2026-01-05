from forecast_gold import forecast_gold
from forecast_silver import forecast_silver
from forecast_energy import forecast_gas

OUTPUT_FILE = "forecast_output.txt"

def main():
    with open(OUTPUT_FILE, "w") as f:
        f.write(forecast_gold())
        f.write(forecast_silver())
        f.write(forecast_gas())

    print("[OK] forecast_output.txt updated")

if __name__ == "__main__":
    main()
