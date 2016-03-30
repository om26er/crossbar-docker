.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build -t crossbario/crossbar:plus -f Dockerfile.plus .
	time sudo docker build -t crossbario/crossbar:community -t crossbario/crossbar:latest -f Dockerfile.community .

test: test_plus test_community

test_plus:
	sudo docker run --rm -it -p 8080:8080 --name crossbar crossbario/crossbar:plus

test_community:
	sudo docker run --rm -it -p 8080:8080 --name crossbar crossbario/crossbar:community

version: version_plus version_community

version_plus:
	sudo docker run --rm --entrypoint=/opt/crossbar/bin/crossbar -it crossbario/crossbar:plus version

version_community:
	sudo docker run --rm --entrypoint=/usr/local/bin/crossbar -it crossbario/crossbar:community version

publish: build
	sudo docker push crossbario/crossbar:latest
	sudo docker push crossbario/crossbar:plus
	sudo docker push crossbario/crossbar:community

list:
	sudo docker images
