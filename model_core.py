import numpy as np
import pandas as pd


def model_score(df: pd.DataFrame) -> float:
    if len(df) < 70:
        return 0.50

    close = df["Close"]

    r21 = (close.iloc[-1] / close.iloc[-21]) - 1
    r63 = (close.iloc[-1] / close.iloc[-63]) - 1
    vol21 = close.pct_change().rolling(21).std().iloc[-1]

    r21_n = np.tanh(r21 * 5)
    r63_n = np.tanh(r63 * 3)
    vol_n = np.tanh(vol21 * 10)

    score = (
        0.50
        + 0.15 * r21_n
        + 0.10 * r63_n
        - 0.10 * vol_n
    )

    return float(np.clip(score, 0.30, 0.70))
