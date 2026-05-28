pipeline {
    agent any

    environment {
        IMAGE_NAME = "treeo2-api"
        CONTAINER_NAME = "treeo2-production"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Stage 1: Building Docker image for TreeO2 Backend API'
                bat 'docker build -t %IMAGE_NAME% .'
            }
        }

        stage('Test') {
            steps {
                echo 'Stage 2: Running automated API tests using pytest'
                bat 'python -m pytest tests'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Stage 3: Running Python compile check as code quality validation'
                bat 'python -m compileall app'
            }
        }

        stage('Security') {
            steps {
                echo 'Stage 4: Running Bandit security scan'
                bat 'bandit -r app || exit 0'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Stage 5: Deploying TreeO2 API container'
                bat 'docker rm -f %CONTAINER_NAME% || exit 0'
                bat 'docker run -d --name %CONTAINER_NAME% -p 8000:8000 %IMAGE_NAME%'
            }
        }

        stage('Release') {
            steps {
                echo 'Stage 6: Creating release image tag'
                bat 'docker tag %IMAGE_NAME% %IMAGE_NAME%:release-%BUILD_NUMBER%'
                echo 'Release created successfully'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Stage 7: Monitoring deployed application using health and metrics endpoints'
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
            echo 'TreeO2 DevOps pipeline failed. Check console output.'
        }
    }
}