.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	sudo docker build \
		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
		-t crossbario/autobahn-python-aarch64:cpy2 \
		-t crossbario/autobahn-python-aarch64:cpy2-${AUTOBAHN_PYTHON_VERSION} \
		-f Dockerfile.cpy2 .

	sudo docker build \
		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
		-t crossbario/autobahn-python-aarch64:latest \
		-t crossbario/autobahn-python-aarch64:cpy3 \
		-t crossbario/autobahn-python-aarch64:cpy3-${AUTOBAHN_PYTHON_VERSION} \
		-f Dockerfile.cpy3 .

#	sudo docker build \
#		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
#		-t crossbario/autobahn-python-aarch64:pypy2 \
#		-t crossbario/autobahn-python-aarch64:pypy2-${AUTOBAHN_PYTHON_VERSION} \
#		-f Dockerfile.pypy2 .
#
#	sudo docker build \
#		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
#		-t crossbario/autobahn-python-aarch64:pypy3 \
#		-t crossbario/autobahn-python-aarch64:pypy3-${AUTOBAHN_PYTHON_VERSION} \
#		-f Dockerfile.pypy3 .

#	sudo docker build \
#		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
#		-t crossbario/autobahn-python-aarch64:cpy2-alpine \
#		-t crossbario/autobahn-python-aarch64:cpy2-alpine-${AUTOBAHN_PYTHON_VERSION} \
#		-f Dockerfile.cpy2-alpine .
#
#	sudo docker build \
#		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
#		-t crossbario/autobahn-python-aarch64:latest \
#		-t crossbario/autobahn-python-aarch64:cpy3-alpine \
#		-t crossbario/autobahn-python-aarch64:cpy3-alpine-${AUTOBAHN_PYTHON_VERSION} \
#		-f Dockerfile.cpy3-alpine .

	sudo docker build \
		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
		-t crossbario/autobahn-python-aarch64:cpy2-minimal-aio \
		-t crossbario/autobahn-python-aarch64:cpy2-minimal-aio-${AUTOBAHN_PYTHON_VERSION} \
		-f Dockerfile.cpy2-minimal-aio .

	sudo docker build \
		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
		-t crossbario/autobahn-python-aarch64:cpy3-minimal-aio \
		-t crossbario/autobahn-python-aarch64:cpy3-minimal-aio-${AUTOBAHN_PYTHON_VERSION} \
		-f Dockerfile.cpy3-minimal-aio .

	sudo docker build \
		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
		-t crossbario/autobahn-python-aarch64:cpy2-minimal-tx \
		-t crossbario/autobahn-python-aarch64:cpy2-minimal-tx-${AUTOBAHN_PYTHON_VERSION} \
		-f Dockerfile.cpy2-minimal-tx .

	sudo docker build \
		--build-arg AUTOBAHN_PYTHON_VERSION=${AUTOBAHN_PYTHON_VERSION} \
		-t crossbario/autobahn-python-aarch64:cpy3-minimal-tx \
		-t crossbario/autobahn-python-aarch64:cpy3-minimal-tx-${AUTOBAHN_PYTHON_VERSION} \
		-f Dockerfile.cpy3-minimal-tx .

version: os_version python_version autobahn_version

os_version:
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2 uname -a
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3 uname -a
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:pypy2 uname -a
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:pypy3 uname -a
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-alpine uname -a
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-alpine uname -a
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-minimal-aio uname -a
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-minimal-aio uname -a
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-minimal-tx uname -a
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-minimal-tx uname -a

python_version:
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2 python -V
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3 python -V
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:pypy2 python -V
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:pypy3 python -V
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-alpine python -V
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-alpine python -V
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-minimal-aio python -V
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-minimal-aio python -V
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-minimal-tx python -V
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-minimal-tx python -V

autobahn_version:
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:pypy2 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:pypy3 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
#	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-minimal-aio python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-minimal-aio python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy2-minimal-tx python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-aarch64:cpy3-minimal-tx python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"

test: test_cpy2 test_cpy3 test_pypy2 test_pypy3 test_cpy2_alpine test_cpy3_alpine test_cpy2_minimal_aio test_cpy3_minimal_aio test_cpy2_minimal_tx test_cpy3_minimal_tx

test_cpy2:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:cpy2

test_cpy3:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:cpy3

test_pypy2:
	@echo "PyPy isn't available for aarch64 yet"
	#sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:pypy2

test_pypy3:
	@echo "PyPy isn't available for aarch64 yet"
	#sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:pypy3

test_cpy2_alpine:
	# FIXME
	#sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:cpy2-alpine

test_cpy3_alpine:
	# FIXME
	#sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:cpy3-alpine

test_cpy2_minimal_aio:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:cpy2-minimal-aio

test_cpy3_minimal_aio:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:cpy3-minimal-aio

test_cpy2_minimal_tx:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:cpy2-minimal-tx

test_cpy3_minimal_tx:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-aarch64:cpy3-minimal-tx

publish: build
	sudo docker push crossbario/autobahn-python-aarch64:latest
	sudo docker push crossbario/autobahn-python-aarch64:cpy2
	sudo docker push crossbario/autobahn-python-aarch64:cpy2-${AUTOBAHN_PYTHON_VERSION}
	sudo docker push crossbario/autobahn-python-aarch64:cpy3
	sudo docker push crossbario/autobahn-python-aarch64:cpy3-${AUTOBAHN_PYTHON_VERSION}
#	sudo docker push crossbario/autobahn-python-aarch64:pypy2
#	sudo docker push crossbario/autobahn-python-aarch64:pypy2-${AUTOBAHN_PYTHON_VERSION}
#	sudo docker push crossbario/autobahn-python-aarch64:pypy3
#	sudo docker push crossbario/autobahn-python-aarch64:pypy3-${AUTOBAHN_PYTHON_VERSION}
#	sudo docker push crossbario/autobahn-python-aarch64:cpy2-alpine
#	sudo docker push crossbario/autobahn-python-aarch64:cpy2-alpine-${AUTOBAHN_PYTHON_VERSION}
#	sudo docker push crossbario/autobahn-python-aarch64:cpy3-alpine
#	sudo docker push crossbario/autobahn-python-aarch64:cpy3-alpine-${AUTOBAHN_PYTHON_VERSION}
	sudo docker push crossbario/autobahn-python-aarch64:cpy2-minimal-aio
	sudo docker push crossbario/autobahn-python-aarch64:cpy2-minimal-aio-${AUTOBAHN_PYTHON_VERSION}
	sudo docker push crossbario/autobahn-python-aarch64:cpy3-minimal-aio
	sudo docker push crossbario/autobahn-python-aarch64:cpy3-minimal-aio-${AUTOBAHN_PYTHON_VERSION}
	sudo docker push crossbario/autobahn-python-aarch64:cpy2-minimal-tx
	sudo docker push crossbario/autobahn-python-aarch64:cpy2-minimal-tx-${AUTOBAHN_PYTHON_VERSION}
	sudo docker push crossbario/autobahn-python-aarch64:cpy3-minimal-tx
	sudo docker push crossbario/autobahn-python-aarch64:cpy3-minimal-tx-${AUTOBAHN_PYTHON_VERSION}

clean:
	./removeall.sh

list:
	sudo docker images

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
