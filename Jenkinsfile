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

        stage('Deploy') {
            steps {
                // Jenkins තියෙන සර්වර් එකේම App එක background එකේ run කරනවා
                sh '''
                    echo "Deploying the App..."
                    source venv/bin/activate
                    
                    # කලින් run වෙන app එකක් තියෙනම් ඒක නවත්වන්න (Port 5000 උදාහරණයක් ලෙස)
                    pkill -f "python3 src/main_pipeline.py" || true
                    
                    # App එක background එකේ run කරන්න
                    nohup python3 src/main_pipeline.py > app.log 2>&1 &
                '''
            }
        }
    }
}