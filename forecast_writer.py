# forecast_writer.py

from datetime import datetime

def write_daily_summary(results):
    print("=" * 100)
    print("MARKET FORECAST – DAILY SUMMARY")
    print(f"Run time (UTC): {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 100)
    print(
        f"{'ASSET':<12}{'DATE':<12}{'CLOSE':<18}"
        f"{'MODEL SCORE':<14}{'SIGNAL':<12}"
        f"{'FORECAST 1–5D':<15}{'FORECAST 2–3W':<15}"
        f"STRATEGY"
    )
    print("=" * 100)

    for r in results:
        print(
            f"{r['asset']:<12}"
            f"{r['date']:<12}"
            f"{r['close']:<18}"
            f"{r['model_score']:<14}"
            f"{r['signal']:<12}"
            f"{r['forecast_1_5d']:<15}"
            f"{r['forecast_2_3w']:<15}"
            f"{r['strategy']}"
        )

    print("=" * 100)
