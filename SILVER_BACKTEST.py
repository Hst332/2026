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
    for i, row in df.iterrows():
        signal = None
        if row['prob_up'] >= threshold:
            signal = 1  # LONG
        elif row['prob_up'] <= 1-threshold:
            signal = -1  # SHORT
        else:
            continue
        # Profit: +1 für Treffer, -1 für Fehlsignal
        ret = 1 if (signal == 1 and row["Target"]==1) or (signal==-1 and row["Target"]==0) else -1
        trades.append(ret)
    trades = np.array(trades)
    if len(trades) == 0:
        return {"threshold": threshold, "accuracy": None, "profit": None, "n_trades":0}
    accuracy = np.mean(trades>0)
    profit = np.sum(trades)
    return {"threshold": threshold, "accuracy": accuracy, "profit": profit, "n_trades": len(trades)}

# =======================
# MAIN
# =======================
def main():
    df = load_silver()
    df = build_features(df)

    # Modell
    X = df[FEATURES]
    y = df["Target"]
    model = LogisticRegression(max_iter=200, class_weight="balanced")
    model.fit(X, y)
    df["prob_up"] = model.predict_proba(X)[:,1]

    results = []
    for th in THRESHOLDS:
        res = backtest(df, th)
        results.append(res)
        print(f"Threshold {th*100:.0f}% | Accuracy: {res['accuracy']*100 if res['accuracy'] else 'N/A'}% | "
              f"Profit: {res['profit']} | Trades: {res['n_trades']}")

    # Speichern
    pd.DataFrame(results).to_csv(OUT_CSV, index=False)
    print(f"\n[OK] Backtest abgeschlossen. Ergebnisse in {OUT_CSV}")

if __name__ == "__main__":
    main()
