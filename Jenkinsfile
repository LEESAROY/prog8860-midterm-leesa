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
                powershell 'python -m pip install --upgrade pip'
                powershell 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                powershell 'python -m pip install --upgrade pip'
                powershell 'pip install -r requirements.txt'
                powershell 'python -m unittest test_midterm.py'
            }
        }

        stage('Push Docker') {
            steps {
                powershell 'docker build -t leesa007/python-jenkins:latest .'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    powershell '''
                    $env:DOCKER_PASSWORD | docker login -u $env:DOCKER_USERNAME --password-stdin
                    docker push leesa007/python-jenkins:latest
                    '''
                }
            }
        }
    }
}
