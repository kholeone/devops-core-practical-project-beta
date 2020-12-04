pipeline {
    agent any
    stages {
        stage('Installation') {
            steps {
                sh './scripts/ansible.sh'
            }
        }
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