from datetime import datetime


def write_daily_summary(results, filename="forecast_output.txt"):
    with open(filename, "w", encoding="utf-8") as f:

        f.write("=" * 100 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("=" * 100 + "\n")

        header = (
            f"{'ASSET':<12}"
            f"{'DATE':<12}"
            f"{'CLOSE':<18}"
            f"{'MODEL SCORE':<14}"
            f"{'SIGNAL':<12}"
            f"{'FORECAST 1–5D':<15}"
            f"{'FORECAST 2–3W':<15}"
            f"STRATEGY\n"
        )
        f.write(header)
        f.write("=" * 100 + "\n")

        for r in results:
            strategy = r.get("strategy", "-")

            line = (
                f"{r['asset']:<12}"
                f"{r['date']:<12}"
                f"{r['close']:<18}"
                f"{r['model_score']:<14}"
                f"{r['signal']:<12}"
                f"{r['forecast_1_5d']:<15}"
                f"{r['forecast_2_3w']:<15}"
                f"{strategy}\n"
            )
            f.write(line)

        f.write("=" * 100 + "\n")
