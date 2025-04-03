from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open('Stroke_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))  # Load StandardScaler

# Value mappings
mappings = {
    'ever_married': {'Yes': 1, 'No': 0},
    'Residence_type': {'Urban': 1, 'Rural': 0},
    'work_type': {'Private': 0, 'Self-employed': 1, 'children': 2, 'Govt_job': 3, 'Never_worked': 4},
    'gender': {'Male': 0, 'Female': 1, 'Other': 2},
    'smoking_status': {'never smoked': 0, 'Unknown': 1, 'formerly smoked': 2, 'smokes': 3},
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json

        # Extract and map input values
        gender = mappings['gender'].get(data['gender'], 0)
        age = float(data['age'])
        hypertension = int(data['hypertension'])
        heart_disease = int(data['heart_disease'])
        ever_married = mappings['ever_married'].get(data['ever_married'], 0)
        work_type = mappings['work_type'].get(data['work_type'], 0)
        Residence_type = mappings['Residence_type'].get(data['Residence_type'], 0)
        avg_glucose_level = float(data['avg_glucose_level'])
        bmi = float(data['bmi'])
        smoking_status = mappings['smoking_status'].get(data['smoking_status'], 0)

        # Convert input to DataFrame with feature names
        feature_names = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married',
                         'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']
        
        features_df = pd.DataFrame([[gender, age, hypertension, heart_disease, ever_married, 
                                     work_type, Residence_type, avg_glucose_level, bmi, smoking_status]], 
                                   columns=feature_names)

        # Apply StandardScaler transformation
        features_scaled = scaler.transform(features_df.values)  # Ensure correct format

        # Debugging: Print input data
        print("Model Input Data (Raw):", features_df)
        print("Model Input Data (Scaled):", features_scaled)

        # Make prediction using probability (if applicable)
        probability = model.predict_proba(features_scaled)[0][1]  # Get probability of stroke

        # Apply threshold (adjustable)
        threshold = 0.5
        prediction = 1 if probability >= threshold else 0

        # Debugging: Print model output
        print(f"Stroke Probability: {probability}")
        print(f"Final Prediction (Threshold {threshold}): {prediction}")

        return jsonify({'stroke_prediction': prediction})
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
