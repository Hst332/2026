#!/usr/bin/env python3
"""
CODE B – SILVER BACKTEST

Automatisch prüft, ob Prob_UP >= 54% oder 56% sinnvoll ist.
Output: console + CSV
"""

import pandas as pd
import numpy as np
from datetime import datetime
import yfinance as yf
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import TimeSeriesSplit

# =======================
# CONFIG
# =======================
SILVER_SYMBOL = "SI=F"
START_DATE = "2010-01-01"
OUT_CSV = "silver_backtest_results.csv"
FEATURES = ["trend_5", "trend_20", "vol_10"]  # ggf. erweitern
THRESHOLDS = [0.54, 0.56]

# =======================
# DATEN LADEN
# =======================
def load_silver():
    df = yf.download(SILVER_SYMBOL, start=START_DATE, progress=False)
    df = df[["Close"]].rename(columns={"Close":"Silver_Close"})
    df.dropna(inplace=True)
    return df

# =======================
# FEATURES
# =======================
def build_features(df):
    df = df.copy()
    df["ret"] = df["Silver_Close"].pct_change()
    df["trend_5"] = df["Silver_Close"].pct_change(5)
    df["trend_20"] = df["Silver_Close"].pct_change(20)
    df["vol_10"] = df["ret"].rolling(10).std()
    df.dropna(inplace=True)
    df["Target"] = (df["ret"].shift(-1) > 0).astype(int)
    return df

# =======================
# BACKTEST
# =======================
def backtest(df, threshold):
    trades = []

    for _, row in df.iterrows():
        # 🔒 erzwingt Skalar (kein Series-Fehler mehr)
        prob = float(row["prob_up"])
        target = int(row["Target"])

        # Signal-Logik
        if prob >= threshold:
            signal = 1   # LONG
        elif prob <= 1 - threshold:
            signal = -1  # SHORT
        else:
            continue

        # Treffer-Logik (1-Tages-Forecast)
        if (signal == 1 and target == 1) or (signal == -1 and target == 0):
            ret = 1
        else:
            ret = -1

        trades.append(ret)

    # Keine Trades → sauber abbrechen
    if len(trades) == 0:
        return {
            "threshold": threshold,
            "accuracy": None,
            "profit": 0,
            "n_trades": 0
        }

    trades = np.array(trades)

    return {
        "threshold": threshold,
        "accuracy": float(np.mean(trades > 0)),
        "profit": int(np.sum(trades)),
        "n_trades": int(len(trades))
    }

# =======================
# MAIN
# =======================
def main():
    print("[START] Silver backtest")

    # -----------------------
    # Daten laden
    # -----------------------
    df = load_silver()

    if df is None or len(df) == 0:
        print("[ERROR] No silver data loaded")
        return

    # -----------------------
    # Schwellen testen
    # -----------------------
    thresholds = [0.52, 0.54, 0.56, 0.58]
    results = []

    for th in thresholds:
        res = backtest(df, th)
        results.append(res)

    # -----------------------
    # Ergebnisse anzeigen
    # -----------------------
    print("\n=== SILVER BACKTEST RESULTS ===")
    for r in results:
        print(
            f"TH={r['threshold']:.2f} | "
            f"Trades={r['n_trades']} | "
            f"Accuracy={r['accuracy']} | "
            f"Profit={r['profit']}"
        )

    # -----------------------
    # Ergebnisse speichern
    # -----------------------
    out = pd.DataFrame(results)
    out.to_csv("silver_backtest_results.csv", index=False)

    print("\n[OK] silver_backtest_results.csv written")

if __name__ == "__main__":
    main()
