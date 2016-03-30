.PHONY: crossbar autobahnjs

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

# run this to start a test Crossbar.io container
crossbar:
	sudo docker run -it -p 8080:8080 --name crossbar --rm crossbario/crossbar

# run this to test all Autobahn flavors against above Crossbar.io sequentially
autobahn: autobahnjs autobahnjs_alpine \
		  autobahncpp_gcc autobahncpp_clang \
	      autobahnpython_cpy2 autobahnpython_cpy3 autobahnpython_pypy2 autobahnpython_cpy2_alpine autobahnpython_cpy3_alpine

autobahncpp_gcc:
	sudo docker run -it sh -c "cd /usr/local/app/ && make && crossbario/autobahn-cpp:gcc /usr/local/app/client ws://$(HOSTIP):8080/ws realm1"

autobahncpp_clang:
	sudo docker run -it sh -c "cd /usr/local/app/ && make && crossbario/autobahn-cpp:clang /usr/local/app/client ws://$(HOSTIP):8080/ws realm1"

autobahnjs:
	sudo docker run -it crossbario/autobahn-js node /root/client.js ws://$(HOSTIP):8080/ws realm1

autobahnjs_alpine:
	sudo docker run -it crossbario/autobahn-js:alpine node /root/client.js ws://$(HOSTIP):8080/ws realm1

autobahnpython_cpy2:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy2

autobahnpython_cpy3:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy3

autobahnpython_pypy2:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:pypy2

autobahnpython_cpy2_alpine:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy2-alpine

autobahnpython_cpy3_alpine:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy2-alpine

autobahnpython_cpy3_minimal:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy3-minimal

# pull all our images
pull:
	sudo docker pull crossbario/crossbar:latest
	sudo docker pull crossbario/autobahn-cpp:latest
	#sudo docker pull crossbario/autobahn-cpp:gcc
	#sudo docker pull crossbario/autobahn-cpp:clang
	sudo docker pull crossbario/autobahn-js:latest
	sudo docker pull crossbario/autobahn-js:full
	sudo docker pull crossbario/autobahn-js:alpine
	#sudo docker pull crossbario/autobahn-python:latest
	sudo docker pull crossbario/autobahn-python:cpy2
	sudo docker pull crossbario/autobahn-python:cpy3
	sudo docker pull crossbario/autobahn-python:pypy2
	sudo docker pull crossbario/autobahn-python:cpy2-alpine
	#sudo docker pull crossbario/autobahn-python:cpy3-alpine
	#sudo docker pull crossbario/autobahn-python:cpy3-minimal

requirements: docker docker_compose

# install docker
docker:
	sudo apt-get install -y apt-transport-https ca-certificates
	sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
	sudo sh -c "echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' > /etc/apt/sources.list.d/docker.list"
	sudo apt-get update
	sudo apt-get purge lxc-docker
	sudo apt-cache policy docker-engine
	sudo apt-get install -y linux-image-extra-$$(uname -r)
	sudo apt-get install -y docker-engine

# install docker compose (see: https://github.com/docker/compose/releases)
docker_compose:
	sudo sh -c "curl -L https://github.com/docker/compose/releases/download/1.7.0-rc1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"
	sudo chmod +x /usr/local/bin/docker-compose

# http://jimhoskins.com/2013/07/27/remove-untagged-docker-images.html
clean:
	#sudo docker rm $(sudo docker ps -a -q)
	sudo docker rmi -f $$(sudo docker images | grep "^<none>" | awk "{print $$3}")

list:
	sudo docker images
