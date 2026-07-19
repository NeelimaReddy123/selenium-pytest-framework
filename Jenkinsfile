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
                sh """
                docker compose -f docker-compose.yml down --volumes --remove-orphans

                echo "Spinning up 3 nodes for ${params.BROWSER} and 0 for the rest..."

                docker compose -f docker-compose.yml up -d --force-recreate \\
                    --scale chrome=0 \\
                    --scale firefox=0 \\
                    --scale edge=0 \\
                    --scale ${params.BROWSER}=3

                echo "Waiting for Selenium Hub and Node Registration..."

                # FIXED: Swapped to a POSIX-compliant while loop for Jenkins /bin/sh
                attempt=1
                while [ \$attempt -le 30 ]; do
                     STATUS=\$(curl -s http://127.0.0.1:4444/status || true)
                     if echo "\$STATUS" | grep -q '"ready":true' && echo "\$STATUS" | grep -q '"nodeCount":[1-9]'; then
                          echo "Selenium Grid Hub is fully ready with registered nodes!"
                          break
                     fi
                     echo "Waiting for browser nodes to register (Attempt \$attempt/30)..."
                     attempt=\$((attempt + 1))
                     sleep 2
                done
                """
            }
        }

            stage('Run Tests') {
                steps {
                    // FIXED: Explicitly calling the pytest binary inside our virtual environment folder
                    sh """
                    ./venv/bin/pytest --alluredir=${REPORT_DIR} -n 3 --browser ${params.BROWSER} --env ${params.ENVIRONMENT} --mode ${params.MODE}
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