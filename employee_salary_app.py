import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("salary_predictor_model.pkl")

# Encoding maps based on training preprocessing
workclass_map = {
    "Private": 0, "Self-emp-not-inc": 1, "Self-emp-inc": 2, "Federal-gov": 3,
    "Local-gov": 4, "State-gov": 5, "Without-pay": 6, "Never-worked": 7
}
education_map = {
    "Bachelors": 0, "HS-grad": 1, "11th": 2, "Masters": 3, "9th": 4, "Some-college": 5,
    "Assoc-acdm": 6, "Assoc-voc": 7, "7th-8th": 8, "Doctorate": 9, "Prof-school": 10,
    "5th-6th": 11, "10th": 12, "1st-4th": 13, "Preschool": 14, "12th": 15
}
marital_map = {
    "Married-civ-spouse": 0, "Divorced": 1, "Never-married": 2, "Separated": 3,
    "Widowed": 4, "Married-spouse-absent": 5, "Married-AF-spouse": 6
}
occupation_map = {
    "Tech-support": 0, "Craft-repair": 1, "Other-service": 2, "Sales": 3, "Exec-managerial": 4,
    "Prof-specialty": 5, "Handlers-cleaners": 6, "Machine-op-inspct": 7, "Adm-clerical": 8,
    "Farming-fishing": 9, "Transport-moving": 10, "Priv-house-serv": 11, "Protective-serv": 12,
    "Armed-Forces": 13
}
relationship_map = {
    "Wife": 0, "Own-child": 1, "Husband": 2, "Not-in-family": 3,
    "Other-relative": 4, "Unmarried": 5
}
race_map = {
    "White": 0, "Black": 1, "Asian-Pac-Islander": 2,
    "Amer-Indian-Eskimo": 3, "Other": 4
}
gender_map = {"Male": 0, "Female": 1}
country_list = [
    "United-States", "Cambodia", "England", "Puerto-Rico", "Canada", "Germany",
    "Outlying-US(Guam-USVI-etc)", "India", "Japan", "Greece", "South", "China",
    "Cuba", "Iran", "Honduras", "Philippines", "Italy", "Poland", "Jamaica",
    "Vietnam", "Mexico", "Portugal", "Ireland", "France", "Dominican-Republic",
    "Laos", "Ecuador", "Taiwan", "Haiti", "Columbia", "Hungary", "Guatemala",
    "Nicaragua", "Scotland", "Thailand", "Yugoslavia", "El-Salvador",
    "Trinadad&Tobago", "Peru", "Hong", "Holand-Netherlands"
]
country_map = {c: i for i, c in enumerate(country_list)}

# Page config
st.set_page_config(page_title="Employee Salary Predictor", layout="wide", page_icon="💼")
st.title("💼 Employee Salary Predictor")
st.sidebar.header("Enter Employee Details")

# Quick examples
if st.sidebar.button("👔 High Income"):
    example = {
        "age": 45, "workclass": "Private", "fnlwgt": 200000, "education": "Masters",
        "educational-num": 14, "marital-status": "Married-civ-spouse",
        "occupation": "Exec-managerial", "relationship": "Husband", "race": "White",
        "gender": "Male", "capital-gain": 15000, "capital-loss": 0, "hours-per-week": 50,
        "native-country": "United-States"
    }
    st.session_state.update(example)
if st.sidebar.button("👤 Low Income"):
    example = {
        "age": 22, "workclass": "Private", "fnlwgt": 150000, "education": "HS-grad",
        "educational-num": 9, "marital-status": "Never-married",
        "occupation": "Handlers-cleaners", "relationship": "Own-child", "race": "White",
        "gender": "Male", "capital-gain": 0, "capital-loss": 0, "hours-per-week": 25,
        "native-country": "United-States"
    }
    st.session_state.update(example)

# Input form
with st.sidebar.form("input_form"):
    age = st.slider("Age", 17, 90, st.session_state.get("age", 35))
    workclass = st.selectbox("Work Class", list(workclass_map.keys()), index=list(workclass_map.keys()).index(st.session_state.get("workclass", "Private")))
    fnlwgt = st.number_input("FNLWGT", 12285, 1484705, st.session_state.get("fnlwgt", 100000))
    education = st.selectbox("Education Level", list(education_map.keys()), index=list(education_map.keys()).index(st.session_state.get("education", "Bachelors")))
    education_num = st.slider("Years of Education", 1, 16, st.session_state.get("educational-num", 9))
    marital = st.selectbox("Marital Status", list(marital_map.keys()), index=list(marital_map.keys()).index(st.session_state.get("marital-status", "Never-married")))
    occupation = st.selectbox("Occupation", list(occupation_map.keys()), index=list(occupation_map.keys()).index(st.session_state.get("occupation", "Tech-support")))
    relationship = st.selectbox("Relationship", list(relationship_map.keys()), index=list(relationship_map.keys()).index(st.session_state.get("relationship", "Own-child")))
    race = st.selectbox("Race", list(race_map.keys()), index=list(race_map.keys()).index(st.session_state.get("race", "White")))
    gender = st.selectbox("Gender", list(gender_map.keys()), index=list(gender_map.keys()).index(st.session_state.get("gender", "Male")))
    capital_gain = st.number_input("Capital Gain", 0, 100000, st.session_state.get("capital-gain", 0))
    capital_loss = st.number_input("Capital Loss", 0, 5000, st.session_state.get("capital-loss", 0))
    hours = st.slider("Hours per Week", 1, 100, st.session_state.get("hours-per-week", 40))
    native_country = st.selectbox("Native Country", country_list, index=country_list.index(st.session_state.get("native-country", "United-States")))
    submitted = st.form_submit_button("Predict Salary")

# If submitted, process and predict
if submitted:
    # Encode inputs
    data = {
        "age": age,
        "workclass": workclass_map[workclass],
        "fnlwgt": fnlwgt,
        "education": education_map[education],
        "educational-num": education_num,
        "marital-status": marital_map[marital],
        "occupation": occupation_map[occupation],
        "relationship": relationship_map[relationship],
        "race": race_map[race],
        "gender": gender_map[gender],
        "capital-gain": capital_gain,
        "capital-loss": capital_loss,
        "hours-per-week": hours,
        "native-country": country_map[native_country]
    }
    input_df = pd.DataFrame([data])

    # Display input
    st.subheader("📋 Input Parameters")
    display_df = input_df.copy()
    display_df.columns = [col.replace("-", " ").title() for col in display_df.columns]
    st.write(display_df.T)

    # Predict
    result = model.predict(input_df)[0]
    prediction = ">50K" if result == 1 else "<=50K"
    st.subheader("🎯 Prediction")
    if prediction == ">50K":
        st.success(f"💰 Predicted Salary: {prediction}")
        st.balloons()
    else:
        st.info(f"Predicted Salary: {prediction}")

    # Show probabilities
    probs = model.predict_proba(input_df)[0]
    st.subheader("📈 Probabilities")
    prob_df = pd.DataFrame({
        "Income": [">50K", "<=50K"],
        "Probability": [probs[1], probs[0]]
    }).set_index("Income")
    st.bar_chart(prob_df)
