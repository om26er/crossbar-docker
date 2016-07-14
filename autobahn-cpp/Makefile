.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

# https://github.com/crossbario/crossbar-docker/issues/25
#build: build_gcc build_clang
build: build_gcc

build_gcc:
	time sudo docker build \
		-t crossbario/autobahn-cpp \
		-t crossbario/autobahn-cpp:0.2.0 \
		-t crossbario/autobahn-cpp-gcc \
		-t crossbario/autobahn-cpp-gcc:0.2.0 \
		-f Dockerfile.gcc .

build_clang:
	time sudo docker build \
		-t crossbario/autobahn-cpp-clang \
		-t crossbario/autobahn-cpp-clang:0.2.0 \
		-f Dockerfile.clang .

shell_gcc:
	sudo docker run -it --rm crossbario/autobahn-cpp-gcc bash

shell_clang:
	sudo docker run -it --rm crossbario/autobahn-cpp-clang bash

test_gcc:
	sudo docker run -it --rm crossbario/autobahn-cpp-gcc bash -c "cd /usr/local/app && make && ./client ws://$(HOSTIP):8080/ws realm1"

publish:
	sudo docker push crossbario/autobahn-cpp-gcc
	#sudo docker push crossbario/autobahn-cpp-clang

list:
	sudo docker images

clean:
	sudo docker rmi crossbario/autobahn-cpp*
