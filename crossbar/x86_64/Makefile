.PHONY: crossbar crossbar_dev client client_dev

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')
REPOS=../..

build:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build -t crossbario/crossbar:plus -f Dockerfile.plus .
	time sudo docker build -t crossbario/crossbar:community -t crossbario/crossbar:latest -f Dockerfile.community .

test_plus:
	sudo docker run --rm -it -p 8080:8080 --name crossbar crossbario/crossbar:plus

test_community:
	sudo docker run --rm -it -p 8080:8080 --name crossbar crossbario/crossbar:community

publish: build
	sudo docker push crossbario/crossbar:latest
	sudo docker push crossbario/crossbar:plus
	sudo docker push crossbario/crossbar:community

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
		--name crossbar \
		--rm \
		-p 8080:8080 \
		-it crossbario/crossbar
