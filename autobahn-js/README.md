This contains the build stuff for AutobahnJS-Node / Docker.

## Build and Deploy

To build and deploy the AutobahnJS image to DockerHub, do:

```console
make build
make test
make publish
```

## End-user Experience

The end user experience of a user with only Docker installed is one command to download the AutobahnJS image and start a new container with a AutobahnJS client connecting to a Crossbar.io router:

```console
sudo docker run -it crossbario/autobahn-js node /root/client.js ws://192.168.1.144:8080/ws realm1
```

> Note: replace the URL `ws://192.168.1.144:8080/ws` with the WAMP listening transport URL of your Crossbar.io node, and replace `realm1` with the realm to connect to.

This will log something like:

```console
oberstet@thinkpad-t430s:~$ sudo docker pull crossbario/autobahn-js
[sudo] password for oberstet:
Using default tag: latest
latest: Pulling from crossbario/autobahn-js

fdd5d7827f33: Pull complete
a3ed95caeb02: Pull complete
0f35d0fe50cc: Pull complete
7b40647e93b7: Pull complete
ce5207842c4c: Pull complete
5a3b05f77d24: Pull complete
2109bd3acb97: Pull complete
3e0f42890cc0: Pull complete
027acc4ac430: Pull complete
Digest: sha256:5332528d5b1cf886db4e00ea8d2dcc190c69379ce7206ca092293f81e283a0c0
Status: Downloaded newer image for crossbario/autobahn-js:latest
oberstet@thinkpad-t430s:~$ sudo docker run -it crossbario/autobahn-js ws://192.168.1.142:8080/ws realm1
exec: "ws://192.168.1.142:8080/ws": stat ws://192.168.1.142:8080/ws: no such file or directory
docker: Error response from daemon: Container command not found or does not exist..
oberstet@thinkpad-t430s:~$ sudo docker run -it crossbario/autobahn-js node /root/client.js ws://192.168.1.142:8080/ws realm1
session open! { x_cb_node_id: '60ef04fa6b73',
  realm: 'realm1',
  authid: '5TQF-7U6A-GPF9-M474-C9XH-EMJ9',
  authrole: 'anonymous',
  authmethod: 'anonymous',
  authprovider: 'static',
  roles:
   { broker: { features: [Object] },
     dealer: { features: [Object] } } }
session closed: closed { reason: 'wamp.close.normal',
  message: '',
  retry_delay: null,
  retry_count: null,
  will_retry: false }
oberstet@thinkpad-t430s:~$
```
