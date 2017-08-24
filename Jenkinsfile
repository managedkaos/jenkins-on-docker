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
                // sh "/usr/local/bin/docker stop ${params.Name}"
            }
        }
        stage('Prepare') {
            when {
                expression { params.Pull_Existing == true }
            }
            steps {
                echo "Pull lastet Jenkins container image"
                // sh '/usr/local/bin/docker pull jenkins'
            }
        }
    }
}

/*
function jenkinsondocker() {
    docker stop jenkins || echo "Nothing to see here! :D"
    docker rm jenkins || echo "Nothing to see here! :D"
    docker pull jenkins
    docker run --detach --publish 49000:8080 --name jenkins jenkins
    echo "Waiting for Jenkins process to start ...."
    for i in {0..30};
    do
        echo -n "."
        sleep 1
    done
    echo
    echo -n "Here's the admin password!    "
    docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
    echo "Browse to http://localhost:49000"
}
*/
