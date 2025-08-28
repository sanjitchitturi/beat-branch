from joblib import load
import os
import argparse

MODEL_PATH = os.path.join("models", "genre_classifier.joblib")

# Load once
model = load(MODEL_PATH)

def predict_song(title, artist):
    text = f"{title} {artist}"
    return model.predict([text])[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict song genre by title and artist")
    parser.add_argument("--title", type=str, help="Song title")
    parser.add_argument("--artist", type=str, help="Artist name")

    args = parser.parse_args()

    if args.title and args.artist:
        genre = predict_song(args.title, args.artist)
        print(f"{args.title} — {args.artist} => {genre}")
    else:
        examples = [
            ("Blinding Lights", "The Weeknd"),
            ("Jolene", "Dolly Parton"),
            ("Lose Yourself", "Eminem"),
            ("Hello", "Adele"),
        ]
        for title, artist in examples:
            genre = predict_song(title, artist)
            print(f"{title} — {artist} => {genre}")
