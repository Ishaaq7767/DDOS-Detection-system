import pandas as pd
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load train and test data
X_train = pd.read_csv("X_train.csv")
X_test = pd.read_csv("X_test.csv")
y_train = pd.read_csv("y_train.csv")
y_test = pd.read_csv("y_test.csv")

# Train XGBoost model
model = XGBClassifier(n_estimators=50, use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train.values.ravel())  # Use .ravel() to avoid shape issues

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.4f}")

# Save the trained model
joblib.dump(model, "ddos_model.pkl")
print("Model saved as 'ddos_model.pkl'.")
