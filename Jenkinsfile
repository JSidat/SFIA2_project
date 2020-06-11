pipeline {
    agent any

    stages {
        stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }
        
        stage('run ansible') {
            steps {
                sh './script/before-installation.sh'
                sh './script/ansible.sh'

        stage('deploy on docker-compose'){
            steps{
                sh './script/docker.sh'
            }
        }
                
            }
        }
    }
}