#!/bin/bash
echo -n "# $(date) Waiting for Jenkins process to start ."
until code=$(curl -o /dev/null --silent --head --write-out '%{http_code}' http://127.0.0.1:60000) && ([ "$code" -eq 200 ] || [ "$code" -eq 403 ]); do
    echo -n '.';
    sleep 1
done

# ADMIN_PASS=$(docker exec jenkins-on-docker cat /var/jenkins_home/secrets/initialAdminPassword)
