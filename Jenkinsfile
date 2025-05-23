pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t budget-tracker .'
            }
        }
        stage('Test') {
            steps {
                echo 'Running unit tests...'
                sh 'pytest tests > test_report.txt'
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
                echo 'Deploying container...'
                sh 'docker run -d -p 5000:5000 budget-tracker'
            }
        }
        stage('Release') {
            steps {
                echo 'Tagging release...'
                sh 'git tag v1.0 || true'
                sh 'git push origin v1.0 || true'
            }
        }
        stage('Monitoring') {
            steps {
                echo 'Health check...'
                sh 'curl --fail http://localhost:5000/health || echo "Health check failed"'
            }
        }
    }
}
