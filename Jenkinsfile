@Library('jenkins-shared-lib') _

pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "taye97/${env.JOB_BASE_NAME}"
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'
        APP_ENV = 'production'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sharedLib.buildDocker(DOCKER_IMAGE)
                }
            }
        }

        stage('Security Scan') {
            steps {
                script {
                    sharedLib.securityScan(DOCKER_IMAGE)
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    sharedLib.runTests()
                }
            }
        }

        stage('Push Image') {
            steps {
                script {
                    sharedLib.pushDocker(DOCKER_IMAGE, DOCKER_CREDENTIALS_ID)
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sharedLib.deploy(APP_ENV)
                }
            }
        }
    }
}
