pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Test Shell') {
            steps {
                sh 'echo Hello, World!'
            }
        }
    }
}
