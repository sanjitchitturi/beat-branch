from joblib import load
import os

MODEL_PATH = os.path.join("models", "genre_classifier.joblib")

def predict_song(title, artist):
    model = load(MODEL_PATH)
    text = f"{title} {artist}"
    return model.predict([text])[0]

if __name__ == "__main__":
    examples = [
        ("Blinding Lights", "The Weeknd"),
        ("Jolene", "Dolly Parton"),
        ("Lose Yourself", "Eminem"),
        ("Hello", "Adele"),
    ]

    for title, artist in examples:
        genre = predict_song(title, artist)
        print(f"{title} — {artist} => {genre}")
