pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    cd C:\Python_challenges\Python_Challenges\hypotenuse
                    ls -lah
			  input.txt
                '''
            }
        }
    }
}