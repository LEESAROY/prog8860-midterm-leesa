pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        // PATH = "C:\\Users\\keval\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\keval\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'py -m venv flask'
                bat 'flask\\Scripts\\activate && py -m pip install --upgrade pip'
                bat 'flask\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'flask\\Scripts\\activate && py -m unittest test_midterm.py'
            }
        }

        stage('Push Docker') {
            steps {
                bat 'docker build -t leesa007/python-jenkins:latest .'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat 'echo %DOCKER_PASSWORD% | docker login -u %DOCKER_USERNAME% --password-stdin'
                    bat 'docker push leesa007/python-jenkins:latest'
                }
            }
        }
    }
}
