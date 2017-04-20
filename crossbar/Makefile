

# export CROSSBAR_VERSION='17.3.1'

#
# replacing teh base image from command line (the part after FROM)
# is possible only with docker >= 17.05
# https://github.com/moby/moby/issues/6822#issuecomment-293317857
#

default:
	@echo ""
	@echo "Targets:"
	@echo ""
	@echo "  build                  Build images"
	@echo "  test                   Test images"
	@echo "  version                Print CB version in images"
	@echo "  publish                Publish images"
	@echo ""


#
# BUILD / VERSION / TEST: Community, all flavors
#
build_community: build_community_cpy3 build_community_pypy3

version_community: version_community_cpy3 version_community_pypy3

test_community: test_community_cpy3 test_community_pypy3


#
# BUILD: Community / CPython 3
#
build_community_cpy3: build_amd64_community_cpy3 build_armhf_community_cpy3 build_aarch64_community_cpy3

build_amd64_community_cpy3:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build \
		--build-arg CROSSBAR_VERSION=${CROSSBAR_VERSION} \
		-t crossbario/crossbar:latest \
		-t crossbario/crossbar:community-cpy3 \
		-t crossbario/crossbar:community-cpy3-${CROSSBAR_VERSION}\
		-f Dockerfile.amd64-community-cpy3 .

build_armhf_community_cpy3:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build \
		--build-arg CROSSBAR_VERSION=${CROSSBAR_VERSION} \
		-t crossbario/crossbar-armhf:latest \
		-t crossbario/crossbar-armhf:community-cpy3 \
		-t crossbario/crossbar-armhf:community-cpy3-${CROSSBAR_VERSION}\
		-f Dockerfile.armhf-community-cpy3 .

build_aarch64_community_cpy3:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build \
		--build-arg CROSSBAR_VERSION=${CROSSBAR_VERSION} \
		-t crossbario/crossbar-aarch64:latest \
		-t crossbario/crossbar-aarch64:community-cpy3 \
		-t crossbario/crossbar-aarch64:community-cpy3-${CROSSBAR_VERSION}\
		-f Dockerfile.aarch64-community-cpy3 .


#
# BUILD: Community / PyPy 3
#
build_community_pypy3: build_amd64_community_pypy3 build_armhf_community_pypy3 build_aarch64_community_pypy3

build_amd64_community_pypy3:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build \
		--build-arg CROSSBAR_VERSION=${CROSSBAR_VERSION} \
		-t crossbario/crossbar:latest \
		-t crossbario/crossbar:community-pypy3 \
		-t crossbario/crossbar:community-pypy3-${CROSSBAR_VERSION}\
		-f Dockerfile.amd64-community-pypy3 .

build_armhf_community_pypy3:
	@echo "PyPy3 isn't available for armhf yet"

build_aarch64_community_pypy3:
	@echo "PyPy3 isn't available for aarch64 yet"


#
# VERSION: Community / CPython 3
#
version_community_cpy3: version_amd64_community_cpy3 version_armhf_community_cpy3 version_aarch64_community_cpy3

version_amd64_community_cpy3:
	sudo docker run \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar:community-cpy3 version

version_armhf_community_cpy3:
	sudo docker run \
		-v ./.qemu/qemu-arm-static:/usr/bin/qemu-arm-static \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar-armhf:community-cpy3 version

version_aarch64_community_cpy3:
	sudo docker run \
		-v ./.qemu/qemu-aarch64-static:/usr/bin/qemu-aarch64-static \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar-aarch64:community-cpy3 version


#
# VERSION: Community / PyPy 3
#
version_community_pypy3: version_amd64_community_pypy3 version_armhf_community_pypy3 version_aarch64_community_pypy3

version_amd64_community_pypy3:
	sudo docker run \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar:community-pypy3 version

version_armhf_community_pypy3:
	@echo "PyPy3 isn't available for armhf yet"

version_aarch64_community_pypy3:
	@echo "PyPy3 isn't available for aaarch64 yet"


#
# TEST: Community / CPython 3
#
test_community_cpy3: test_amd64_community_cpy3 test_armhf_community_cpy3 test_aarch64_community_cpy3

test_amd64_community_cpy3:
	sudo docker run \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar:community-cpy3

test_armhf_community_cpy3:
	sudo docker run \
		-v ./.qemu/qemu-arm-static:/usr/bin/qemu-arm-static \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar-armhf:community-cpy3

test_aarch64_community_cpy3:
	sudo docker run \
		-v ./.qemu/qemu-aarch64-static:/usr/bin/qemu-aarch64-static \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar-aarch64:community-cpy3


#
# TEST: Community / PyPy 3
#
test_community_cpy3: test_amd64_community_pypy3 test_armhf_community_pypy3 test_aarch64_community_pypy3

test_amd64_community_pypy3:
	sudo docker run \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar:community-pypy3

test_armhf_community_pypy3:
	sudo docker run \
		-v ./.qemu/qemu-arm-static:/usr/bin/qemu-arm-static \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar-armhf:community-pypy3

test_aarch64_community_pypy3:
	sudo docker run \
		-v ./.qemu/qemu-aarch64-static:/usr/bin/qemu-aarch64-static \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar-aarch64:community-pypy3

#
# Install Qemu (this is needed for cross-building armhf/aarch64 on amd64)
#
qemu_deps:
	sudo apt-get update
	sudo apt-get install -y --no-install-recommends qemu-user-static binfmt-support
	sudo update-binfmts --enable qemu-arm
	sudo update-binfmts --enable qemu-aarch64
	sudo update-binfmts --display qemu-arm
	sudo update-binfmts --display qemu-aarch64
	mkdir -p ./.qemu
	cp /usr/bin/qemu-aarch64-static ./.qemu
	cp /usr/bin/qemu-arm-static ./.qemu


#
# Copy over current AutobahnJS into the default node directory
# we bake into the images
#
autobahn:
	cp ../../autobahn-js-built/autobahn.* ./node/web/js/
	cp ../../autobahn-js-built/CHECKSUM.* ./node/web/js/
	cp ../../autobahn-js-built/LICENSE ./node/web/js/

#
# List all images
#
list:
	sudo docker images crossbario/crossbar*

#
# WARNING: this will destroy ALL your images AND containers!
#
removeall:
	./removeall.sh
