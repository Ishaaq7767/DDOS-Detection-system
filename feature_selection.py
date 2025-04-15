import pandas as pd

# Load dataset
file_path = "balanced_dataset.csv"  # Make sure this path is correct
df = pd.read_csv(file_path)

# Drop unnecessary columns
df = df.drop(columns=["Flow ID", "Timestamp"])

# Save the updated dataset
df.to_csv("processed_dataset.csv", index=False)

print("Feature selection completed. Saved as 'processed_dataset.csv'.")
