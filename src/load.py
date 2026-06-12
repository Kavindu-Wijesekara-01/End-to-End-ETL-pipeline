import pandas as pd
from database import get_engine

def load_data(df, table_name="sales_processed_data"):
    """Clean karapu DataFrame eka PostgreSQL database ekata save karana function eka."""
    print(f"[Load] Data database ekata save kirima patan gaththa. Table: {table_name}")
    
    try:
        # database.py eken engine eka gannawa
        engine = get_engine()
        if engine is None:
            print("[Load] Database connection eka fail.")
            return False
        
        # pandas wala to_sql use karala kelinma database table ekata data danawa
        # if_exists='replace' kiyanne table eka kalin thibboth eka makala aluth eka danawa kiyana eka
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        
        print(f"[Load] Data successfully '{table_name}' table ekata save wuna!")
        return True
        
    except Exception as e:
        print(f"[Load] Database ekata data danakota error ekak aawa: {e}")
        return False