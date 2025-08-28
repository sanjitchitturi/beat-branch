import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from joblib import dump
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_PATH = os.path.join("data", "songs_dataset.csv")
MODEL_PATH = os.path.join("models", "genre_classifier.joblib")

def main():
    # Load dataset
    df = pd.read_csv(DATA_PATH)

    # Features: combine title + artist
    X = (df["title"] + " " + df["artist"]).values
    y = df["genre"].values

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Pipeline: TF-IDF + Decision Tree
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", DecisionTreeClassifier(random_state=42, max_depth=10))
    ])

    # Train model
    pipeline.fit(X_train, y_train)

    # Evaluate
    preds = pipeline.predict(X_test)
    print(classification_report(y_test, preds))

    # Confusion matrix plot
    cm = confusion_matrix(y_test, preds, labels=pipeline.classes_)
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
                xticklabels=pipeline.classes_,
                yticklabels=pipeline.classes_)
    plt.xlabel("Predicted")
    plt.ylabel("True")
    plt.title("Confusion Matrix")
    plt.tight_layout()
    os.makedirs("results", exist_ok=True)
    plt.savefig("results/confusion_matrix.png")
    print("Confusion matrix saved to results/confusion_matrix.png")

    # Save model
    os.makedirs("models", exist_ok=True)
    dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
