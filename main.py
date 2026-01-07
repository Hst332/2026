from forecast_gold import gold_result
from forecast_silver import silver_result
from forecast_gas import gas_result
from forecast_copper import copper_result
from forecast_writer import write_daily_summary

def main():
    results = [
        gold_result(),
        silver_result(),
        gas_result(),
        copper_result(),
    ]
    write_daily_summary(results)
    print("Forecast erfolgreich erstellt!")

if __name__ == "__main__":
    main()
