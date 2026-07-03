import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Iris Flower Classifier",
    page_icon="🌸",
    layout="centered"
)

# Load model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "Models" / "iris_model.pkl"

model = joblib.load(MODEL_PATH)

# Title
st.title("🌸 Iris Flower Classification")
st.markdown("""
This application predicts the **species of an Iris flower**
based on four flower measurements.
""")

st.divider()

# User Inputs
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.number_input(
        "Sepal Length (cm)",
        value=5.1
    )

    petal_length = st.number_input(
        "Petal Length (cm)",
        value=1.4
    )

with col2:
    sepal_width = st.number_input(
        "Sepal Width (cm)",
        value=3.5
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        value=0.2
    )

if st.button("Predict Species", use_container_width=True):

    sample = pd.DataFrame({
        "SepalLengthCm": [sepal_length],
        "SepalWidthCm": [sepal_width],
        "PetalLengthCm": [petal_length],
        "PetalWidthCm": [petal_width]
    })

    prediction = model.predict(sample)[0]

    st.success(f"🌼 Predicted Species: **{prediction}**")