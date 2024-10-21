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
            agent {
                docker {
                    image 'python:3.8'
                }
            }
            steps {
                sh 'python3 -m pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.8'
                }
            }
            steps {
                sh 'python3 -m pip install --upgrade pip && pip install -r requirements.txt'
                sh 'python -m unittest test_midterm.py'
            }
        }

        stage('Push Docker') {
            agent {
                docker {
                    image 'docker:latest'
                }
            }
            steps {
                sh 'docker build -t leesa007/python-jenkins:latest .'
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin && docker push leesa007/python-jenkins:latest'
                }
            }
        }
    }
}
