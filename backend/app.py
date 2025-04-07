import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # Enable CORS for all routes

# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), "claim_model.pkl")
model = joblib.load(model_path)

@app.route('/')
def home():
    return "Claim Prediction API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from request
        data = request.get_json()

        # Convert data to DataFrame
        df = pd.DataFrame([data])

        # Convert categorical values to numeric (same as in training)
        df["policy_type"] = df["policy_type"].map({"comprehensive": 1, "third-party": 0})
        df["vehicle_damage"] = df["vehicle_damage"].map({"Yes": 1, "No": 0})

        # Ensure correct order of features
        features = ["age", "policy_type", "previous_claims", "vehicle_damage"]
        df = df[features]

        # Make prediction
        prediction = model.predict(df)[0]

        # Return result
        return jsonify({"claim_approved": int(prediction)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
