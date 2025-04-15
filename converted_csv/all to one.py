import pandas as pd
import os

def merge_csv_files(csv_folder, output_file):
    """
    Merges all CSV files in a folder into a single CSV file.
    """
    all_dfs = []
    
    for file in os.listdir(csv_folder):
        if file.endswith(".csv"):
            file_path = os.path.join(csv_folder, file)
            print(f"Reading {file}...")
            df = pd.read_csv(file_path)
            all_dfs.append(df)
    
    merged_df = pd.concat(all_dfs, ignore_index=True)
    print(f"Saving merged dataset to {output_file}...")
    merged_df.to_csv(output_file, index=False)
    print("Merging complete!")
    return merged_df

# Example usage
merged_df = merge_csv_files("converted_csv/", "merged_dataset.csv")