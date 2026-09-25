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
                    
                    # Port 5000 හෝ අදාළ process එක කලින් run වෙනවා නම් නවත්වන්න
                    fuser -k 5000/tcp || true
                    pkill -f "python3 src/main_pipeline.py" || true
                    
                    # Jenkins ගෙන් process එක සම්පූර්ණයෙන්ම නිදහස් කරලා background run කිරීම
                    export BUILD_ID=dontKillMe
                    nohup python3 src/main_pipeline.py > app.log 2>&1 < /dev/null &
                    
                    # තත්පර 2ක් ඉඳලා shell එකෙන් සාර්ථකව exit වෙන්න
                    sleep 2
                '''
            }
        }
    }
}