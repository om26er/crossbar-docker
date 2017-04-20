# Crossbar.io for Docker

Crossbar.io for Docker is available from the official Dockerhub repository [here](https://hub.docker.com/r/crossbario/crossbar/).

The Docker images are built from a Debian Jessie base image and then simply install Crossbar.io from our own binary package repositories for Debian/Ubuntu.

> Because of the above approach, Docker images for Crossbar.io are always current, and hence only need republishing when the image build process steps change.

## Images

Crossbar.io Edition | Architecture | Base OS | Python | Base Image | Dockerfile | Image Tag
---|---|---|---|---|---|---
C | amd64 | Alpine | CPy3 | `python:3-alpine` | [Dockerfile.amd64-community-cpy3](Dockerfile.amd64-community-cpy3) | `crossbario/crossbar:community-cpy3-17.3.1`
C | armhf | Debian/Jessie | CPy3 | `armhf/python:3.6` | [Dockerfile.armhf-community-cpy3](Dockerfile.armhf-community-cpy3) | `crossbario/crossbar-armhf:community-cpy3-17.3.1`
C | aarch64 | Debian/Jessie | CPy3 | `aarch64/python:3.6` | [Dockerfile.aarch64-community-cpy3](Dockerfile.aarch64-community-cpy3) | `crossbario/crossbar-aarch64:community-cpy3-17.3.1`


## Limitations

We currently don't have images for PyPy3 on `armhf` or `aarch64`:

* PyPy does not yet support `aarch64`, see [here](https://bitbucket.org/pypy/pypy/issues/2331/armv8-aarch64-or-aarch32-support).

* PyPy does not yet have automated builders for PyPy3 on `aarch64`, see [here](https://bitbucket.org/pypy/pypy/issues/2540/missing-pypy3-armhf-builder)



