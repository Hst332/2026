from datetime import datetime

def write_daily_summary(results, filename="forecast_output.txt"):

    def sig_fmt(s):
        return "TRADE" if s != "NO_TRADE" else "NO_TRADE"

    STRATEGY_COL = 60  # ab dieser Spalte läuft die Strategie

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("=" * 80 + "\n")
        f.write(
            "ASSET        DATE        CLOSE      PROB UP   SIGNAL     POSITION   STRATEGY\n"
        )
        f.write("=" * 80 + "\n")

        for r in results:
            # Kopfzeile bis POSITION
            header = (
                f"{r['asset']:<12}"
                f"{r['date']:<12}"
                f"{r['close']:<10.2f} "
                f"{r['prob_up']*100:>6.2f} %   "
                f"{sig_fmt(r['signal']):<10}"
                f"{r['position']:<10}"
            )

            # Erste Strategielinie in derselben Zeile
            first_strategy = r["strategy_lines"][0]
            f.write(
                header
                + " " * max(1, STRATEGY_COL - len(header))
                + first_strategy
                + "\n"
            )

            # Weitere Strategielinien darunter, exakt eingerückt
            for line in r["strategy_lines"][1:]:
                f.write(" " * STRATEGY_COL + line + "\n")

            f.write("-" * 80 + "\n")

        f.write("=" * 80 + "\n")
