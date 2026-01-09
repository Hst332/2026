from forecast_assets import run_all
from datetime import datetime


def main():
    print("=" * 90)
    print("MARKET FORECAST – DAILY SUMMARY")
    print("Run time (UTC):", datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 90)
    print(f"{'ASSET':<10}{'CLOSE':<18}{'SCORE':<10}{'SIGNAL':<10}{'1–5D':<8}{'2–3W'}")
    print("-" * 90)

    for r in run_all():
        print(
            f"{r['asset']:<10}"
            f"{r['close']:<18}"
            f"{r['score']:<10}"
            f"{r['signal']:<10}"
            f"{r['f_1_5']:<8}"
            f"{r['f_2_3w']}"
        )

    print("=" * 90)


if __name__ == "__main__":
    main()
