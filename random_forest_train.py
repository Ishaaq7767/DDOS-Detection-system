import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
df = pd.read_csv("balanced_dataset.csv")

# Ensure 'Label' column exists and separate it from features
if "Label" not in df.columns:
    raise ValueError("Error: 'Label' column is missing from dataset!")

# Convert non-categorical numeric columns to float
for col in df.columns:
    if col != "Label":  # Convert only non-label columns
        df[col] = pd.to_numeric(df[col], errors='coerce')

# Split features and labels
X = df.drop(columns=["Label"])  # Feature columns
y = df["Label"]  # Target column

# Split dataset into train-test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define and train Random Forest model
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.4f}")

# Save the trained model
joblib.dump(model, "random_forest_ddos_model.pkl")
print("✅ Model saved successfully as 'random_forest_ddos_model.pkl'!")
