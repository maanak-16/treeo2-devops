pipeline {
    agent any

    environment {
        IMAGE_NAME = "treeo2-api"
        CONTAINER_NAME = "treeo2-production"
    }

    stages {
        stage('Build') {
            steps {
                echo 'Stage 1: Building Docker image'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Test') {
            steps {
                echo 'Stage 2: Running tests inside Docker container'
                sh 'docker run --rm $IMAGE_NAME pytest tests'
            }
        }

        stage('Code Quality') {
            steps {
                echo 'Stage 3: Running code quality compile check inside Docker'
                sh 'docker run --rm $IMAGE_NAME python -m compileall app'
            }
        }

        stage('Security') {
            steps {
                echo 'Stage 4: Running Bandit security scan inside Docker'
                sh 'docker run --rm $IMAGE_NAME bandit -r app || true'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Stage 5: Deploying application container'
                sh 'docker rm -f $CONTAINER_NAME || true'
                sh 'docker run -d --name $CONTAINER_NAME -p 8000:8000 $IMAGE_NAME'
            }
        }

        stage('Release') {
            steps {
                echo 'Stage 6: Creating release tag'
                sh 'docker tag $IMAGE_NAME $IMAGE_NAME:release-$BUILD_NUMBER'
            }
        }

        stage('Monitoring') {
            steps {
                echo 'Stage 7: Checking health and metrics endpoints'
                sh 'sleep 5'
                sh 'curl http://localhost:8000/health'
                sh 'curl http://localhost:8000/metrics'
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