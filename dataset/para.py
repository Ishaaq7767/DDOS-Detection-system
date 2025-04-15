import pandas as pd
import os

def convert_parquet_to_csv(parquet_folder, output_folder):
    """
    Converts all Parquet files in a folder to CSV format and saves them in the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for file in os.listdir(parquet_folder):
        if file.endswith(".parquet"):
            parquet_file = os.path.join(parquet_folder, file)
            csv_file = os.path.join(output_folder, file.replace(".parquet", ".csv"))
            
            print(f"Converting {file} to CSV...")
            df = pd.read_parquet(parquet_file)
            df.to_csv(csv_file, index=False)
            print(f"Saved: {csv_file}")

# Example usage
convert_parquet_to_csv("dataset/", "converted_csv/")
