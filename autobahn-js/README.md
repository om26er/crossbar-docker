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

    sudo docker run -it crossbario/autobahn-js

This will log something like:

```console
...
```
