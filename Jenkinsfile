pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/rohit1443/Mytask2.git'
            }
        }
        stage('Run Unit Tests') {
            steps {
                sh 'python3 testsite.py'
            }
        }
    }
}
