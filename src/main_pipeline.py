import os
from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    
    
    # CSV file eke path eka hadaganeema (data folder eka athule thiyana)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "data", "sales_data.csv")
    
    # 1. Extract Step
    df = extract_data(file_path)
    if df is None:
        print("Pipeline fail wuna: Extraction Error.")
        return
        
    # 2. Transform Step
    transformed_df = transform_data(df)
    if transformed_df is None:
        print("Pipeline fail wuna: Transformation Error.")
        return
        
    # 3. Load Step
    success = load_data(transformed_df)
    if success:
        print("ETL Pipeline Completed Successfully")
    else:
        print("Pipeline fail wuna: Database Load Error.")

if __name__ == "__main__":
    run_pipeline()