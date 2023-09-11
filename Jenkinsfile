pipeline {
    agent any 

    stages {
        stage('Checkout') {
            steps {
                checkout scm 
            }
        }
        
        stage('Build and Test Authentication Service') {
            steps {
                sh 'cd authentication && docker build -t auth_service .'
                sh 'cd authentication/tests && pytest'
            }
        }
        
        stage('Build and Test Products Service') {
            steps {
                sh 'cd products && docker build -t products_service .'
                sh 'cd products/tests && pytest'
            }
        }
        
        stage('Build and Test Reviews Service') {
            steps {
                sh 'cd reviews && docker build -t reviews_service .'
                sh 'cd reviews/tests && pytest'
            }
        }

        stage('Deployment') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
