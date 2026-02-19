pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Pulling code from GitHub...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Simulating build step'
                sh 'ls -l'
            }
        }

        stage('Success') {
            steps {
                echo 'Pipeline executed successfully 🎉'
            }
        }
    }
}
