import metals_bundle

print("[START] Silver backtest")

df = metals_bundle.load_silver()

# letzter Datensatz
last_row = df.iloc[-1]

# WICHTIG: explizit float
prob_up = float(last_row["prob_up"])
close_price = float(last_row["Close"])

if prob_up >= 0.96:
    signal = "LONG"
elif prob_up >= 0.90:
    signal = "LONG (partial)"
else:
    signal = "NO_TRADE"

print("--------- SILVER ---------")
print(f"Close   : {close_price}")
print(f"Prob UP : {prob_up:.2%}")
print(f"Signal  : {signal}")
