pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }

    stages {
        stage('Build') {
            steps {
                checkout scm
                sh 'python3 -m pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m pip install --upgrade pip && pip install -r requirements.txt'
                sh 'python -m unittest test_midterm.py'
            }
        }

        stage('Push Docker') {
            steps {
                sh 'docker build -t leesa007/python-jenkins:latest .'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin && docker push leesa007/python-jenkins:latest'
                }
            }
        }
    }
}
