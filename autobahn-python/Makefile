.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	time sudo docker build -t crossbario/autobahn-python:cpy2 -f Dockerfile.cpy2 .
	time sudo docker build -t crossbario/autobahn-python:cpy3 -f Dockerfile.cpy3 .
	time sudo docker build -t crossbario/autobahn-python:pypy2 -f Dockerfile.pypy2 .
	time sudo docker build -t crossbario/autobahn-python:cpy2-alpine -f Dockerfile.cpy2-alpine .
	time sudo docker build -t crossbario/autobahn-python:cpy3-alpine -f Dockerfile.cpy3-alpine .
	time sudo docker build -t crossbario/autobahn-python:cpy3-minimal -t crossbario/autobahn-python:latest -f Dockerfile.cpy3-minimal .

version:
	sudo docker run -it crossbario/autobahn-python:cpy2 python -V
	sudo docker run -it crossbario/autobahn-python:cpy3 python -V
	sudo docker run -it crossbario/autobahn-python:pypy2 pypy -V
	sudo docker run -it crossbario/autobahn-python:cpy2-alpine python -V
	sudo docker run -it crossbario/autobahn-python:cpy3-alpine python -V
	sudo docker run -it crossbario/autobahn-python:cpy3-minimal python -V

autobahn_version:
	sudo docker run -it crossbario/autobahn-python:cpy2 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:cpy3 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:pypy2 pypy -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:cpy2-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:cpy3-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:cpy3-minimal python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"

test_cpy2:
	sudo docker run -it crossbario/autobahn-python:cpy2 python /app/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_cpy3:
	sudo docker run -it crossbario/autobahn-python:cpy3 python /app/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_pypy2:
	sudo docker run -it crossbario/autobahn-python:pypy2 pypy /app/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_cpy2_alpine:
	sudo docker run -it crossbario/autobahn-python:cpy2-alpine python /app/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_cpy3_alpine:
	sudo docker run -it crossbario/autobahn-python:cpy3-alpine python /app/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_cpy3_minimal:
	sudo docker run -it crossbario/autobahn-python:cpy3-minimal python /app/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

publish:
	sudo docker push crossbario/autobahn-python:cpy2
	sudo docker push crossbario/autobahn-python:cpy3
	sudo docker push crossbario/autobahn-python:pypy2
	sudo docker push crossbario/autobahn-python:cpy2-alpine
	sudo docker push crossbario/autobahn-python:cpy3-alpine
	sudo docker push crossbario/autobahn-python:cpy3-minimal

list:
	sudo docker images
