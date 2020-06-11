pipeline {
    agent any

    stages {
        stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }
        
        stage('running ansible') {
            steps {
                sh './script/before-installation.sh'
                sh './script/ansible.sh'

        stage('Deploying Docker Stack'){
                
                steps{
                    sh 'chmod +x ./script/*'
                    sh './script/docker.sh'
                }
            }
        }
                
            }
        }
    }
