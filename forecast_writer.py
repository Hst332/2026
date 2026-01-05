from datetime import datetime

def write_daily_summary(results, filename="forecast_output.txt"):
    """Schreibt die tägliche Forecast-Tabelle ins txt File"""
    def sig_fmt(s):
        return "YES" if s != "NO_TRADE" else "NO_TRADE"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("="*80 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("="*80 + "\n")
        f.write("ASSET        DATE        CLOSE      PROB UP   SIGNAL     POSITION   STRATEGY\n")
        f.write("="*80 + "\n")

        for r in results:
            # Erste Zeile inkl. erstem Strategy-Line
            f.write(
                f"{r['asset']:<12}"
                f"{r['date']:<12}"
                f"{r['close']:<10.2f} "
                f"{r['prob_up']:<6.2f}%   "
                f"{sig_fmt(r['signal']):<10}"
                f"{r['position']:<10}"
                f"{r['strategy_lines'][0]}\n"
            )
            # Rest der Strategy-Lines untereinander, eingerückt
            for line in r['strategy_lines'][1:]:
                f.write(f"{'':<52}{line}\n")

            f.write("-"*80 + "\n")
        f.write("="*80 + "\n")
