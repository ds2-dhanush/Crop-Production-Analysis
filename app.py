import streamlit as st
import pandas as pd
import joblib
import numpy as np
import base64

# Load model and encoders
model = joblib.load('models/crop_production_model.pkl')
state_encoder = joblib.load('models/state_encoder.pkl')
district_encoder = joblib.load('models/district_encoder.pkl')
crop_encoder = joblib.load('models/crop_encoder.pkl')
season_encoder = joblib.load('models/season_encoder.pkl')
feature_columns = joblib.load('models/model_features.pkl')

# Predefined dropdown values from training data
unique_states = list(state_encoder.classes_)
unique_districts = list(district_encoder.classes_)
unique_crops = list(crop_encoder.classes_)
unique_seasons = list(season_encoder.classes_)

# Inject custom style
st.markdown("""
    <style>
        .main {
            background-color: #f8f9f5;
            font-family: 'Arial';
        }
        h1, h2, h3 {
            color: #2f4f4f;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
        .css-1d391kg { padding: 1rem 1rem 1rem 1rem; }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="🌾 Crop Yield Predictor", layout="wide")

st.title("🌾 Smart Agriculture: Crop Production Predictor")
st.markdown("""
Estimate crop production based on historical trends, region, crop type, and season.
This tool is built for agricultural planners, researchers, and farmers to make better decisions.
""")

st.markdown("---")

# CSV Upload Section
st.subheader("📂 Upload CSV file (Batch Prediction)")
uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"])

if uploaded_file:
    try:
        data = pd.read_csv(uploaded_file)
        data['State'] = state_encoder.transform(data['State'])
        data['District'] = district_encoder.transform(data['District'])
        data['Crop'] = crop_encoder.transform(data['Crop'])
        data['Season'] = season_encoder.transform(data['Season'])
        data = data[feature_columns]

        preds = model.predict(data)
        data['Predicted_Production (Tonnes)'] = preds

        st.success("✅ Batch predictions completed!")
        st.dataframe(data)

        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Predictions", csv, "predictions.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")

st.markdown("---")

# Manual Form Input
st.subheader("📝 Manual Entry (Single Prediction)")
with st.form("manual_input"):
    col1, col2 = st.columns(2)

    with col1:
        year = st.number_input("Year", min_value=2000, max_value=2035, step=1)
        area = st.number_input("Area (in hectares)", min_value=0.0, step=0.1)
        state = st.selectbox("Select State", unique_states)
        district = st.selectbox("Select District", unique_districts)

    with col2:
        crop = st.selectbox("Select Crop", unique_crops)
        season = st.selectbox("Select Season", unique_seasons)

    submit = st.form_submit_button("🌾 Predict Production")

    if submit:
        try:
            # Encode inputs
            state_encoded = state_encoder.transform([state])[0]
            district_encoded = district_encoder.transform([district])[0]
            crop_encoded = crop_encoder.transform([crop])[0]
            season_encoded = season_encoder.transform([season])[0]

            input_data = pd.DataFrame([[year, area, crop_encoded, season_encoded, state_encoded, district_encoded]],
                                      columns=feature_columns)

            prediction = model.predict(input_data)[0]

            st.success(f"🌱 *Estimated Crop Production:* {round(prediction, 2)} tonnes")

        except Exception as e:
            st.error(f"❌ Error: {e}. Please ensure values exist in training data.")

st.markdown("---")
st.caption("© 2025 | Built for Agri-Analytics by DHANUSH")