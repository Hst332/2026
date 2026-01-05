def forecast_rating(prob_up: float):
    """
    Returns qualitative forecasts:
    short term (1–5 days), mid term (2–3 weeks)
    """
    if prob_up >= 0.60:
        return "++", "+"
    elif prob_up >= 0.55:
        return "+", "+"
    elif prob_up >= 0.48:
        return "=", "="
    elif prob_up >= 0.42:
        return "-", "-"
    else:
        return "--", "--"
