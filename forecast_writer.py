from datetime import datetime

def write_daily_summary(results, filename="forecast_output.txt"):

    def g(r, key, default=""):
        return r.get(key, default)

    with open(filename, "w", encoding="utf-8") as f:
        f.write("=" * 100 + "\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("=" * 100 + "\n")

        f.write(
            "ASSET        DATE        CLOSE        SIGNAL        "
            "FORECAST 1–5D  FORECAST 2–3W   STRATEGY\n"
        )
        f.write("=" * 100 + "\n")

        for r in results:
            f.write(
                f"{g(r,'asset'):<12}"
                f"{g(r,'date'):<12}"
                f"{g(r,'close_str'):<12}"
                f"{g(r,'signal','NO_TRADE'):<14}"
                f"{g(r,'forecast_1_5d','='):^14}"
                f"{g(r,'forecast_2_3w','='):^16}"
                f"{g(r,'strategy_lines',[''])[0]}\n"
            )

            for line in g(r, "strategy_lines", [])[1:]:
                f.write(f"{'':<89}{line}\n")

            f.write("-" * 100 + "\n")

        f.write("=" * 100 + "\n")
