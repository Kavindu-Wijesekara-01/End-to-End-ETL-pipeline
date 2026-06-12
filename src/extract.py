import pandas as pd
import os

def extract_data(file_path):
    """CSV file eka read karana function eka."""
    print(f"[Extract] Data load wemin pawathi... File: {file_path}")
    try:
        # File eka hariyata thiyenawada kiyala check karanawa
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Error: {file_path} file eka hoyaganna baha.")
        
        # Pandas walin CSV eka read karanawa
        df = pd.read_csv(file_path, encoding='windows-1252') 
        
        print(f"[Extract] Data extract kara gaththa. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
        
    except Exception as e:
        print(f"[Extract] Error ekak aawa: {e}")
        return None