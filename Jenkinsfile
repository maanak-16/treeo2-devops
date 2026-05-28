pipeline {
    agent any

    environment {
        IMAGE_NAME = "treeo2-api"
        CONTAINER_NAME = "treeo2-production"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Stage 1: Installing dependencies and building Docker image'
                bat 'py -m pip install -r requirements.txt'
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Test') {
            steps {
                echo 'Stage 2: Running automated API tests using pytest'
                bat 'py -m pytest tests'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Stage 3: Checking Python code quality'
                bat 'py -m compileall app'
            }
        }

        stage('Security') {
            steps {
                echo 'Stage 4: Running Bandit security scan'
                bat 'py -m bandit -r app || exit 0'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Stage 5: Deploying application container'
                bat 'docker rm -f %CONTAINER_NAME% || exit 0'
                bat 'docker run -d --name %CONTAINER_NAME% -p 8000:8000 %IMAGE_NAME%'
            }
        }

        stage('Release') {
            steps {
                echo 'Stage 6: Creating release tag'
                bat 'docker tag %IMAGE_NAME% %IMAGE_NAME%:release-%BUILD_NUMBER%'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Stage 7: Checking health and metrics endpoints'
                bat 'curl http://localhost:8000/health'
                bat 'curl http://localhost:8000/metrics'
            }
        }
    }

    post {
        success {
            echo 'TreeO2 DevOps pipeline completed successfully.'
        }

        failure {
            echo 'TreeO2 DevOps pipeline failed.'
        }
    }
}