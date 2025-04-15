import pandas as pd
import numpy as np
from catboost import CatBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("balanced_dataset.csv")

if "Label" not in df.columns:
    raise ValueError("Error: 'Label' column is missing from dataset!")

categorical_features = df.select_dtypes(include=['object']).columns.tolist()
if "Label" in categorical_features:
    categorical_features.remove("Label")  

for col in df.columns:
    if col not in categorical_features + ["Label"]:  
        df[col] = pd.to_numeric(df[col], errors='coerce')

X = df.drop(columns=["Label"])  
y = df["Label"]  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = CatBoostClassifier(iterations=100, learning_rate=0.1, depth=6, cat_features=categorical_features, verbose=100)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model Accuracy: {accuracy:.4f}")

model.save_model("catboost_ddos_model.cbm")
print("✅ Model saved successfully!")
