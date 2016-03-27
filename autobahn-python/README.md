This contains the build stuff for AutobahnPython / Docker.

## Build and Deploy

To build and deploy the AutobahnPython images to DockerHub, do:

```console
make build
make test_cpy2
make test_cpy3
make test_pypy2
make test_cpy2_alpine
make test_cpy3_alpine
make publish
```

## End-user Experience

The end user experience of a user with only Docker installed is one command to download the AutobahnJS image and start a new container with a AutobahnJS client connecting to a Crossbar.io router:

```console
sudo docker run -it crossbario/autobahn-python:cpy2 python /root/client.py --url ws://192.168.1.144:8080/ws --realm realm1
```

> Note: replace the URL `ws://192.168.1.144:8080/ws` with the WAMP listening transport URL of your Crossbar.io node, and replace `realm1` with the realm to connect to.

This will log something like:

```console
oberstet@thinkpad-t430s:~$ make test_cpy2
sudo docker run -it crossbario/autobahn-python:cpy2 python /root/client.py --url ws://192.168.55.135:8080/ws --realm realm1
2016-03-26T21:20:00+0000 Client connected
2016-03-26T21:20:00+0000 Client session joined SessionDetails(realm=<realm1>, session=7649507387404776, authid=<CPYQ-WTNV-EUG5-5QTX-3QNY-K74Q>, authrole=<anonymous>, authmethod=anonymous, authprovider=static, authextra=None)
2016-03-26T21:20:00+0000 Router session closed (CloseDetails(reason=<wamp.close.normal>, message='None'))
2016-03-26T21:20:00+0000 Router connection closed
2016-03-26T21:20:00+0000 Main loop terminated.
```
