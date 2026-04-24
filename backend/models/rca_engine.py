def root_cause_analysis(logs):

    all_logs=" ".join(
      [x["log"].lower() for x in logs]
    )

    if "db timeout" in all_logs:
        return {
          "cause":"Database Saturation",
          "confidence":"94%",
          "fix":"Scale database replicas"
        }

    elif "cpu spike" in all_logs:
        return {
          "cause":"Resource Exhaustion",
          "confidence":"91%",
          "fix":"Scale service pods"
        }

    return {
       "cause":"Unknown",
       "confidence":"60%",
       "fix":"Manual inspection needed"
    }