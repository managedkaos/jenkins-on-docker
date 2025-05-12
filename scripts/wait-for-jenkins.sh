#!/bin/bash
echo -n "# $(date) Waiting for Jenkins process to start ."
until [ $(curl -o /dev/null --silent --head --write-out '%{http_code}\n' http://127.0.0.1:60000) -eq 403 ]; do
    echo -n '.';
    sleep 1;
done

# ADMIN_PASS=$(docker exec jenkins-on-docker cat /var/jenkins_home/secrets/initialAdminPassword)
