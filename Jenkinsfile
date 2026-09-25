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
                withEnv(['JENKINS_NODE_COOKIE=dontKillMe']) {
                    sh '''
                        echo "Deploying the App..."
                        source venv/bin/activate
                        
                        # කලින් එක නවත්වන්න
                        fuser -k 5000/tcp || true
                        pkill -f "python3 src/main_pipeline.py" || true
                        
                        # setsid හරහා සම්පූර්ණයෙන්ම වෙනම session එකක run කිරීම
                        setsid python3 src/main_pipeline.py > app.log 2>&1 < /dev/null &
                        
                        sleep 2
                        echo "Deployment step completed!"
                    '''
                }
            }
        }
    }
}