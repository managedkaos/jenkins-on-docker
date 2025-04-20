#!/bin/bash

# configure jenkins
echo "# $(date) Configuring Jenkins..."
docker exec --user root jenkins-on-docker bash -c "apt update && apt install wget && which wget"

## download the list of plugins
echo "# $(date) Downloading the list of plugins..."
docker exec --user root jenkins-on-docker \
    wget -q https://raw.githubusercontent.com/jenkinsci/jenkins/master/core/src/main/resources/jenkins/install/platform-plugins.json

## get the suggested plugins
## note the 'grep -v name' hack to account for an error in processing the list
echo "# $(date) Using the keyword 'suggest' to find the suggested plugins in the list..."
docker exec --user root jenkins-on-docker \
    bash -c 'grep suggest platform-plugins.json | cut -d\" -f 4 | grep -v name | tee suggested-plugins.txt'

# include additional plugins
for i in dark-theme configuration-as-code;
do
    docker exec --user root jenkins-on-docker \
        bash -c "echo ${i} >> suggested-plugins.txt"
done

## download the plugin installation tool
echo "# $(date) Downloading the plugin installation tool"
docker exec --user root jenkins-on-docker \
    bash -c 'wget -q https://github.com/jenkinsci/plugin-installation-manager-tool/releases/download/2.13.0/jenkins-plugin-manager-2.13.0.jar'

## run the plugin installation tool
echo "# $(date) Running the plugin installation tool..."
docker exec --user root jenkins-on-docker \
    bash -c '/usr/bin/env java -jar ./jenkins-plugin-manager-2.13.0.jar \
    --verbose \
    --plugin-download-directory=/var/jenkins_home/plugins \
    --plugin-file=./suggested-plugins.txt | tee /var/log/plugin-installation.log'

cp ./jenkins-configuration.yaml $(pwd)/data_volume/userContent

# The container must be restarted to pick up the new configuration
echo "# $(date) Restarting Jenkins container..."
docker restart jenkins-on-docker

echo -n "# $(date) Waiting for Jenkins process to start ."
until [ $(curl -o /dev/null --silent --head --write-out '%{http_code}\n' http://127.0.0.1:60000) -eq 403 ]; do
    echo -n '.';
    sleep 1;
done

echo -e "\n# $(date) Plugin installation complete."
