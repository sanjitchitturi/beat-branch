# BeatBranch

BeatBranch predicts music genres from audio using a Decision Tree classifier.

## Features
- Extracts MFCCs, chroma, spectral contrast, tonnetz, tempo, and other audio features (librosa).
- Reproducible scikit-learn pipeline with cross-validation and hyperparameter tuning.
- Tools for model evaluation (confusion matrix, classification report) and feature importance.
- Optional simple web UI (Streamlit/Flask) for demo.

## Requirements
- Python 3.8+
- librosa, numpy, pandas, scikit-learn, matplotlib, joblib
- (Optional) streamlit, flask

Install:
```bash
pip install numpy pandas scikit-learn librosa matplotlib joblib streamlit
