.PHONY: crossbar autobahnjs

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

crossbar:
	sudo docker run -it -p 8080:8080 crossbario/crossbar

autobahnjs:
	sudo docker run -it crossbario/autobahn-js node /root/client.js ws://$(HOSTIP):8080/ws realm1

pull:
	sudo docker pull crossbario/crossbar
	sudo docker pull crossbario/autobahn-js
	sudo docker pull crossbario/autobahn-js:alpine
	sudo docker pull crossbario/autobahn-python:cpy2
	sudo docker pull crossbario/autobahn-python:cpy3
	sudo docker pull crossbario/autobahn-python:pypy2
	sudo docker pull crossbario/autobahn-python:cpy2-alpine
	sudo docker pull crossbario/autobahn-python:cpy3-alpine

docker:
	sudo apt-get install -y apt-transport-https ca-certificates
	sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
	sudo sh -c "echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' > /etc/apt/sources.list.d/docker.list"
	sudo apt-get update
	sudo apt-get purge lxc-docker
	sudo apt-cache policy docker-engine
	sudo apt-get install -y linux-image-extra-$$(uname -r)
	sudo apt-get install -y docker-engine
