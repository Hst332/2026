def model_score(df):
    last = float(df["Close"].iloc[-1])
    past = float(df["Close"].iloc[-21])

    r = (last - past) / past

    score = 0.5 + max(min(r * 5, 0.5), -0.5)
    return round(score, 3)   # 🔑 0–1 Skala
