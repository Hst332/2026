# forecast_writer.py
from datetime import datetime

def write_daily_summary(results, filename="forecast_output.txt"):

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("=" * 80 + "\n")
        f.write(
            "ASSET        DATE        CLOSE      PROB UP   SIGNAL    STRATEGY\n"
        )
        f.write("=" * 80 + "\n")

        for r in results:
            f.write(
                f"{r['asset']:<12}"
                f"{r['date']:<12}"
                f"{r['close']:<10.2f} "
                f"{r['prob_up']*100:>6.2f} %   "
                f"{r['signal']:<8} "
                f"{r['strategy_lines'][0]}\n"
            )

            # Strategie mehrzeilig, aber in derselben Spalte
            for line in r["strategy_lines"][1:]:
                f.write(f"{'':<52}{line}\n")

            # Forecast-Horizonte
            f.write(
                f"{'':<52}"
                f"Forecast 1–5d : {r['forecast_1_5']} | "
                f"Forecast 2–3w : {r['forecast_2_3w']}\n"
            )

            f.write("-" * 80 + "\n")

        f.write("=" * 80 + "\n")
