import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# .env file eke details load karaganna
load_dotenv()

# Database credentials read kirima
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# PostgreSQL connection string eka hadeema
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

def get_engine():
    """PostgreSQL database engine eka return karana function eka."""
    try:
        engine = create_engine(DATABASE_URL)
        return engine
    except Exception as e:
        print(f"Database connection error: {e}")
        return None