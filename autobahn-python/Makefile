.PHONY: build

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

build:
	time sudo docker build -t crossbario/autobahn-python:cpy2 -f Dockerfile.cpy2 .
	time sudo docker build -t crossbario/autobahn-python:cpy3 -f Dockerfile.cpy3 .
	time sudo docker build -t crossbario/autobahn-python:pypy2 -f Dockerfile.pypy2 .
	time sudo docker build -t crossbario/autobahn-python:cpy2-alpine -f Dockerfile.cpy2-alpine .
	time sudo docker build -t crossbario/autobahn-python:cpy3-alpine -f Dockerfile.cpy3-alpine .

version:
	sudo docker run -it crossbario/autobahn-python:cpy2 python -V
	sudo docker run -it crossbario/autobahn-python:cpy3 python -V
	sudo docker run -it crossbario/autobahn-python:pypy2 pypy -V
	sudo docker run -it crossbario/autobahn-python:cpy2-alpine python -V
	sudo docker run -it crossbario/autobahn-python:cpy3-alpine python -V

autobahn_version:
	sudo docker run -it crossbario/autobahn-python:cpy2 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:cpy3 python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:pypy2 pypy -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:cpy2-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"
	sudo docker run -it crossbario/autobahn-python:cpy3-alpine python -c "import autobahn; print('running autobahn-{}'.format(autobahn.__version__))"

test_cpy2:
	sudo docker run -it crossbario/autobahn-python:cpy2 python /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_cpy3:
	sudo docker run -it crossbario/autobahn-python:cpy3 python /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_pypy2:
	sudo docker run -it crossbario/autobahn-python:pypy2 pypy /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_cpy2_alpine:
	sudo docker run -it crossbario/autobahn-python:cpy2-alpine python /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

test_cpy3_alpine:
	sudo docker run -it crossbario/autobahn-python:cpy3-alpine python /root/client.py --url ws://$(HOSTIP):8080/ws --realm realm1

publish:
	sudo docker push crossbario/autobahn-python:cpy2
	sudo docker push crossbario/autobahn-python:cpy3
	sudo docker push crossbario/autobahn-python:pypy2
	sudo docker push crossbario/autobahn-python:cpy2-alpine
	sudo docker push crossbario/autobahn-python:cpy3-alpine

list:
	sudo docker images
