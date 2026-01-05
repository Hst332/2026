from forecast_writer import write_daily_summary
from forecast_gold import gold_result
from forecast_silver import silver_result
from forecast_gas import gas_result

def main():
    results = [
        gold_result,
        silver_result,
        gas_result
    ]

    write_daily_summary(results)

if __name__ == "__main__":
    main()
