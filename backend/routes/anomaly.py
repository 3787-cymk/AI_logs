from models.anomaly_model import detect_anomalies

def detect(logs):
    """
    API route for anomaly detection
    """
    result = detect_anomalies(logs)

    return {
        "status":"success",
        "anomalies":result
    }