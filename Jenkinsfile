pipeline {
    agent any

    environment {
        PYTHON_PATH = 'python3'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Python') {
            steps {
                sh "${PYTHON_PATH} --version"
            }
        }

        stage('Lint Code') {
            steps {
                sh "${PYTHON_PATH} -m flake8 ."
            }
        }

        stage('Run Tests') {
            steps {
                sh "${PYTHON_PATH} -m unittest discover"
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.log', allowEmptyArchive: true
        }
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed.'
        }
    }
}
