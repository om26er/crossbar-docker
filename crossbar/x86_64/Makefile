.PHONY: crossbar crossbar_dev client client_dev

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')
REPOS=../..

build:
	rm -f .crossbar/node.key
	time sudo docker build --no-cache -t crossbario/crossbar .

test:
	sudo docker run -it -p 8080:8080 crossbario/crossbar

publish:
	sudo docker push crossbario/crossbar

start:
	sudo docker run --entrypoint=/opt/crossbar/bin/crossbar -it -p 8080:8080 crossbario/crossbar start --cbdir /var/crossbar/.crossbar

version:
	sudo docker run --entrypoint=/opt/crossbar/bin/crossbar -it crossbario/crossbar version

list:
	sudo docker images

crossbar:
	# FIXME: the Docker image runs Crossbar.io under user "daemon" - make sure it can write
	sudo chown -R daemon:daemon node
	sudo docker run \
		-v ${PWD}/node:/var/crossbar \
		-p 8080:8080 \
		-it crossbario/crossbar
