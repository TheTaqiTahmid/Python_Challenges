pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    ls -lah
			  cd ./hypotenuse/
			  cat input.txt
                	 '''
            }
        }
    }
}