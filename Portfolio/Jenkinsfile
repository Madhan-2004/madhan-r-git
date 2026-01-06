pipeline {
    agent any

    stages {
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Start App') {
            steps {
                sh 'nohup python app/app.py &'
                sh 'sleep 5'
            }
        }

        stage('Run Automation') {
            steps {
                sh 'pytest --alluredir=reports'
            }
        }

        stage('Publish Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'reports']]
            }
        }

        stage('Deploy') {
            when { success() }
            steps {
                sh 'echo "Deployment Approved"'
            }
        }
    }
}
