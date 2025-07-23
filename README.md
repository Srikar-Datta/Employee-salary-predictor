# 💼 Employee Salary Predictor

A machine learning web app built with **Streamlit** to predict whether an individual's income is **greater than 50K** or not, based on their demographic and employment features.

---

## 🌐 Live App (Local Network)

👉 [Click here to open the app](http://192.168.58.201:8501/)  
📌 Note: This link works only on the same local network as the host.

---

## 🚀 Features

- ✅ Predicts if income is >50K or ≤50K
- 🔍 Inputs include age, education, workclass, marital status, hours/week, etc.
- 📊 Built-in examples for testing
- 🎯 Displays prediction result and probabilities
- 🧠 Model trained using **Random Forest Classifier**

---

## 🧠 System Overview

### 🔹 Dataset Used
- [UCI Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult)

### 🔹 ML Pipeline
1. **Preprocessing**:
   - Handling missing values
   - Label encoding for categorical data
2. **Model**:
   - Random Forest Classifier
   - Trained on 80/20 train-test split
3. **Deployment**:
   - Model saved as `salary_predictor_model.pkl` using `joblib`
   - UI built with Streamlit and launched via:
     ```bash
     streamlit run employee_salary_app.py
     ```

---

## 🗂️ File Structure

-📦 employee-salary-predictor/

~ employee_salary_app.py # 💻 Streamlit web app

~ salary_predictor_model.pkl # 🎯 Trained ML model

~ adult 3.csv # 📂 Dataset 

~ requirements.txt # 📦 Python dependencies

~ README.md # 📘 Project documentation




---

## 🧪 Sample Use Case

| Feature            | Value               |
|--------------------|---------------------|
| Age                | 38                  |
| Education          | Masters             |
| Occupation         | Exec-manager        |
| Hours-per-week     | 45                  |
| Marital Status     | Married             |

🔮 **Prediction**: Income >50K  
📈 **Confidence**: 85.6%

---

## 📌 To-Do Improvements

- [ ] CSV batch upload support
- [ ] Deploy to public cloud (Streamlit Cloud, Hugging Face)
- [ ] Add feature importance visualizations
- [ ] Add user session logging
- [ ] Include SHAP or LIME explanations

---

## 📄 License

This project is licensed under the **MIT License**  
© 2025 Srikar Datta

---

## 🙌 References

- [UCI Adult Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [Joblib Docs](https://joblib.readthedocs.io/)

