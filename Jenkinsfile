pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the repository
                checkout scm
            }
        }

        stage('Install Python') {
            steps {
                // Ensure Python is installed
                sh 'python --version'
            }
        }

        stage('Run Tests') {
            steps {
                // Run unit tests
                sh 'python -m unittest discover'
            }
        }
    }

    post {
        always {
            // Archive test results and logs
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
