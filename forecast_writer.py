from datetime import datetime

def write_daily_summary(results, filename="forecast_output.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 100 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("=" * 100 + "\n")
        f.write(
            "ASSET        DATE        CLOSE        MODEL SCORE   SIGNAL        "
            "FORECAST 1–5D  FORECAST 2–3W   STRATEGY\n"
        )
        f.write("=" * 100 + "\n")

        for r in results:
            f.write(
                f"{r['asset']:<12}"
                f"{r['date']:<12}"
                f"{r['close']:<14}"
                f"{r['model_score']:^14}"
                f"{r['signal']:<14}"
                f"{r['forecast_1_5d']:^14}"
                f"{r['forecast_2_3w']:^16}"
                f"{r['strategy_lines'][0]}\n"
            )

            for line in r["strategy_lines"][1:]:
                f.write(f"{'':<82}{line}\n")

            f.write("-" * 100 + "\n")

        f.write("=" * 100 + "\n")
