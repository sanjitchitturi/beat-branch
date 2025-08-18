# Beat Branch

*A beginner-friendly machine learning project to classify music genres using only song title and artist name.*  

---

## Project Overview
Beat Branch is a simple, introductory-level machine learning project that demonstrates how to:  
- Load and process a small dataset  
- Extract text features using **TF-IDF**  
- Train a **Decision Tree Classifier** to predict music genres  
- Save and load trained models for later predictions  

This project is intentionally small and easy-to-run, making it perfect for learners who are new to machine learning and want to build their first end-to-end ML pipeline.  

---

## Repository Structure

```

Beat-Branch/
│
├── data/
│   └── songs\_dataset.csv      # Small dataset of songs with title, artist, and genre
│
├── models/
│   └── genre\_classifier.joblib  # Saved model after training (created after running train.py)
│
├── src/
│   ├── train.py               # Script to train and evaluate the model
│   └── predict.py             # Script to make predictions with the saved model
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

````

---

## Dataset
The dataset is stored in `data/songs_dataset.csv` and contains **song title**, **artist name**, and **genre**. Example rows:  

| title              | artist          | genre     |
|--------------------|-----------------|-----------|
| Blinding Lights    | The Weeknd      | Pop       |
| Bohemian Rhapsody  | Queen           | Rock      |
| Lose Yourself      | Eminem          | Hip-Hop   |
| Für Elise          | Beethoven       | Classical |
| Jolene             | Dolly Parton    | Country   |

---

## Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/sanjitchitturi/Beat-Branch.git
   cd Beat-Branch

2. **Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
---

## Usage

### 1. Train the model

Run the training script to train the Decision Tree model and save it:

```bash
python src/train.py
```

This will:

* Train a Decision Tree on the dataset
* Print a classification report
* Save the model + vectorizer to `models/genre_classifier.joblib`

---

### 2. Predict genres

Use the saved model to make predictions:

```bash
python src/predict.py
```

Example output:

```
Blinding Lights — The Weeknd  =>  Pop
Jolene — Dolly Parton         =>  Country
```

You can edit `src/predict.py` to test different songs manually.

---

## Requirements

* Python 3.8+
* pandas
* scikit-learn
* joblib

Install them with:

```bash
pip install -r requirements.txt
```

---

## How It Works

1. **Feature Extraction:** Song title + artist name are combined into text and converted into a TF-IDF vector.
2. **Model Training:** A Decision Tree classifier learns patterns from the text to predict genres.
3. **Evaluation:** The script prints a classification report to evaluate accuracy.
4. **Prediction:** The trained model is used to classify new songs into genres.

---

## Future Improvements

* Add more songs and genres to improve accuracy
* Try other classifiers (Random Forest, SVM, etc.)
* Build a simple web/app interface for predictions

---

# Designed & Built by Sanjit Chitturi.
