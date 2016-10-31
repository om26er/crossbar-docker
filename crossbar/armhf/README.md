This contains the build stuff for Crossbar.io / Docker on armhf.

## Build and Deploy

To build and deploy the Crossbar.io Docker image to DockerHub, do:

```console
make build
make test
make publish
```

## End-user Experience

The end user experience of a user with only Docker installed is one command to download the Crossbar.io Docker image and start a new container with Crossbar.io and a default node configuration:

    sudo docker run -it -p 8080:8080 crossbario/crossbar-armhf

This will log something like:

```console
```
