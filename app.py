from pathlib import Path
import joblib
import streamlit as st
from train_model import train_model

ROOT = Path(__file__).resolve().parent
MODEL_PATH = ROOT / "model.joblib"
 
st.set_page_config(page_title="Phishing Email Detection", page_icon="🛡️")
st.title("Phishing Email Detection")
st.write("A beginner NLP and machine-learning application that classifies email text as phishing or legitimate.")
st.warning("Learning demo only. The bundled dataset is small and illustrative. Do not use this tool to make real security decisions.")

if not MODEL_PATH.exists():
    with st.spinner("Training the model for the first time..."):
        train_model()

model = joblib.load(MODEL_PATH)
user_text = st.text_area("Paste email text", height=170)
if st.button("Check email", type="primary"):
    if not user_text.strip():
        st.error("Please enter some text first.")
    else:
        prediction = model.predict([user_text])[0]
        probabilities = model.predict_proba([user_text])[0]
        st.write(f"**Prediction:** {prediction.upper()}")
        st.write(f"Model confidence: {float(max(probabilities)):.1%}")
        st.caption("Model confidence is not a guarantee. Review the limitations in the README.")
st.divider()
st.caption("Built with Python, pandas, scikit-learn and Streamlit.")
