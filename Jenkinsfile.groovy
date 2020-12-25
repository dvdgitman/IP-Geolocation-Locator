pipeline {

    agent {
        label 'docker_node'
    }

    stages {
        stage('Build Docker image') {
            steps {
                dir('/var/jenkins_home/workspace/Test'){
                    script {
                        sh "sudo docker build -t iplocation ."
                    }
                }
            }
        }
    }
}
