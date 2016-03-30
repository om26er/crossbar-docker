.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	time sudo docker build -t crossbario/autobahn-cpp:gcc -f Dockerfile.gcc .
	#time sudo docker build -t crossbario/autobahn-cpp:clang -f Dockerfile.clang .

shell_gcc:
	sudo docker run -it --rm crossbario/autobahn-cpp:gcc bash

shell_clang:
	sudo docker run -it --rm crossbario/autobahn-cpp:clang bash

test_gcc:
	sudo docker run -it --rm crossbario/autobahn-cpp bash -c "cd /usr/local/app && make && ./client ws://$(HOSTIP):8080/ws realm1"

publish:
	sudo docker push crossbario/autobahn-cpp:gcc
	#sudo docker push crossbario/autobahn-cpp:clang

list:
	sudo docker images
