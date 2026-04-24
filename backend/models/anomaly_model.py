from sklearn.ensemble import IsolationForest

model=IsolationForest()

def detect(vectors):
    pred=model.fit_predict(vectors)
    return pred