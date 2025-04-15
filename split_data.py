import pandas as pd
from sklearn.model_selection import train_test_split

# Load encoded dataset
df = pd.read_csv("encoded_dataset.csv")

# Define features and labels
X = df.drop(columns=["Label"])  # Features
y = df["Label"]  # Target

# Split dataset (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save train and test sets
X_train.to_csv("X_train.csv", index=False)
X_test.to_csv("X_test.csv", index=False)
y_train.to_csv("y_train.csv", index=False)
y_test.to_csv("y_test.csv", index=False)

print("Data split completed. Training & testing datasets saved.")
