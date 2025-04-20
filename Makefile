JENKINS_DATA = $(shell pwd)/data_volume

help:
	echo hello

development-requirements: requirements
	@pip install --requirement .development-requirements.txt

requirements:
	@pip install --requirement requirements.txt

all: pull start-jenkins install-plugins get-admin-password go

pull:
	docker pull jenkins/jenkins:lts

start-jenkins:
	@echo "# $(shell date) Starting Jenkins container..."
	@if [ ! -d $(JENKINS_DATA) ]; then mkdir -p $(JENKINS_DATA); fi
	-@docker run --detach \
		--volume $(JENKINS_DATA):/var/jenkins_home \
		--restart always \
		--publish 60000:8080 \
		--name jenkins-on-docker \
		jenkins/jenkins:lts || \
		printf "\nIs the container already running?\n\n"
	@./scripts/wait-for-jenkins.sh

install-plugins:
	@./scripts/install-plugins.sh

get-admin-password:
	-@./scripts/get-admin-password.sh

go:
	@echo "# http://localhost:60000"
	@open http://localhost:60000

exec:
	-@docker exec -it jenkins-on-docker bash

root-exec:
	-@docker exec -it --user root jenkins-on-docker bash

stop-jenkins:
	-@docker stop jenkins-on-docker || \
		printf "Is the container already stopped?\n\n"

clean: stop-jenkins
	-@docker rm jenkins-on-docker || \
		printf "Is the container already removed?\n\n"

nuke: clean
	-@rm -rf $(JENKINS_DATA) || \
		printf "Is the data directory already removed?\n\n"

.PHONY: help development-requirements requirements all pull start-jenkins install-plugins get-admin-password go exec root-exec stop-jenkins clean nuke
