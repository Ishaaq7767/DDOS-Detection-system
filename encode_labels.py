import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load processed dataset
df = pd.read_csv("processed_dataset.csv")

# Encode labels
encoder = LabelEncoder()
df["Label"] = encoder.fit_transform(df["Label"])  # 'ddos' → 1, 'normal' → 0

# Save the encoded dataset
df.to_csv("encoded_dataset.csv", index=False)

print("Label encoding completed. Saved as 'encoded_dataset.csv'.")
