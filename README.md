# Beat Branch

A beginner-friendly machine learning project to classify music genres using just song title and artist name.

Beat Branch is a lightweight project that walks you through building a complete machine learning pipeline from data processing to model training, evaluation, and prediction.

---

## Features

- Load and process a small song dataset.
- Extract text features using TF-IDF.  
- Train a Decision Tree Classifier to predict music genres.
- Evaluate with a classification report and confusion matrix plot.
- Save and load trained models (pipeline with vectorizer and classifier). 
- Predict genres via CLI inputs or built-in examples.
- Simple, easy-to-run code for beginners. 

---

## Project Structure

```

Beat-Branch/
│
├── data/
│   └── songs\_dataset.csv
│
├── src/
│   ├── train.py
│   └── predict.py
│
├── requirements.txt
└── README.md

````

---

## Dataset Preview

Stored in `data/songs_dataset.csv`:

| title             | artist        | genre     |
| ----------------- | ------------- | --------- |
| Blinding Lights   | The Weeknd    | Pop       |
| Bohemian Rhapsody | Queen         | Rock      |
| Lose Yourself     | Eminem        | Hip-Hop   |
| Für Elise         | Beethoven     | Classical |
| Jolene            | Dolly Parton  | Country   |

---

## Installation and Setup

```bash
# 1. Clone the repository
git clone https://github.com/sanjitchitturi/Beat-Branch.git
cd Beat-Branch

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
````

---

## Training the Model

Run the training script:

```bash
python src/train.py
```

This will:

* Train a Decision Tree Classifier on the dataset.
* Split the data into train and test sets (80/20).
* Print a classification report.

---

## Making Predictions

You can predict genres in two ways:

### 1. With CLI Inputs

```bash
python src/predict.py --title "Shape of You" --artist "Ed Sheeran"
```

Output:

```
Shape of You — Ed Sheeran => Pop
```

### 2. With Default Examples

If no arguments are passed, the script predicts for built-in examples:

```bash
python src/predict.py
```

Example Output:

```
Blinding Lights — The Weeknd  =>  Pop
Jolene — Dolly Parton         =>  Country
Lose Yourself — Eminem        =>  Hip-Hop
Hello — Adele                 =>  Pop
```

---

## Requirements

* Python 3.8+
* pandas
* scikit-learn
* joblib
* matplotlib
* seaborn

Install via:

```bash
pip install -r requirements.txt
```

---

## How It Works

1. **Feature Extraction**: Combines song title and artist into text and converts it to TF-IDF vectors.
2. **Model Training**: A Decision Tree learns patterns to predict genres.
3. **Evaluation**: Uses a train/test split, prints a classification report, and saves a confusion matrix plot.
4. **Prediction**: Loads the saved pipeline to predict genres for new songs.

---
