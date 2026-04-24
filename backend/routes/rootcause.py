from models.rca_engine import root_cause_analysis

def analyze(logs):
    cause=root_cause_analysis(logs)

    return {
       "root_cause":cause["cause"],
       "confidence":cause["confidence"],
       "fix":cause["fix"]
    }