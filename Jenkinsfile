pipeline {
    agent any

    stages {
        stage('Build Image') {
            steps {
                sh 'docker build -t login-app:latest .'
            }
        }

        stage('Deploy App') {
            steps {
                sh '''
                docker rm -f login-app || true
                docker run -d \
                  --name login-app \
                  -p 5010:5000 \
                  login-app:latest
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh '''
                sleep 5
                curl -f http://localhost:5010/health
                '''
            }
        }
    }
}

