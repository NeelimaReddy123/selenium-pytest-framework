pipeline {
    agent any

    parameters {
        choice(name: 'BROWSER', choices: ['chrome', 'firefox', 'edge'], description: 'Which browser should we test on?')
        choice(name: 'ENVIRONMENT', choices: ['remote', 'local'], description: 'Run on Docker Grid (remote) or Local Machine?')
        choice(name: 'MODE', choices: ['headless', 'normal'], description: 'Run headless for CI/CD speed, or normal for debugging?')
    }

    environment {
        REPORT_DIR = 'reports'
        ALLURE_REPORT_DIR = 'allure_report'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // FIXED: Capitalized "Requirements.txt" to match your project exactly
                sh '''
                python3 -m venv venv
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r Requirements.txt
                '''
            }
        }

        stage('Set Up Selenium Grid') {
            steps {
                sh '''
                docker compose -f docker-compose.yml up -d
                echo "Waiting for Selenium Grid Hub to be available..."
                for i in {1..15}; do
                     if curl -s http://localhost:4444/status | grep -q '"ready":true'; then
                      echo "Selenium Grid Hub is ready."
                      break
                     fi
                     echo "Waiting for Selenium Grid Hub to initialize..."
                     sleep 2
                done
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh """
                pytest --alluredir=${REPORT_DIR} -n 3 --browser ${params.BROWSER} --env ${params.ENVIRONMENT} --mode ${params.MODE}
                """
            }
        }
    }
    post {
        always {
            echo 'Always execute post-actions, even if the stage fails.'

            // REMOVED: sh 'allure generate' (The plugin below does this automatically!)

            // Generates and archives the report inside the Jenkins UI natively
            allure([
                results: [[path: "${REPORT_DIR}"]],
                reportBuildPolicy: 'ALWAYS'
            ])

            sh '''
            docker compose -f docker-compose.yml down
            '''
        }
    }
}