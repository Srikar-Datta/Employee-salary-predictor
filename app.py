import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load("salary_predictor_model.pkl")

st.title("Employee Salary Predictor")

# Input fields for user
age = st.number_input("Age", 18, 100)
workclass = st.number_input("Workclass (Encoded)", 0, 8)
fnlwgt = st.number_input("FNLWGT")
education = st.number_input("Education (Encoded)", 0, 15)
edu_num = st.number_input("Educational-Num", 1, 16)
marital = st.number_input("Marital Status (Encoded)", 0, 6)
occupation = st.number_input("Occupation (Encoded)", 0, 13)
relationship = st.number_input("Relationship (Encoded)", 0, 5)
race = st.number_input("Race (Encoded)", 0, 4)
gender = st.number_input("Gender (Encoded)", 0, 1)
capital_gain = st.number_input("Capital Gain")
capital_loss = st.number_input("Capital Loss")
hours = st.number_input("Hours per Week", 1, 100)
country = st.number_input("Native Country (Encoded)", 0, 40)

if st.button("Predict Salary"):
    sample = pd.DataFrame([[age, workclass, fnlwgt, education, edu_num,
                            marital, occupation, relationship, race, gender,
                            capital_gain, capital_loss, hours, country]],
                          columns=model.feature_names_in_)

    result = model.predict(sample)
    st.success(f"Prediction: {'>50K' if result[0] == 1 else '<=50K'}")
