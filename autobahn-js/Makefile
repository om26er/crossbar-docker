.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	time sudo docker build --no-cache -t crossbario/autobahn-js -f Dockerfile .
	time sudo docker build --no-cache -t crossbario/autobahn-js:alpine -f Dockerfile.alpine .
	time sudo docker build --no-cache -t crossbario/autobahn-js:alpine-node-only -f Dockerfile.alpine.node-only .

version: node_version autobahn_version

node_version:
	sudo docker run -it crossbario/autobahn-js node -v
	sudo docker run -it crossbario/autobahn-js:alpine node -v

autobahn_version:
	sudo docker run -it crossbario/autobahn-js sh -c "echo \"console.log('autobahn-' + require('autobahn').version + ' is installed');\" | node"
	sudo docker run -it crossbario/autobahn-js:alpine sh -c "echo \"console.log('autobahn-' + require('autobahn').version + ' is installed');\" | node"

ping:
	sudo docker run --add-host=crossbar:$(HOSTIP) -it crossbario/autobahn-js ping crossbar

ping_alpine:
	sudo docker run --add-host=crossbar:$(HOSTIP) -it crossbario/autobahn-js:alpine ping crossbar

test:
	sudo docker run -it crossbario/autobahn-js node /root/client.js ws://$(HOSTIP):8080/ws realm1

test_alpine:
	sudo docker run -it crossbario/autobahn-js:alpine node /root/client.js ws://$(HOSTIP):8080/ws realm1

publish:
	sudo docker push crossbario/autobahn-js
	sudo docker push crossbario/autobahn-js:alpine

list:
	sudo docker images
