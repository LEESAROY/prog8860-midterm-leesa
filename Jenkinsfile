pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python -m pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pip install --upgrade pip && pip install -r requirements.txt'
                bat 'python -m unittest test_midterm.py'
            }
        }

        stage('Push Docker') {
            steps {
                bat 'docker build -t leesa007/python-jenkins:latest .'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    bat 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin && docker push leesa007/python-jenkins:latest'
                }
            }
        }
    }
}
