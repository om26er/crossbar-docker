.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	docker build \
		-t crossbario/autobahn-java \
		-t crossbario/autobahn-java:latest \
		-f Dockerfile.Android .

run:
	docker run \
		--volume ${PWD}/../../autobahn-java:/workspace/ autobahn-java
	echo "Generated: ../../autobahn-java/demo-gallery/build/outputs/apk/demo-gallery-release-unsigned.apk"

clean:
	./removeall.sh

list:
	docker images -q crossbario/autobahn-java:*
