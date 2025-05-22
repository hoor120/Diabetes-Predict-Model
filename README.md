# 🩺 Diabetes Prediction Web App

This is a **Flask-based machine learning web application** that predicts whether a person is diabetic or not based on input medical parameters. It uses a trained model and provides predictions through a user-friendly web interface.

---

## 📁 Project Files

```
📦 diabetes-prediction-app/
├── app.py              → Flask backend logic
├── templates/
│   ├── index.html      → Input form for user data
│   └── result.html     → Displays prediction result
├── model.pkl           → Trained ML model
├── requirements.txt    → Required Python packages
├── README.md           → This file
```

---

## 💡 Features

- Predicts diabetes using medical data
- Clean UI with HTML forms
- Uses a trained machine learning model
- Powered by Flask (Python web framework)

---

## 🧠 Model Info

- Trained on the **Pima Indians Diabetes Dataset**
- Features used:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age
- Algorithm used: **Random Forest / Logistic Regression**

---

## 🚀 How to Run This App Locally

1. **Clone the repository or download the files**
2. Open terminal in the project folder

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**
   ```bash
   python app.py
   ```

5. **Open your browser and go to**
   ```
   http://localhost:5000/
   ```

---

## 🖼️ App Pages

- `index.html` → Form to enter patient data
- `result.html` → Displays prediction result
- `app.py` → Flask code that connects everything

---

## 🧪 Sample Output

```text
Prediction: The person is likely to be diabetic.
```

or

```text
Prediction: The person is not likely to be diabetic.
```

---

## 📦 requirements.txt

```
flask
pandas
scikit-learn
joblib
---

## 📄 License

This project is for educational and learning purposes only.

