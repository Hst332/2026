from datetime import datetime

def write_daily_summary(results, filename="forecast_output.txt"):

    def sig_fmt(s):
        return "YES" if s != "NO_TRADE" else "NO"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("=" * 80 + "\n")
        f.write(
            "ASSET        DATE        CLOSE      PROB UP   SIGNAL   POSITION   "
            "1–5D   2–3W   STRATEGY\n"
        )
        f.write("=" * 80 + "\n")

        for r in results:
            f.write(
                f"{r['asset']:<12}"
                f"{r['date']:<12}"
                f"{r['close']:<10.2f} "
                f"{r['prob_up']:<6.2f}%   "
                f"{sig_fmt(r['signal']):<8}"
                f"{r['position']:<10}"
                f"{r['fc_short']:^6}"
                f"{r['fc_mid']:^6}"
                f"{r['strategy_lines'][0]}\n"
            )

            for line in r["strategy_lines"][1:]:
                f.write(f"{'':<60}{line}\n")

            f.write("-" * 80 + "\n")

        f.write("=" * 80 + "\n")
