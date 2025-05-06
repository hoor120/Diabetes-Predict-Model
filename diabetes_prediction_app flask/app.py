from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('diabetes_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')  # Your HTML form page

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from form and convert to numeric
        gender = request.form['gender']
        pregnancies = int(request.form['pregnancies']) if gender == 'female' else 0
        glucose = float(request.form['glucose'])
        blood_pressure = float(request.form['blood_pressure'])
        skin_thickness = float(request.form['skin_thickness'])
        insulin = float(request.form['insulin'])
        bmi = float(request.form['bmi'])
        dpf = float(request.form['dpf'])  # Diabetes Pedigree Function
        age = int(request.form['age'])

        # Prepare input data
        input_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]]
        
        # Make prediction
        prediction = model.predict(input_data)
        
        if prediction[0] == 1:
            result = 'Patient may have diabetes.'
        else:
            result = 'Patient is likely healthy.'

        return render_template('result.html', prediction_text=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
