pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // GitHub එකෙන් අලුත්ම කෝඩ් එක ගන්නවා
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Python Virtual Environment එකක් හදලා requirements ටික install කරනවා
                sh '''
                    echo "Installing Python Dependencies..."
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Pipeline') {
            steps {
                // ETL Data Pipeline එක run කරනවා
                sh '''
                    echo "Running the ETL Pipeline..."
                    source venv/bin/activate
                    python3 src/main_pipeline.py
                '''
            }
        }
    }
}