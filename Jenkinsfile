pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh './scripts/test.sh'
            }
        }
        stage('Push/Build') {
            steps {
                sh './scripts/build.sh'
            }
        }
        stage('Deploy') {
            steps {
                sh './scripts/deploy.sh'
            }
        }
    }
}
