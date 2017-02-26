.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	time sudo docker build \
		-t crossbario/autobahn-python:cpy2 \
		-t crossbario/autobahn-python:cpy2-0.17.2 \
		-f Dockerfile.cpy2 .

	time sudo docker build \
		-t crossbario/autobahn-python:cpy3 \
		-t crossbario/autobahn-python:cpy3-0.17.2 \
		-f Dockerfile.cpy3 .

	time sudo docker build \
		-t crossbario/autobahn-python:pypy2 \
		-t crossbario/autobahn-python:pypy2-0.17.2 \
		-f Dockerfile.pypy2 .

	time sudo docker build \
		-t crossbario/autobahn-python:pypy3 \
		-t crossbario/autobahn-python:pypy3-0.17.2 \
		-f Dockerfile.pypy3 .

	time sudo docker build \
		-t crossbario/autobahn-python:cpy2-alpine \
		-t crossbario/autobahn-python:cpy2-alpine-0.17.2 \
		-f Dockerfile.cpy2-alpine .

	time sudo docker build \
		-t crossbario/autobahn-python:latest \
		-t crossbario/autobahn-python:cpy3-alpine \
		-t crossbario/autobahn-python:cpy3-alpine-0.17.2 \
		-f Dockerfile.cpy3-alpine .

	time sudo docker build \
		-t crossbario/autobahn-python:cpy2-minimal-aio \
		-t crossbario/autobahn-python:cpy2-minimal-aio-0.17.2 \
		-f Dockerfile.cpy2-minimal-aio .

	time sudo docker build \
		-t crossbario/autobahn-python:cpy3-minimal-aio \
		-t crossbario/autobahn-python:cpy3-minimal-aio-0.17.2 \
		-f Dockerfile.cpy3-minimal-aio .

	time sudo docker build \
		-t crossbario/autobahn-python:cpy2-minimal-tx \
		-t crossbario/autobahn-python:cpy2-minimal-tx-0.17.2 \
		-f Dockerfile.cpy2-minimal-tx .

	time sudo docker build \
		-t crossbario/autobahn-python:cpy3-minimal-tx \
		-t crossbario/autobahn-python:cpy3-minimal-tx-0.17.2 \
		-f Dockerfile.cpy3-minimal-tx .

version: python_version autobahn_version

python_version:
	sudo docker run -it --rm crossbario/autobahn-python:cpy2 python -V
	sudo docker run -it --rm crossbario/autobahn-python:cpy3 python -V
	sudo docker run -it --rm crossbario/autobahn-python:pypy2 python -V
	sudo docker run -it --rm crossbario/autobahn-python:pypy3 python -V
	sudo docker run -it --rm crossbario/autobahn-python:cpy2-alpine python -V
	sudo docker run -it --rm crossbario/autobahn-python:cpy3-alpine python -V
	sudo docker run -it --rm crossbario/autobahn-python:cpy2-minimal-aio python -V
	sudo docker run -it --rm crossbario/autobahn-python:cpy3-minimal-aio python -V
	sudo docker run -it --rm crossbario/autobahn-python:cpy2-minimal-tx python -V
	sudo docker run -it --rm crossbario/autobahn-python:cpy3-minimal-tx python -V

autobahn_version:
	sudo docker run -it --rm crossbario/autobahn-python:cpy2 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:cpy3 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:pypy2 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:pypy3 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:cpy2-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:cpy3-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:cpy2-minimal-aio python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:cpy3-minimal-aio python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:cpy2-minimal-tx python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it --rm crossbario/autobahn-python:cpy3-minimal-tx python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"

test: test_cpy2 test_cpy3 test_pypy2 test_pypy3 test_cpy2_alpine test_cpy3_alpine test_cpy2_minimal_aio test_cpy3_minimal_aio test_cpy2_minimal_tx test_cpy3_minimal_tx

test_cpy2:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy2

test_cpy3:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy3

test_pypy2:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:pypy2

test_pypy3:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:pypy3

test_cpy2_alpine:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy2-alpine

test_cpy3_alpine:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy3-alpine

test_cpy2_minimal_aio:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy2-minimal-aio

test_cpy3_minimal_aio:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy3-minimal-aio

test_cpy2_minimal_tx:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy2-minimal-tx

test_cpy3_minimal_tx:
	sudo docker run -it --rm --link crossbar crossbario/autobahn-python:cpy3-minimal-tx

publish: build
	sudo docker push crossbario/autobahn-python:latest
	sudo docker push crossbario/autobahn-python:cpy2
	sudo docker push crossbario/autobahn-python:cpy2-0.17.2
	sudo docker push crossbario/autobahn-python:cpy3
	sudo docker push crossbario/autobahn-python:cpy3-0.17.2
	sudo docker push crossbario/autobahn-python:pypy2
	sudo docker push crossbario/autobahn-python:pypy2-0.17.2
	sudo docker push crossbario/autobahn-python:pypy3
	sudo docker push crossbario/autobahn-python:pypy3-0.17.2
	sudo docker push crossbario/autobahn-python:cpy2-alpine
	sudo docker push crossbario/autobahn-python:cpy2-alpine-0.17.2
	sudo docker push crossbario/autobahn-python:cpy3-alpine
	sudo docker push crossbario/autobahn-python:cpy3-alpine-0.17.2
	sudo docker push crossbario/autobahn-python:cpy2-minimal-aio
	sudo docker push crossbario/autobahn-python:cpy2-minimal-aio-0.17.2
	sudo docker push crossbario/autobahn-python:cpy3-minimal-aio
	sudo docker push crossbario/autobahn-python:cpy3-minimal-aio-0.17.2
	sudo docker push crossbario/autobahn-python:cpy2-minimal-tx
	sudo docker push crossbario/autobahn-python:cpy2-minimal-tx-0.17.2
	sudo docker push crossbario/autobahn-python:cpy3-minimal-tx
	sudo docker push crossbario/autobahn-python:cpy3-minimal-tx-0.17.2

list:
	sudo docker images
