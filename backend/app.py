from fastapi import FastAPI
from routes.anomaly import detect
from routes.rootcause import analyze

app=FastAPI()

@app.post("/detect")
def detect_logs(logs:list):
    return detect(logs)

@app.post("/rootcause")
def rootcause(logs:list):
    return analyze(logs)