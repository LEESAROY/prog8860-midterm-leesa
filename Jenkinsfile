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
                script {
                    // Use pip module for installation
                    def command = '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    '''
                    sh command
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    def command = '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    python -m unittest test_midterm.py
                    '''
                    sh command
                }
            }
        }

        stage('Push Docker') {
            steps {
                script {
                    def command = '''
                    docker build -t leesa007/python-jenkins:latest .
                    '''
                    sh command
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                        def dockerLoginCommand = '''
                        echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
                        docker push leesa007/python-jenkins:latest
                        '''
                        sh dockerLoginCommand
                    }
                }
            }
        }
    }
}
