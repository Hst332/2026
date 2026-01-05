# forecast_writer.py
from datetime import datetime

OUT_FILE = "forecast_output.txt"

def _fmt_float(x, digits=2):
    try:
        return f"{float(x):.{digits}f}"
    except Exception:
        return "NA"

def _fmt_pct(x, digits=2):
    try:
        return f"{float(x)*100:.{digits}f} %"
    except Exception:
        return "NA"

def init_forecast_file():
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write("================================================================================\n")
        f.write("MARKET FORECAST – DAILY SUMMARY\n")
        f.write(f"Run time (UTC): {datetime.utcnow():%Y-%m-%d %H:%M:%S}\n")
        f.write("================================================================================\n")
        f.write(
            "ASSET        DATE        CLOSE      PROB UP   SIGNAL     POSITION   STRATEGY\n"
        )
        f.write("================================================================================\n")

def write_asset_row(
    asset,
    date,
    close,
    prob_up,
    signal,
    position,
    strategy_lines
):
    with open(OUT_FILE, "a", encoding="utf-8") as f:
        f.write(
            f"{asset:<12} {date:<10} "
            f"{_fmt_float(close,2):<10} "
            f"{_fmt_pct(prob_up):<9} "
            f"{signal:<10} "
            f"{position:<9} "
            f"{strategy_lines[0]}\n"
        )
        for line in strategy_lines[1:]:
            f.write(f"{'':<63}{line}\n")
        f.write("-" * 80 + "\n")

def finalize_forecast():
    with open(OUT_FILE, "a", encoding="utf-8") as f:
        f.write("=" * 80 + "\n")
