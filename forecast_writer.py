from datetime import datetime

# -----------------------
# Helper: Signal Mapping
# -----------------------
def signal_from_prob(prob, rules):
    """
    rules: dict with keys like:
    {
        "yes100": 0.55,
        "yes50": 0.53
    }
    """
    if prob >= rules.get("yes100", 1.1):
        return "YES100"
    elif prob >= rules.get("yes50", 1.1):
        return "YES50"
    else:
        return "NO"


def forecast_bucket(prob):
    if prob >= 0.60:
        return "++"
    elif prob >= 0.55:
        return "+"
    elif prob >= 0.45:
        return "="
    elif prob >= 0.40:
        return "-"
    else:
        return "--"


# -----------------------
# Main Writer
# -----------------------
def write_daily_summary(results, filename="forecast_output.txt"):

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 90 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("=" * 90 + "\n")

        f.write(
            "ASSET        DATE        CLOSE      PROB UP   SIGNAL   FCAST 1–5D  FCAST 2–3W  STRATEGY\n"
        )
        f.write("=" * 90 + "\n")

        for r in results:

            prob = r["prob_up"]
            signal = signal_from_prob(prob, r["signal_rules"])

            fcast_short = forecast_bucket(prob)
            fcast_mid = r.get("forecast_mid", fcast_short)

            f.write(
                f"{r['asset']:<12}"
                f"{r['date']:<12}"
                f"{r['close']:<10.2f} "
                f"{prob*100:>6.2f} %   "
                f"{signal:<7} "
                f"{fcast_short:^10} "
                f"{fcast_mid:^11} "
                f"{r['strategy_lines'][0]}\n"
            )

            for line in r["strategy_lines"][1:]:
                f.write(f"{'':<64}{line}\n")

            f.write("-" * 90 + "\n")

        f.write("=" * 90 + "\n")
