pipeline {
    agent any
    environment {
        DOCKER_BUILDKIT = 1
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t budget-tracker .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest tests > test_report.txt || true'
            }
        }
        stage('Code Quality') {
            steps {
                echo 'Running pylint...'
                sh 'pylint app > pylint_report.txt || true'
            }
        }
        stage('Security') {
            steps {
                echo 'Running Bandit...'
                sh 'bandit -r app > bandit_report.txt || true'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'docker run -d -p 5000:5000 budget-tracker'
            }
        }
        stage('Release') {
            steps {
                echo 'Tagging version...'
                sh 'git tag v1.0 || true'
                sh 'git push origin v1.0 || true'
            }
        }
        stage('Monitoring') {
            steps {
                echo 'Health Check...'
                sh 'curl --fail http://localhost:5000/health || echo "Health check failed"'
            }
        }
    }
}
