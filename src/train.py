import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from joblib import dump
import os

DATA_PATH = os.path.join("data", "songs_dataset.csv")
MODEL_PATH = os.path.join("models", "genre_classifier.joblib")

def main():
    df = pd.read_csv(DATA_PATH)

    X = (df["title"] + " " + df["artist"]).values
    y = df["genre"].values

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", DecisionTreeClassifier(random_state=42))
    ])

    pipeline.fit(X, y)
    preds = pipeline.predict(X)

    print(classification_report(y, preds))
    os.makedirs("models", exist_ok=True)
    dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
