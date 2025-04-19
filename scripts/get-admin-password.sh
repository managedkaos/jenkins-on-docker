#!/bin/bash
# This script retrieves the initial admin password for Jenkins running in a Docker container.

ADMIN_PASS=$(docker exec jenkins-on-docker cat /var/jenkins_home/secrets/initialAdminPassword)

echo
echo
echo
echo "Jenkins URL:"
echo "    http://localhost:60000"
echo
echo "Admin password:"
echo "    ${ADMIN_PASS}"
echo
echo "To run commands in the container as root:"
echo "    docker exec --user root -it jenkins-on-docker bash"

