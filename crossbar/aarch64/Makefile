.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

default:
	@echo ""
	@echo "Targets:"
	@echo ""
	@echo "  build                  Build images"
	@echo "  test                   Test images"
	@echo "  version                Print CB version in images"
	@echo "  publish                Publish images"
	@echo ""


autobahn:
	cp ../../../autobahn-js-built/autobahn.* ./node/web/js/
	cp ../../../autobahn-js-built/CHECKSUM.* ./node/web/js/
	cp ../../../autobahn-js-built/LICENSE ./node/web/js/


build: build_community_cpy3 build_community_pypy3

build_community_cpy3:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build \
		-t crossbario/crossbar-armhf:latest \
		-t crossbario/crossbar-armhf:community-cpy3 \
		-t crossbario/crossbar-armhf:community-cpy3-17.3.1 \
		-f Dockerfile.community-cpy3 .

build_community_pypy3:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build \
		-v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static \
		-t crossbario/crossbar-armhf:community-pypy3 \
		-t crossbario/crossbar-armhf:community-pypy3-17.3.1 \
		-f Dockerfile.community-pypy3 .


test: test_community_cpy3 test_community_pypy3

test_community_cpy3:
	sudo docker run \
		-v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar-armhf:community-cpy3

test_community_pypy3:
	sudo docker run \
		-v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar-armhf:community-pypy3


version: version_community_cpy3 version_community_pypy3

version_community_cpy3:
	sudo docker run \
		-v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar-armhf:community-cpy3 version

version_community_pypy3:
	sudo docker run \
		-v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar-armhf:community-pypy3 version


publish: publish_community_cpy3 publish_community_pypy3

publish_community_cpy3: build_community_cpy3
	sudo docker push crossbario/crossbar-armhf:latest
	sudo docker push crossbario/crossbar-armhf:community-cpy3
	sudo docker push crossbario/crossbar-armhf:community-cpy3-17.3.1

publish_community_pypy3: build_community_pypy3
	sudo docker push crossbario/crossbar-armhf:community-pypy3
	sudo docker push crossbario/crossbar-armhf:community-pypy3-17.3.1


list:
	sudo docker images crossbario/crossbar-armhf

removeall:
	./removeall.sh
