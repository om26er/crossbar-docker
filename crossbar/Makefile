#
# CROSSBAR_VERSION must be set, eg to '17.3.1'.
#
# Get the Git commit fingerprint of the tagged release, and
# get the current day as build date for the image:
#


default:
	@echo ""
	@echo "Targets:"
	@echo ""
	@echo "  params                 Print build parameter"
	@echo "  build                  Build images"
	@echo "  version                Print version of images"
	@echo "  test                   Test images"
	@echo "  publish                Publish images"
	@echo ""


#
# Print build parameters
#
params:
	@echo "${CROSSBAR_VERSION}"
	@echo "${CROSSBAR_VCS_REF}"
	@echo "${BUILD_DATE}"



#
# BUILD
#
build: build_community

build_community: build_community_cpy3 build_community_pypy3


#
# BUILD: Community / CPython 3
#
build_community_cpy3: build_amd64_community_cpy3 build_armhf_community_cpy3 build_aarch64_community_cpy3

build_amd64_community_cpy3:
	# enforce auto-generating a new key when using the images
	rm -f node/.crossbar/node.key
	time docker build \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%d"` \
		--build-arg CROSSBAR_VCS_REF=${CROSSBAR_VCS_REF} \
		--build-arg CROSSBAR_VERSION=${CROSSBAR_VERSION} \
		-t crossbario/crossbar:latest \
		-t crossbario/crossbar:${CROSSBAR_VERSION} \
		-t crossbario/crossbar:community \
		-t crossbario/crossbar:community-${CROSSBAR_VERSION} \
		-t crossbario/crossbar:community-cpy3 \
		-t crossbario/crossbar:community-cpy3-${CROSSBAR_VERSION} \
		-f ./x86_64/Dockerfile.community-cpy3 .

build_armhf_community_cpy3:
	# enforce auto-generating a new key when using the images
	rm -f node/.crossbar/node.key
	time docker build \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%d"` \
		--build-arg CROSSBAR_VCS_REF=${CROSSBAR_VCS_REF} \
		--build-arg CROSSBAR_VERSION=${CROSSBAR_VERSION} \
		-t crossbario/crossbar-armhf:latest \
		-t crossbario/crossbar-armhf:community \
		-t crossbario/crossbar-armhf:community-cpy3 \
		-t crossbario/crossbar-armhf:community-cpy3-${CROSSBAR_VERSION} \
		-f ./armhf/Dockerfile.community-cpy3 .

build_aarch64_community_cpy3:
	# enforce auto-generating a new key when using the images
	rm -f node/.crossbar/node.key
	time docker build \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%d"` \
		--build-arg CROSSBAR_VCS_REF=${CROSSBAR_VCS_REF} \
		--build-arg CROSSBAR_VERSION=${CROSSBAR_VERSION} \
		-t crossbario/crossbar-aarch64:latest \
		-t crossbario/crossbar-aarch64:community \
		-t crossbario/crossbar-aarch64:community-cpy3 \
		-t crossbario/crossbar-aarch64:community-cpy3-${CROSSBAR_VERSION} \
		-f ./aarch64/Dockerfile.community-cpy3 .


#
# BUILD: Community / PyPy 3
#
build_community_pypy3: build_amd64_community_pypy3 build_armhf_community_pypy3 build_aarch64_community_pypy3

build_amd64_community_pypy3:
	# enforce auto-generating a new key when using the images
	rm -f node/.crossbar/node.key
	time docker build \
		--build-arg BUILD_DATE=`date -u +"%Y-%m-%d"` \
		--build-arg CROSSBAR_VCS_REF=${CROSSBAR_VCS_REF} \
		--build-arg CROSSBAR_VERSION=${CROSSBAR_VERSION} \
		-t crossbario/crossbar:community-pypy3 \
		-t crossbario/crossbar:community-pypy3-${CROSSBAR_VERSION} \
		-f ./x86_64/Dockerfile.community-pypy3 .

build_armhf_community_pypy3:
	@echo "PyPy3 isn't available for armhf yet"

build_aarch64_community_pypy3:
	@echo "PyPy3 isn't available for aarch64 yet"


#
# VERSION: Community / CPython 3
#
version: version_community

version_community: version_community_cpy3 version_community_pypy3

version_community_cpy3: version_amd64_community_cpy3 version_armhf_community_cpy3 version_aarch64_community_cpy3

version_amd64_community_cpy3:
	docker run \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar:community-cpy3 version

version_armhf_community_cpy3:
	docker run \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar-armhf:community-cpy3 version

version_aarch64_community_cpy3:
	docker run \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar-aarch64:community-cpy3 version


#
# VERSION: Community / PyPy 3
#
version_community_pypy3: version_amd64_community_pypy3 version_armhf_community_pypy3 version_aarch64_community_pypy3

version_amd64_community_pypy3:
	docker run \
		--rm --entrypoint=/usr/local/bin/crossbar -it \
		crossbario/crossbar:community-pypy3 version

version_armhf_community_pypy3:
	@echo "PyPy3 isn't available for armhf yet"

version_aarch64_community_pypy3:
	@echo "PyPy3 isn't available for aarch64 yet"


test: test_community

test_community: test_community_cpy3 test_community_pypy3

#
# TEST: Community / CPython 3
#
test_community_cpy3: test_amd64_community_cpy3 test_armhf_community_cpy3 test_aarch64_community_cpy3

test_amd64_community_cpy3:
	docker run \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar:community-cpy3

test_armhf_community_cpy3:
	docker run \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar-armhf:community-cpy3

test_aarch64_community_cpy3:
	docker run \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar-aarch64:community-cpy3


#
# TEST: Community / PyPy 3
#
test_community_pypy3: test_amd64_community_pypy3 test_armhf_community_pypy3 test_aarch64_community_pypy3

test_amd64_community_pypy3:
	docker run \
		--rm -it -p 8080:8080 --name crossbar \
		crossbario/crossbar:community-pypy3

test_armhf_community_pypy3:
	@echo "PyPy3 isn't available for armhf yet"

test_aarch64_community_pypy3:
	@echo "PyPy3 isn't available for aarch64 yet"


publish: publish_community

publish_community: build_community
	# amd64 / community / cpy3
	docker push crossbario/crossbar:latest
	docker push crossbario/crossbar:community
	docker push crossbario/crossbar:community-cpy3
	docker push crossbario/crossbar:community-cpy3-${CROSSBAR_VERSION}

	# armhf / community / cpy3
	docker push crossbario/crossbar-armhf:latest
	docker push crossbario/crossbar-armhf:community
	docker push crossbario/crossbar-armhf:community-cpy3
	docker push crossbario/crossbar-armhf:community-cpy3-${CROSSBAR_VERSION}

	# aarch64 / community / cpy3
	docker push crossbario/crossbar-aarch64:latest
	docker push crossbario/crossbar-aarch64:community
	docker push crossbario/crossbar-aarch64:community-cpy3
	docker push crossbario/crossbar-aarch64:community-cpy3-${CROSSBAR_VERSION}

	# amd64 / community / pypy3
	docker push crossbario/crossbar:community-pypy3
	docker push crossbario/crossbar:community-pypy3-${CROSSBAR_VERSION}


#
# Install Qemu (this is needed for cross-building armhf/aarch64 on amd64)
#
qemu_deps:
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
	-docker images crossbario/crossbar*

#
# Remove all images !!!
#
clean:
	./removeall.sh
