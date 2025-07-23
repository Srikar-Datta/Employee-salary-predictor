# 💼 Employee Salary Predictor

A machine learning web application built with Streamlit that predicts whether an individual's salary is **above or below $50K** based on demographic and employment features.  

This project uses classification models trained on the **Adult Income dataset** (also known as the "Census Income" dataset) from the UCI Machine Learning Repository.

---

## 🚀 Demo

![App Screenshot]("C:\Users\lenovo\OneDrive\Desktop\employee-salary-predictor\{F0CBB6DC-2476-4010-97C3-6D4B87D62FDF}.png") <!-- Optional: Replace with a real screenshot if needed -->

---

## 📦 Features

- Predicts whether a person earns `>50K` or `<=50K`
- Clean and modern UI built with Streamlit
- Preprocessing and feature encoding handled in the backend
- Quick test examples for high-income and low-income profiles
- Displays prediction probabilities and input summary

---

## 🧠 Model Details

- **Dataset**: [UCI Adult Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- **Model Used**: K-Nearest Neighbors (can be replaced with any classifier)
- **Input Features**:
  - Age
  - Workclass
  - Education
  - Marital Status
  - Occupation
  - Relationship
  - Race
  - Gender
  - Hours per week
  - Native country
  - Capital gain / loss
  - FNLWGT

---

## 🛠️ Tech Stack

| Tool         | Description                   |
|--------------|-------------------------------|
| Python       | Core programming language     |
| Streamlit    | Web framework for ML apps     |
| Pandas       | Data handling                 |
| Joblib       | Model loading                 |
| Scikit-learn | ML modeling (KNN)             |

---

## 📁 File Structure
-📦 employee-salary-predictor/

~ employee_salary_app.py # 💻 Streamlit web app

~ salary_predictor_model.pkl # 🎯 Trained ML model

~ adult 3.csv # 📂 Dataset 

~ requirements.txt # 📦 Python dependencies

~ README.md # 📘 Project documentation



📌 To-Do Suggestions
 🔄 Add option to upload CSV files for batch predictions
 📈 Show feature importance using SHAP or LIME
 🌙 Add light/dark mode toggle
 🚀 Deploy to Hugging Face Spaces or Render
 🗃️ Log predictions into a local CSV or database
 🧪 Add support for multiple ML models (RandomForest, Logistic, XGBoost)


 📄 License
This project is licensed under the MIT License
© 2025 [K.srikar Datta]
