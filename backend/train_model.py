import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load dataset with correct file path
csv_path = os.path.join(os.path.dirname(__file__), "insurance_claims.csv")
df = pd.read_csv(csv_path)

print("✅ Dataset loaded successfully!")

# Convert categorical columns to numerical values
df["policy_type"] = df["policy_type"].map({"comprehensive": 1, "third-party": 0})
df["vehicle_damage"] = df["vehicle_damage"].map({"Yes": 1, "No": 0})

# Check if all values are numeric
print(df.dtypes)

# Prepare features (X) and target (y)
X = df.drop(columns=["claim_approved"])
y = df["claim_approved"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make sample predictions using training data
sample_predictions = model.predict(X_train[:10])
print("Sample Predictions:", sample_predictions)
print("Actual Labels:", y_train[:10].values)


# Save the trained model
joblib.dump(model, os.path.join(os.path.dirname(__file__), "claim_model.pkl"))
print("✅ Model training complete! Model saved as claim_model.pkl")
