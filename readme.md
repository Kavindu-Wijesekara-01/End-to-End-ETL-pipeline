# Customer Sales Data ETL Pipeline

## 📌 Project Overview
This project is a beginner-friendly MLOps and Data Engineering pipeline that extracts raw customer sales data from a CSV file, cleans and transforms the data using Pandas and NumPy, and securely loads the processed data into a Dockerized PostgreSQL database. 

It demonstrates core Data Engineering principles, environment management, and containerization.

## 🛠️ Tech Stack & Tools
* **Language:** Python 3.9+
* **Data Processing:** Pandas, NumPy
* **Database:** PostgreSQL, SQLAlchemy, psycopg2-binary
* **Containerization:** Docker, Docker Compose
* **Environment Management:** python-dotenv

## 📂 Project Structure

sales_etl_pipeline/
├── data/
│   └── sales_data.csv           # Raw dataset (input)
├── src/
│   ├── __init__.py
│   ├── extract.py               # Data extraction logic
│   ├── transform.py             # Data cleaning & feature engineering
│   ├── load.py                  # Database connection & loading logic
│   ├── database.py              # PostgreSQL SQLAlchemy engine setup
│   └── main_pipeline.py         # Main execution script
├── .env                         # Environment variables (DB credentials)
├── .gitignore                   # Git ignore file
├── docker-compose.yml           # PostgreSQL container setup
├── Dockerfile                   # Python application containerization
└── requirements.txt             # Python dependencies



## Setup & Installation
1. Clone the repository and navigate to the directory:

## Bash
git clone <your-repository-url>
cd sales_etl_pipeline
2. Create and configure the .env file in the root directory:

## Plaintext
DB_HOST=localhost
DB_PORT=5432
DB_NAME=sales_db
DB_USER=postgres
DB_PASSWORD=your_secure_password
3. Set up the Python Virtual Environment:
Windows:

## Bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Linux/Mac:



## Bash
docker-compose up -d
Step 2: Execute the ETL Pipeline locally

## Bash
python src/main_pipeline.py
If successful, you will see === ETL Pipeline Completed Successfully! === in your terminal.

## Running the Entire App in Docker
To containerize the Python script alongside the database:

1. Build the Docker Image:

## Bash
docker build -t sales_etl_pipeline .
2. Run the Container:

## Bash
docker run --network="host" --env-file .env sales_etl_pipeline