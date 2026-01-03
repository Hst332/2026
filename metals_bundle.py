from forecast_gold import forecast_gold_2026
from forecast_silver import forecast_silver_2026
from forecast_copper import forecast_copper_2026

def forecast_metals_2026():
    return {
        "sector": "Metals",
        "metals": [
            forecast_gold_2026(),
            forecast_silver_2026(),
            forecast_copper_2026()
        ]
    }
