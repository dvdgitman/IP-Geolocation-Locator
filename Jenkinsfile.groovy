pipeline {

    agent {
        label 'docker_node'
    }

    stages {
        stage('Build Docker image') {
            steps {
                dir('/var/jenkins_home/workspace/DockerNode') {
                    script {
                        sh "docker build -t iplocation ."
                    }
                }
            }
        }
        stage('Test Docker image') {
            steps {
                dir('/var/jenkins_home/workspace/DockerNode/BasicTest') {
                    script {
                        try {
                            sh "./basic.test.sh"
                        } catch (err) {
                            println("Error thrown on test file execution")
                            currentBuild.result = 'ABORTED'
                            error('Error thrown on test file execution')
                        }
                    }
                }
            }
        }
        stage('upload image to repository'){
            steps {
                sh "docker push davidgman/iplocator:${latestVersion}-${lastCommit}"
            }
        }
    }
}    