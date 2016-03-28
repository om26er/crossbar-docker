.PHONY: crossbar autobahnjs

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

# run this to start a test Crossbar.io container
crossbar:
	sudo docker run -it -p 8080:8080 crossbario/crossbar

# run this to test all Autobahn flavors against above Crossbar.io sequentially
autobahn: autobahnjs autobahnjs_alpine \
	      autobahnpython_cpy2 autobahnpython_cpy3 autobahnpython_pypy2 autobahnpython_cpy2_alpine autobahnpython_cpy3_alpine

autobahnjs:
	sudo docker run -it crossbario/autobahn-js node /root/client.js ws://$(HOSTIP):8080/ws realm1

autobahnjs_alpine:
	sudo docker run -it crossbario/autobahn-js:alpine node /root/client.js ws://$(HOSTIP):8080/ws realm1

autobahnpython_cpy2:
	sudo docker run -it crossbario/autobahn-python:cpy2 python /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

autobahnpython_cpy3:
	sudo docker run -it crossbario/autobahn-python:cpy3 python /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

autobahnpython_pypy2:
	sudo docker run -it crossbario/autobahn-python:pypy2 pypy /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

autobahnpython_cpy2_alpine:
	sudo docker run -it crossbario/autobahn-python:cpy2-alpine python /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

autobahnpython_cpy3_alpine:
	sudo docker run -it crossbario/autobahn-python:cpy3-alpine python /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

# pull all our images
pull:
	sudo docker pull crossbario/crossbar
	sudo docker pull crossbario/autobahn-js
	sudo docker pull crossbario/autobahn-js:alpine
	sudo docker pull crossbario/autobahn-python:cpy2
	sudo docker pull crossbario/autobahn-python:cpy3
	sudo docker pull crossbario/autobahn-python:pypy2
	sudo docker pull crossbario/autobahn-python:cpy2-alpine
	sudo docker pull crossbario/autobahn-python:cpy3-alpine

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
