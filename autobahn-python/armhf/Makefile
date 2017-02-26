.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	sudo docker build \
		-t crossbario/autobahn-python-armhf:cpy2 \
		-t crossbario/autobahn-python-armhf:cpy2-0.17.2 \
		-f Dockerfile.cpy2 .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:cpy3 \
		-t crossbario/autobahn-python-armhf:cpy3-0.17.2 \
		-f Dockerfile.cpy3 .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:pypy2 \
		-t crossbario/autobahn-python-armhf:pypy2-0.17.2 \
		-f Dockerfile.pypy2 .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:pypy3 \
		-t crossbario/autobahn-python-armhf:pypy3-0.17.2 \
		-f Dockerfile.pypy3 .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:cpy2-alpine \
		-t crossbario/autobahn-python-armhf:cpy2-alpine-0.17.2 \
		-f Dockerfile.cpy2-alpine .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:latest \
		-t crossbario/autobahn-python-armhf:cpy3-alpine \
		-t crossbario/autobahn-python-armhf:cpy3-alpine-0.17.2 \
		-f Dockerfile.cpy3-alpine .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:cpy2-minimal-aio \
		-t crossbario/autobahn-python-armhf:cpy2-minimal-aio-0.17.2 \
		-f Dockerfile.cpy2-minimal-aio .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:cpy3-minimal-aio \
		-t crossbario/autobahn-python-armhf:cpy3-minimal-aio-0.17.2 \
		-f Dockerfile.cpy3-minimal-aio .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:cpy2-minimal-tx \
		-t crossbario/autobahn-python-armhf:cpy2-minimal-tx-0.17.2 \
		-f Dockerfile.cpy2-minimal-tx .

	sudo docker build \
		-t crossbario/autobahn-python-armhf:cpy3-minimal-tx \
		-t crossbario/autobahn-python-armhf:cpy3-minimal-tx-0.17.2 \
		-f Dockerfile.cpy3-minimal-tx .

version: python_version autobahn_version

python_version:
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy2 python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy3 python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:pypy2 python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:pypy3 python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy2-alpine python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy3-alpine python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy2-minimal-aio python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy3-minimal-aio python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy2-minimal-tx python -V
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy3-minimal-tx python -V

autobahn_version:
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy2 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy3 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:pypy2 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:pypy3 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy2-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy3-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy2-minimal-aio python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy3-minimal-aio python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy2-minimal-tx python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python-armhf:cpy3-minimal-tx python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"

test: test_cpy2 test_cpy3 test_pypy2 test_pypy3 test_cpy2_alpine test_cpy3_alpine test_cpy2_minimal_aio test_cpy3_minimal_aio test_cpy2_minimal_tx test_cpy3_minimal_tx

test_cpy2:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:cpy2

test_cpy3:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:cpy3

test_pypy2:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:pypy2

test_pypy3:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:pypy3

test_cpy2_alpine:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:cpy2-alpine

test_cpy3_alpine:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:cpy3-alpine

test_cpy2_minimal_aio:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:cpy2-minimal-aio

test_cpy3_minimal_aio:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:cpy3-minimal-aio

test_cpy2_minimal_tx:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:cpy2-minimal-tx

test_cpy3_minimal_tx:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python-armhf:cpy3-minimal-tx

publish: build
	sudo docker push crossbario/autobahn-python-armhf:latest
	sudo docker push crossbario/autobahn-python-armhf:cpy2
	sudo docker push crossbario/autobahn-python-armhf:cpy2-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:cpy3
	sudo docker push crossbario/autobahn-python-armhf:cpy3-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:pypy2
	sudo docker push crossbario/autobahn-python-armhf:pypy2-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:pypy3
	sudo docker push crossbario/autobahn-python-armhf:pypy3-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:cpy2-alpine
	sudo docker push crossbario/autobahn-python-armhf:cpy2-alpine-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:cpy3-alpine
	sudo docker push crossbario/autobahn-python-armhf:cpy3-alpine-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:cpy2-minimal-aio
	sudo docker push crossbario/autobahn-python-armhf:cpy2-minimal-aio-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:cpy3-minimal-aio
	sudo docker push crossbario/autobahn-python-armhf:cpy3-minimal-aio-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:cpy2-minimal-tx
	sudo docker push crossbario/autobahn-python-armhf:cpy2-minimal-tx-0.17.2
	sudo docker push crossbario/autobahn-python-armhf:cpy3-minimal-tx
	sudo docker push crossbario/autobahn-python-armhf:cpy3-minimal-tx-0.17.2

list:
	sudo docker images
