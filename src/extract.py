import pandas as pd
import os

def extract_data(file_path):
    """Function to read the CSV file."""
    print(f"[Extract] Loading data... File: {file_path}")
    try:
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Error: Could not find the file {file_path}.")
        
        # Read the CSV file using Pandas
        df = pd.read_csv(file_path, encoding='windows-1252') 
        
        print(f"[Extract] Data successfully extracted. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
        
    except Exception as e:
        print(f"[Extract] An error occurred: {e}")
        return None