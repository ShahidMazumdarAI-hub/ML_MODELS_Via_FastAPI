import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("INSURANCE PREMIUM CATEGORY Predictor")
st.markdown("enter ur details below:")

# i/p Fields
age = st.number_input("Age", min_value=1, max_value=119, value=30)
weight = st.number_input("Weight (kg)", min_value=1.0, value=65.0)
height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7)
income_lpa = st.number_input("Annual Income (LPA)", min_value=0.1, value=10.0)
smoker = st.selectbox("Are U a Smoker?", options=[True,False])
city = st.text_input("city", value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job']
)

if st.button("Predict Premium Category"):
    input_data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation

    }

    try:
        response = requests.post(API_URL, json=input_data)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Predicted Insurance Premium Category: **{result['predicted_category']}**")
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Couldn't connect to the FastAPI server, make sure it's running on port 8000")

#to tun this above program to see ur frontend u need to run a command in terminal (streamlit run <ur file name>.py)
# or run <streamlit run C:/Users/PC/Desktop/FastAPI/myenvagainyaar/FrontEndForAPI.py> in ur terminal
