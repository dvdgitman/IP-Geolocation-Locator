def lastCommit
def latestVersion

pipeline {

    agent {
        label 'docker_node'
    }

    stages {
        stage('Build Docker image') {
            steps {
                dir('/var/jenkins_home/workspace/DockerNode') {
                    script {
                        println("Getting commit id and latest Version")
                        _lastCommit = sh script: "git log | head -1 | awk '{print \$2}' | cut -c1-6", returnStdout: true
                        _latestVersion = sh script: "git branch -r | cut -d '/' -f2 | grep 0. | sort -r | head -1", returnStdout: true
                        lastCommit = _lastCommit.trim()
                        latestVersion = _latestVersion.trim()
                        println("Latest Version seen is ${latestVersion}")
                        sh "docker build -t davidgman/iplocation${latestVersion}-${lastCommit} ."
                        echo "Docker Image Build Successfully"
                    }
                }
            }
        }
        stage('Test Docker image') {
            steps {
                dir('/var/jenkins_home/workspace/DockerNode/BasicTest') {
                    script {
                        try {
                            sh "./basic.test.sh davidgman/iplocation${latestVersion}-${lastCommit}"
                        } catch (err) {
                            println("Error thrown on test file execution")
                            currentBuild.result = 'ABORTED'
                            error('Error thrown on test file execution')
                        }
                    }
                }
            }
        }
        stage('Upload image to DockerHub'){
            steps {
                sh "docker push davidgman/iplocation${latestVersion}-${lastCommit}"
            }
        }
         stage('Deploy as WebApp') {
            steps {
               script {
                   dir('/var/jenkins_home/workspace/DockerNode/') {
                       sh "python3 webapp.py -i 1.1.1.1 8.8.8.8"
                   }
               }

            }
        }
    }
}

