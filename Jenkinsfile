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
                sh "/usr/local/bin/docker stop ${params.Name}"
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
                sh "/usr/loca/bin/docker run --detach --publish ${params.Port}:8080 --name ${params.Name} jenkins"
            }
        }
        stage('Finalize') {
            steps {
                echo "Waiting for jenkins process to start ..."
                waitUntil {
                    sh "/usr/local/bin/docker exec ${params.Name} cat /var/jenkins_home/secrets/initialAdminPassword"
                }
            }
        }
    }
}

/*
function jenkinsondocker() {
    docker stop jenkins || echo "Nothing to see here! :D"
    docker rm jenkins || echo "Nothing to see here! :D"
    docker pull jenkins
    echo "Waiting for Jenkins process to start ...."
    for i in {0..30};
    do
        echo -n "."
        sleep 1
    done
    echo
    echo -n "Here's the admin password!    "
    echo "Browse to http://localhost:49000"
}
*/
