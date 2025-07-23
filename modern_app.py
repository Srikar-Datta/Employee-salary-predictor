import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("salary_predictor_model.pkl")

st.set_page_config(page_title="Employee Salary Predictor", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>Employee Salary Predictor</h1>", unsafe_allow_html=True)
st.write("Fill in the employee's details below to predict whether their salary is above or below 50K.")

with st.form("salary_form"):
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 18, 90, 30)
        fnlwgt = st.number_input("FNLWGT", value=100000)
        edu_num = st.slider("Educational-Num", 1, 16, 9)
        capital_gain = st.number_input("Capital Gain", value=0)
        capital_loss = st.number_input("Capital Loss", value=0)
        hours = st.slider("Hours per Week", 1, 100, 40)

    with col2:
        workclass = st.selectbox("Workclass (Encoded)", list(range(0, 9)))
        education = st.selectbox("Education (Encoded)", list(range(0, 16)))
        marital = st.selectbox("Marital Status (Encoded)", list(range(0, 7)))
        occupation = st.selectbox("Occupation (Encoded)", list(range(0, 14)))
        relationship = st.selectbox("Relationship (Encoded)", list(range(0, 6)))
        race = st.selectbox("Race (Encoded)", list(range(0, 5)))
        gender = st.radio("Gender (Encoded)", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
        country = st.selectbox("Native Country (Encoded)", list(range(0, 41)))

    submitted = st.form_submit_button("Predict Salary")

    if submitted:
        sample = pd.DataFrame([[age, workclass, fnlwgt, education, edu_num,
                                marital, occupation, relationship, race, gender,
                                capital_gain, capital_loss, hours, country]],
                              columns=model.feature_names_in_)

        result = model.predict(sample)[0]
        prediction = ">50K" if result == 1 else "<=50K"
        st.success(f"🧠 Predicted Salary: **{prediction}**")
