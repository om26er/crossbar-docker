.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')


build: build_plus build_community

build_plus:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build -t crossbario/crossbar:plus -f Dockerfile.plus .

build_community:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
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


publish: publish_plus publish_community

publish_plus: build_plus
	sudo docker push crossbario/crossbar:plus

publish_community: build_community
	sudo docker push crossbario/crossbar:latest
	sudo docker push crossbario/crossbar:community


list:
	sudo docker images
