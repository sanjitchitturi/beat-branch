# Beat Branch

**A beginner-friendly machine learning project to classify music genres using just song title and artist name.**

Beat Branch is a lightweight, beginner-level ML project that walks you through building a complete machine learning pipeline—from data processing to model training and prediction.

---

## Features

* Load and process a small song dataset
* Extract text features using **TF-IDF**
* Train a **Decision Tree Classifier** to predict music genres
* Save and load trained models for later use
* Simple, easy-to-run code for ML beginners

---

## Project Structure

```
Beat-Branch/
│
├── data/
│   └── songs_dataset.csv
│
├── models/
│   └── genre_classifier.joblib
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
└── README.md
```

---

## Dataset Preview

Stored in `data/songs_dataset.csv`:

| title             | artist       | genre     |
| ----------------- | ------------ | --------- |
| Blinding Lights   | The Weeknd   | Pop       |
| Bohemian Rhapsody | Queen        | Rock      |
| Lose Yourself     | Eminem       | Hip-Hop   |
| Für Elise         | Beethoven    | Classical |
| Jolene            | Dolly Parton | Country   |

---

## Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/sanjitchitturi/Beat-Branch.git
cd Beat-Branch

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Training the Model

Run the training script to train and save the model:

```bash
python src/train.py
```

This will:

* Train a Decision Tree Classifier
* Print a classification report
* Save the model and vectorizer to `models/genre_classifier.joblib`

---

## Making Predictions

Use the trained model to predict genres:

```bash
python src/predict.py
```

**Example Output:**

```
Blinding Lights — The Weeknd  =>  Pop
Jolene — Dolly Parton         =>  Country
```

You can edit `src/predict.py` to test your own song inputs.

---

## Requirements

* Python 3.8+
* `pandas`
* `scikit-learn`
* `joblib`

Install via:

```bash
pip install -r requirements.txt
```

---

## How It Works

1. **Feature Extraction**: Combines song title + artist into text and converts it to TF-IDF vectors.
2. **Model Training**: A Decision Tree learns patterns to predict genres.
3. **Evaluation**: Outputs classification report to measure performance.
4. **Prediction**: Uses the saved model to predict genre for new songs.

---
