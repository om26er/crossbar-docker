# Crossbar.io and Autobahn for Docker

## tldr;

Images:

* [Crossbar.io](https://hub.docker.com/r/crossbario/crossbar/tags/)
* [Autobahn|Python](https://hub.docker.com/r/crossbario/autobahn-python/tags/))
* [Autobahn|JS](https://hub.docker.com/r/crossbario/autobahn-js/tags/)

Installation:

```console
sudo docker pull crossbario/autobahn-js
sudo docker pull crossbario/autobahn-js:alpine
sudo docker pull crossbario/autobahn-python:cpy2
sudo docker pull crossbario/autobahn-python:cpy3
sudo docker pull crossbario/autobahn-python:pypy2
sudo docker pull crossbario/autobahn-python:cpy2-alpine
sudo docker pull crossbario/autobahn-python:cpy3-alpine
```

## Introduction

The official Docker repository of the Crossbar.io Project can be found on DockerHub [here](https://hub.docker.com/r/crossbario/crossbar/).

The images there are built from the Docker files in this Git repository.

## Running

Obviously, [install Docker](https://docs.docker.com/linux/).

To test the end user experience, open a first terminal and type

```console
sudo docker run -it -p 8080:8080 crossbario/crossbar
```

> This will run a single Docker command to download and start a Crossbar.io container. You can also type `make crossbar` if you are lazy (there is a Makefile with the former command).

In a second terminal, type

```console
sudo docker run -it crossbario/autobahn-js node /root/client.js ws://192.168.1.100:8080/ws realm1
```

Here, you will need to replace the IP address `192.168.1.100` with that of your box (and it needs to be one visible from within the container - NOT `127.0.0.1`).

> This will run a single Docker command to download and start a AutobahnJS container with an example client connecting to the former Crossbar.io running container. You can also type `make autobahnjs` if you are lazy (there is a Makefile with the former command).

In a third terminal, type

```console
sudo docker run -it crossbario/autobahn-python:cpy2 python /root/client.py --url ws://192.168.1.100:8080/ws --realm realm1
```

Again, replace the IP address according to your network setup.
