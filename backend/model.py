def predict_failure(vibration, temperature, pressure):

    score = 0.0

    # Vibration contribution
    if vibration >= 8:
        score += 0.40
    elif vibration >= 6:
        score += 0.20

    # Temperature contribution
    if temperature >= 85:
        score += 0.35
    elif temperature >= 70:
        score += 0.15

    # Pressure contribution
    if pressure >= 8:
        score += 0.25
    elif pressure >= 7:
        score += 0.10

    score = min(score, 1.0)

    if score >= 0.70:
        status = "HIGH_RISK"
    elif score >= 0.40:
        status = "WARNING"
    else:
        status = "NORMAL"

    return {
        "failure_probability": round(score, 2),
        "machine_status": status
    }