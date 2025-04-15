import pandas as pd

# Load dataset
file_path = "balanced_dataset.csv"
df = pd.read_csv(file_path)

# Display dataset info
print(df.info())
print(df.head())
