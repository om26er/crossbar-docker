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
...
```
