pipeline {
    agent { label 'master' }
    parameters {
        string(name: 'Name', defaultValue: 'jenkins', description: 'The name of the container that will run Jenkins')
        string(name: 'Port', defaultValue: '49000', description: 'The localhost port that will be attached to the container')
         booleanParam(name: 'Stop_Existing', defaultValue: true, description: 'Stop any containers that are running with the same name')
         booleanParam(name: 'Pull_Latest', defaultValue: true, description: 'Pull the lastest version of the Jenkins container image')
    }
    stages {
        stage('Stop Existing') {
            when { 
                expression { params.Stop_Existing == true }
            }
            steps {
                echo "Stopping exisiting container with name ${params.Name} ..."
                sh "/usr/local/bin/docker stop ${params.Name} || echo 'Nothing to stop'"
                sh "/usr/local/bin/docker rm ${params.Name} || echo 'Nothing to remove'"
            }
        }
        stage('Pull Latest') {
            when {
                expression { params.Pull_Latest == true }
            }
            steps {
                echo "Pulling lastet Jenkins container image"
                sh "/usr/local/bin/docker pull jenkins"
            }
        }
        stage('Run') {
            steps {
                echo "Running jenkins container ..."
                sh "/usr/local/bin/docker run --detach --publish ${params.Port}:8080 --name ${params.Name} jenkins"
            }
        }
        stage('Finalize') {
            steps {
                echo "Waiting for jenkins process to start ..."
                sleep 15
                script {
                    def initialAdminPassword = sh(script:  "/usr/local/bin/docker exec ${params.Name} cat /var/jenkins_home/secrets/initialAdminPassword", returnStdout: true).trim()
                    echo "Password is ${initialAdminPassword}\nBrowse to http://localhost:${params.Port}"
                }
            }
        }
    }
}
