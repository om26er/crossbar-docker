.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

default:
	@echo "Targets: build, test, publish, .."

build:
	time docker build \
		--build-arg AUTOBAHN_JS_VERSION=${AUTOBAHN_JS_VERSION} \
		-t crossbario/autobahn-js:full \
		-t crossbario/autobahn-js:full-${AUTOBAHN_JS_VERSION} \
		-f Dockerfile.full .
	time docker build \
		-t crossbario/autobahn-js \
		-t crossbario/autobahn-js:alpine \
		-t crossbario/autobahn-js:alpine-${AUTOBAHN_JS_VERSION} \
		-f Dockerfile.alpine .

version: node_version autobahn_version

node_version:
	docker run -it --rm crossbario/autobahn-js:full node -v
	docker run -it --rm crossbario/autobahn-js:alpine node -v

autobahn_version:
	docker run -it --rm crossbario/autobahn-js:full sh -c "echo \"console.log('autobahn-' + require('autobahn').version + ' is installed');\" | node"
	docker run -it --rm crossbario/autobahn-js:alpine sh -c "echo \"console.log('autobahn-' + require('autobahn').version + ' is installed');\" | node"

ping_full:
	docker run --add-host=crossbar:$(HOSTIP) -it --rm crossbario/autobahn-js:full ping crossbar

ping_alpine:
	docker run --add-host=crossbar:$(HOSTIP) -it --rm crossbario/autobahn-js:alpine ping crossbar

test: test_full test_alpine

test_full:
	docker run -it --rm --link crossbar crossbario/autobahn-js:full

test_alpine:
	docker run -it --rm --link crossbar crossbario/autobahn-js:alpine

publish: build
	docker push crossbario/autobahn-js
	docker push crossbario/autobahn-js:alpine
	docker push crossbario/autobahn-js:alpine-${AUTOBAHN_JS_VERSION}
	docker push crossbario/autobahn-js:full
	docker push crossbario/autobahn-js:full-${AUTOBAHN_JS_VERSION}

list:
	docker images

clean:
	-docker rmi -f crossbario/autobahn-js*
