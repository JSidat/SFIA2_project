pipeline {
    agent any

    stages {
        stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }
        
        stage('Run application') {
            steps {
                sh './script/environment.sh'
                
            }
        }
    }
}