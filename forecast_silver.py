# --------- SILVER ---------
import pandas as pd
from datetime import datetime
import metals_bundle  # falls du die Funktion zum Laden der Daten hast

# Lade Silber-Daten
df = metals_bundle.load_silver()  # df muss 'Close' und 'prob_up' enthalten

# Letzter verfügbarer Tag
last_row = df.iloc[-1]
last_date = last_row.name.strftime("%Y-%m-%d")
close_price = last_row["Close"]
prob_up = last_row["prob_up"]

# Handelsstrategie Regeln
# Asset: Silver
# Signal: prob_up ≥ 0.96
# Richtung: LONG only
# Trades/Jahr: ~12
# Hebel: max. 15
# Stop-Loss: hart bei -20 %
# Kein Trade: alles darunter ignorieren

# Signal-Erstellung
if prob_up >= 0.96:
    signal = "LONG"
    position_size = "100 % Positionsgröße"
elif prob_up >= 0.90:
    signal = "LONG (partial)"
    position_size = "50 % Positionsgröße"
else:
    signal = "NO_TRADE"
    position_size = "0 %"

# Ausgabe
print("--------- SILVER ---------")
print(f"Data date : {last_date}")
print(f"Close     : {close_price}")
print(f"Prob UP   : {prob_up:.2f}%")
print("Handelsstrategie:")
print("prob_up ≥ 0.96 → LONG 100 % Positionsgröße")
print("0.90 ≤ prob_up < 0.96 → LONG 50 % Positionsgröße")
print("Alles darunter → kein Trade")
print("Kein Short, Max. Hebel 15, Stop-Loss -20 %")
print(f"Signal    : {signal}")
print(f"Positionsgröße : {position_size}")
