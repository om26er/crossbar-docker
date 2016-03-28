.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	time sudo docker build -t crossbario/autobahn-cpp -f Dockerfile.gcc .

shell:
	sudo docker run -it crossbario/autobahn-cpp bash

test:
	sudo docker run -it crossbario/autobahn-cpp bash -c "cd /usr/local/app && make && ./client ws://$(HOSTIP):8080/ws realm1"

publish:
	sudo docker push crossbario/autobahn-cpp

list:
	sudo docker images
