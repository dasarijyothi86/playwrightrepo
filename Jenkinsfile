pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git 'https://github.com/dasarijyothi86/playwrightrepo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install pytest pytest-html'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --html=reports/report.html'
            }
        }

        stage('Publish Report') {
            steps {
                publishHTML(target: [
                    reportDir: 'reports',
                    reportFiles: 'report.html',
                    reportName: 'Test Report',
                    keepAll: true,
                    alwaysLinkToLastBuild: true,
                    allowMissing: true
                ])
            }
        }
    }
}
