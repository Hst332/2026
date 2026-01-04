# =======================
# SILVER_BACKTEST.PY
# =======================

import pandas as pd
import numpy as np
import yfinance as yf
import csv
from datetime import datetime

SILVER_SYMBOL = "SI=F"  # Silber-Future
START_DATE = "2023-01-01"
THRESHOLDS = [0.59, 0.60, 0.61, 0.62, 0.75, 0.85, 0.95]  # Testschwellen

# =======================
# DATEN LADEN
# =======================
def load_silver():
    df = yf.download(SILVER_SYMBOL, start=START_DATE, progress=False)
    if df.empty:
        raise ValueError("Keine Daten von Yahoo Finance")
    df = df[['Close']].copy()
    df['Return'] = df['Close'].pct_change().shift(-1)  # nächste Periode
    df['Target'] = (df['Return'] > 0).astype(int)
    df.dropna(inplace=True)
    return df

# =======================
# FEATURES ERSTELLEN
# =======================
def build_features(df):
    # Dummy: zufällige Wahrscheinlichkeit, dass Silber steigt
    if 'prob_up' not in df.columns:
        df['prob_up'] = np.random.rand(len(df))
    return df

# =======================
# BACKTEST
# =======================
def backtest(df, threshold):
    trades = []

    for i, row in df.iterrows():
        prob = float(row['prob_up'])  # immer einzelne Zahl
        target = float(row['Target']) # hier war der Fehler

        signal = None
        if prob >= threshold:
            signal = 1  # LONG
        elif prob <= 1 - threshold:
            signal = -1  # SHORT
        else:
            continue

        ret = 1 if (signal == 1 and target == 1) or (signal == -1 and target == 0) else -1
        trades.append(ret)

    trades = np.array(trades)
    if len(trades) == 0:
        return {"threshold": threshold, "accuracy": None, "profit": None, "n_trades": 0}

    accuracy = np.mean(trades > 0)
    profit = np.sum(trades)
    return {"threshold": threshold, "accuracy": accuracy, "profit": profit, "n_trades": len(trades)}

# =======================
# MAIN
# =======================
def main():
    print("[START] Silver backtest")
    df = load_silver()
    df = build_features(df)

    results = []

    for th in THRESHOLDS:
        res = backtest(df, th)
        results.append(res)
        trades = res['n_trades']
        acc = f"{res['accuracy']*100:.2f}%" if res['accuracy'] is not None else "N/A"
        prof = res['profit'] if res['profit'] is not None else "N/A"
        print(f"TH={th:.2f} | Trades={trades} | Accuracy={acc} | Profit={prof}")

    # CSV schreiben
    csv_file = "silver_backtest_results.csv"
    with open(csv_file, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["threshold", "n_trades", "accuracy", "profit"])
        writer.writeheader()
        for r in results:
            writer.writerow({
                "threshold": r["threshold"],
                "n_trades": r["n_trades"],
                "accuracy": r["accuracy"],
                "profit": r["profit"]
            })
    print(f"\n[OK] {csv_file} written")

# =======================
# RUN
# =======================
if __name__ == "__main__":
    main()
