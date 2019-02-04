pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "aws s3 cp test.txt s3://cyberitus-builds/test.txt"'
            }
        }
        
    }
}
