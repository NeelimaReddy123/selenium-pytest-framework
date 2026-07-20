pipeline {
    agent any

    parameters {
        choice(name: 'BROWSER', choices: ['chrome', 'firefox', 'edge'], description: 'Which browser should we test on?')
        choice(name: 'ENVIRONMENT', choices: ['remote', 'local'], description: 'Run on Docker Grid (remote) or Local Machine?')
        choice(name: 'MODE', choices: ['headless', 'normal'], description: 'Run headless for CI/CD speed, or normal for debugging?')
        string(
            name: 'WORKERS',
            defaultValue: '3',
            description: 'Provide the number of multi-threaded parallel execution threads. Set to 1 to enforce sequential testing.'
        )
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
                echo "Cleaning up any existing project containers..."
                docker compose -f docker-compose.yml down --volumes --remove-orphans

                echo "Ensuring name conflicts are resolved..."
                docker rm -f selenium-hub || true

                echo "Spinning up 3 nodes for ${params.BROWSER} and 0 for the rest..."

                docker compose -f docker-compose.yml up -d --force-recreate \\
                    --scale chrome=0 \\
                    --scale firefox=0 \\
                    --scale edge=0 \\
                    --scale ${params.BROWSER}=3

                echo "Waiting for Selenium Hub and Node Registration..."

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
                script {
                    def workerCount = params.WORKERS.toInteger()

                    if (workerCount > 1) {
                        echo "🚀 Spawning an elastic parallel test run utilizing ${workerCount} worker threads..."
                        sh "./venv/bin/pytest --alluredir=${REPORT_DIR} -n ${workerCount} --browser ${params.BROWSER} --env ${params.ENVIRONMENT} --mode ${params.MODE}"
                    } else {
                        echo "🔀 Flag set to 1 or lower. Enforcing strict sequential execution..."
                        sh "./venv/bin/pytest --alluredir=${REPORT_DIR} --browser ${params.BROWSER} --env ${params.ENVIRONMENT} --mode ${params.MODE}"
                    }

                    echo "📝 Injecting Jenkins build data into Allure results..."
                    def executorJson = """{
                        "name": "Jenkins",
                        "type": "jenkins",
                        "url": "${env.JENKINS_URL ?: ''}",
                        "buildOrder": ${env.BUILD_NUMBER ?: 1},
                        "buildName": "${env.JOB_NAME ?: 'Selenium-Framework'} #${env.BUILD_NUMBER ?: 1}",
                        "buildUrl": "${env.BUILD_URL ?: ''}"
                    }"""

                    writeFile file: "${REPORT_DIR}/executor.json", text: executorJson
                }
            }
        }
    }

    post {
        always {
            echo 'Always execute post-actions, even if the stage fails.'

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