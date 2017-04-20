# Crossbar.io for Docker

Crossbar.io for Docker is available from the official Dockerhub repository [here](https://hub.docker.com/r/crossbario/crossbar/).

The Docker images are built from a Debian Jessie base image and then simply install Crossbar.io from our own binary package repositories for Debian/Ubuntu.

> Because of the above approach, Docker images for Crossbar.io are always current, and hence only need republishing when the image build process steps change.


Crossbar.io Edition | Architecture | Base OS | Python | Base Image | Dockerfile | Image Tag
---|---|---|---|---|---|---
Community | amd64 | Alpine | CPython 3 | `python:3-alpine` | [Dockerfile.amd64-community-cpy3](Dockerfile.amd64-community-cpy3) | `crossbario/crossbar:community-cpy3-17.3.1`
Community | armhf | Debian/Jessie | CPython 3 | `armhf/python:3.6` | [Dockerfile.armhf-community-cpy3](Dockerfile.armhf-community-cpy3) | `crossbario/crossbar-armhf:community-cpy3-17.3.1`
Community | aarch64 | Debian/Jessie | CPython 3 | `aarch64/python:3.6` | [Dockerfile.aarch64-community-cpy3](Dockerfile.aarch64-community-cpy3) | `crossbario/crossbar-aarch64:community-cpy3-17.3.1`
