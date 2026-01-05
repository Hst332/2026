from datetime import datetime

def write_daily_summary(results, filename="forecast_output.txt"):
    """
    results = Liste von Dicts mit Keys:
    asset, date, close, prob_up, signal, position, strategy_lines (Liste)
    """

    def fmt_signal(sig):
        return ">> TRADE <<" if sig != "NO_TRADE" else "-- NO TRADE --"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("=" * 80 + "\n")
        f.write(
            "ASSET        DATE        CLOSE      PROB UP    SIGNAL           "
            "POSITION   STRATEGY (RULES)\n"
        )
        f.write("=" * 80 + "\n")

        for r in results:
            f.write(
                f"{r['asset']:<12}"
                f"{r['date']:<12}"
                f"{r['close']:<10.2f}  "
                f"{r['prob_up']*100:>6.2f} %   "
                f"{fmt_signal(r['signal']):<15} "
                f"{r['position']:<9} "
                f"{r['strategy_lines'][0]}\n"
            )

            # weitere Strategieregeln (max. 1–2 Zeilen)
            for line in r['strategy_lines'][1:]:
                f.write(
                    f"{'':<52}{line}\n"
                )

            f.write("-" * 80 + "\n")

        f.write("=" * 80 + "\n")
