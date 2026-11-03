# Phishing Email Detection

A beginner NLP and machine-learning application that classifies email text as phishing or legitimate.

## How it works
- Reads labeled examples from `data/emails.csv`.
- Converts text into TF-IDF features.
- Trains a Logistic Regression classifier.
- Displays a prediction in a Streamlit interface.

## Dataset limitation
The included CSV is a small, hand-written **demonstration dataset** intended to let you run and understand the complete workflow. It is not representative of real-world data and cannot support meaningful claims about real-world accuracy. Replace it with a larger, properly sourced dataset and document its source and licence before making performance claims.

## Run locally on Windows PowerShell
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python train_model.py
streamlit run app.py
```

## Deploy
1. Push this folder to a public GitHub repository.
2. Sign in at https://share.streamlit.io/ using GitHub.
3. Create an app, choose this repository and branch `main`.
4. Set the main file path to `app.py`, then deploy.

## Next improvements
- Replace the demo dataset with a larger public dataset and cite its source/licence.
- Compare more than one algorithm.
- Add a confusion matrix and discuss precision, recall and F1-score.
- Add tests and document failure cases.

## Responsible use
This is an educational baseline, not a production system. Do not use it for real security decisions or paste private customer messages into a public demo.
