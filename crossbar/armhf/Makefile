.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

default:
	@echo ""
	@echo "Targets:"
	@echo ""
	@echo "  build                  Build plus + community images"
	@echo "  build_plus             Build plus image"
	@echo "  build_community        Build community image"
	@echo "  test                   Test plus + community images"
	@echo "  test_plus              Test plus image"
	@echo "  test_community         Test community image"
	@echo "  version                Get CB version in plus + community images"
	@echo "  version_plus           Get CB version in plus image"
	@echo "  version_community      Get CB version in community image"
	@echo "  publish                Publish plus + community images"
	@echo "  publish_plus           Publish plus image"
	@echo "  publish_community      Publish community image"
	@echo ""

build: build_plus build_community build_community_pypy

build_plus:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	sudo docker build \
		-t crossbario/crossbar-armhf:plus \
		-t crossbario/crossbar-armhf:plus-17.3.1 \
		-f Dockerfile.plus .

build_community:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	sudo docker build \
		-t crossbario/crossbar-armhf:latest \
		-t crossbario/crossbar-armhf:community \
		-t crossbario/crossbar-armhf:community-17.3.1 \
		-f Dockerfile.community .

build_community_pypy:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	sudo docker build \
		-t crossbario/crossbar-armhf:community-pypy \
		-t crossbario/crossbar-armhf:community-pypy-17.3.1 \
		-f Dockerfile.community.pypy .


test: test_plus test_community test_community_pypy

test_plus:
	sudo docker run --rm -it -p 8080:8080 --name crossbar crossbario/crossbar-armhf:plus

test_community:
	sudo docker run --rm -it -p 8080:8080 --name crossbar crossbario/crossbar-armhf:community

test_community_pypy:
	sudo docker run --rm -it -p 8080:8080 --name crossbar crossbario/crossbar-armhf:community-pypy


version: version_plus version_community version_community_pypy

version_plus:
	sudo docker run --rm --entrypoint=/opt/crossbar/bin/crossbar -it crossbario/crossbar-armhf:plus version

version_community:
	sudo docker run --rm --entrypoint=/usr/local/bin/crossbar -it crossbario/crossbar-armhf:community version

version_community_pypy:
	sudo docker run --rm --entrypoint=/usr/local/bin/crossbar -it crossbario/crossbar-armhf:community-pypy version


publish: publish_plus publish_community

publish_plus: build_plus
	sudo docker push crossbario/crossbar-armhf:plus

publish_community: build_community
	sudo docker push crossbario/crossbar-armhf:latest
	sudo docker push crossbario/crossbar-armhf:community
	sudo docker push crossbario/crossbar-armhf:community-17.3.1

publish_community_pypy: build_community_pypy
	sudo docker push crossbario/crossbar-armhf:community-pypy
	sudo docker push crossbario/crossbar-armhf:community-pypy-17.3.1

list:
	sudo docker images
