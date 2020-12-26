pipeline {

    agent {
        label 'docker_node'
    }

    stages {
        stage('Build Docker image') {
            steps {
                dir('/var/jenkins_home/workspace/Docker Node') {
                    script {
                        sh "sudo docker build -t iplocation ."
                    }
                }
            }
        }
        stage('Test Docker image') {
            steps {
                dir('/var/jenkins_home/workspace/Docker Node/Basic Test') {
                    script {
                        try {
                            sh "sudo ./basic.test.sh"
                        } catch (err) {
                            println("Error thrown on test file execution")
                            currentBuild.result = 'ABORTED'
                            error('Error thrown on test file execution')
                        }
                    }
                }
            }
        }
    }
}    