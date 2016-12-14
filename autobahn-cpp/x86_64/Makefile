.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build: build_gcc build_clang

build_gcc:
	time sudo docker build \
		-t crossbario/autobahn-cpp \
		-t crossbario/autobahn-cpp:gcc \
		-t crossbario/autobahn-cpp:gcc-0.2.1 \
		-f Dockerfile.gcc .

build_clang:
	time sudo docker build \
		-t crossbario/autobahn-cpp:clang \
		-t crossbario/autobahn-cpp:clang-0.2.1 \
		-f Dockerfile.clang .

shell_gcc:
	sudo docker run -it --rm crossbario/autobahn-cpp-gcc bash

shell_clang:
	sudo docker run -it --rm crossbario/autobahn-cpp-clang bash

test_gcc:
	sudo docker run -it --rm crossbario/autobahn-cpp-gcc bash -c "cd /usr/local/app && make && ./client ws://$(HOSTIP):8080/ws realm1"

test_clang:
	sudo docker run -it --rm crossbario/autobahn-cpp-clang bash -c "cd /usr/local/app && make && ./client ws://$(HOSTIP):8080/ws realm1"

publish:
	sudo docker push crossbario/autobahn-cpp
	sudo docker push crossbario/autobahn-cpp:gcc
	sudo docker push crossbario/autobahn-cpp:gcc-0.2.1
	sudo docker push crossbario/autobahn-cpp:clang
	sudo docker push crossbario/autobahn-cpp:clang-0.2.1

list:
	sudo docker images

clean:
	-sudo docker rmi -f crossbario/autobahn-cpp*
