# Phishing Email Detection

A beginner NLP and machine-learning application that classifies email text as phishing or legitimate.

## How it works
- Reads labeled examples from `data/emails.csv`.
- Converts text into TF-IDF features.
- Trains a Logistic Regression classifier.
- Displays a prediction in a Streamlit interface.

## Dataset limitation
The included CSV is a small, hand-written **demonstration dataset** intended to let you run and understand the complete workflow. It is not representative of real-world data and cannot support meaningful claims about real-world accuracy. Replace it with a larger, properly sourced dataset and document its source and licence before making performance claims.



## Responsible use
This is an educational baseline, not a production system. Do not use it for real security decisions or paste private customer messages into a public demo.
