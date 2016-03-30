.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

default:
	@echo "Targets: build, test, publish, .."

build:
	time sudo docker build -t crossbario/autobahn-js:full -f Dockerfile.full .
	time sudo docker build -t crossbario/autobahn-js:alpine crossbario/autobahn-js:latest -f Dockerfile.alpine .

version: node_version autobahn_version

node_version:
	sudo docker run -it --rm crossbario/autobahn-js:full node -v
	sudo docker run -it --rm crossbario/autobahn-js:alpine node -v

autobahn_version:
	sudo docker run -it --rm crossbario/autobahn-js:full sh -c "echo \"console.log('autobahn-' + require('autobahn').version + ' is installed');\" | node"
	sudo docker run -it --rm crossbario/autobahn-js:alpine sh -c "echo \"console.log('autobahn-' + require('autobahn').version + ' is installed');\" | node"

ping_full:
	sudo docker run --add-host=crossbar:$(HOSTIP) -it --rm crossbario/autobahn-js:full ping crossbar

ping_alpine:
	sudo docker run --add-host=crossbar:$(HOSTIP) -it --rm crossbario/autobahn-js:alpine ping crossbar

test: test_full test_alpine

test_full:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-js:full

test_alpine:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-js:alpine

publish:
	sudo docker push crossbario/autobahn-js:full
	sudo docker push crossbario/autobahn-js:alpine

list:
	sudo docker images
