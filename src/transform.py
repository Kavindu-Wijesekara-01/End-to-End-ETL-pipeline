import pandas as pd
import numpy as np

def transform_data(df):
    """Data clean karana saha features generate karana function eka."""
    print("[Transform] Data clean kirima saha features hadima patan gaththa...")
    
    try:
        # Column names wala thiyena extra spaces ain karanawa
        df.columns = df.columns.str.strip()
        
        # 1. Missing Values Clean Kirima
        # 'Order ID' nathi nisa, 'Sales' saha 'Profit' columns wala missing data thiyenawanm ain karanawa
        df = df.dropna(subset=['Sales', 'Profit'])
        
        # Ithuru wela thiyena anith missing values walata 'Unknown' kiyala danawa
        df.fillna('Unknown', inplace=True)
        
        # 2. Aluth Features Generate Kirima (Feature Engineering)
        # Order Date nathi nisa, NumPy use karala Profit Margin eka witharak hadanawa
        # (Sales 0 ta wada wadi nm witharak, nathnam margin eka 0i)
        df['Profit_Margin'] = np.where(df['Sales'] > 0, df['Profit'] / df['Sales'], 0)
        
        print(f"[Transform] Transformation iwarai. Aluth Data shape eka: {df.shape}")
        return df
        
    except Exception as e:
        print(f"[Transform] Error ekak aawa: {e}")
        return None