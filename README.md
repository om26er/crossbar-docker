# Crossbar.io/Autobahn Docker Images

**The DockerHub repositories of the Crossbar.io Project can be found [here](https://hub.docker.com/r/crossbario/)**. The images there are built from the Docker files in this Git repository and maintained by the Crossbar.io Project.

Images:

* Docker images with [Crossbar.io](https://hub.docker.com/r/crossbario/crossbar/tags/)
* Docker images with [Autobahn|Python](https://hub.docker.com/r/crossbario/autobahn-python/tags/)
* Docker images with [Autobahn|JS](https://hub.docker.com/r/crossbario/autobahn-js/tags/)

Installation:

```console
sudo docker pull crossbario/crossbar
sudo docker pull crossbario/autobahn-cpp
sudo docker pull crossbario/autobahn-cpp:clang
sudo docker pull crossbario/autobahn-js
sudo docker pull crossbario/autobahn-js:alpine
sudo docker pull crossbario/autobahn-python:cpy2
sudo docker pull crossbario/autobahn-python:cpy3
sudo docker pull crossbario/autobahn-python:pypy2
sudo docker pull crossbario/autobahn-python:cpy2-alpine
sudo docker pull crossbario/autobahn-python:cpy3-alpine
```

---

## Usage

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

## Image Sizes

**Please note, that mere image download size [isn't that relevant anyway](https://insights.ubuntu.com/2016/02/10/docker-alpine-ubuntu-and-you/), but here are numbers.**

Standard Ubuntu Linux based x84-64 image download sizes:

* **Crossbar.io: 111 MB**

Images based on Alpine Linux download sizes:

* **AutobahnJS (alpine): 11 MB**
* **AutobahnPython (cpy3-alpine): 91 MB**
* **AutobahnPython (cpy2-alpine): 93 MB**

Images based on  the respective language standard image download sizes:

* AutobahnJS: 254 MB
* AutobahnPython (pypy2): 290 MB
* AutobahnPython (cpy3): 282 MB
* AutobahnPython (cpy2): 286 MB

Installed sizes:

```console
oberstet@thinkpad-t430s:~$ sudo docker images
REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
crossbario/autobahn-js       alpine-node-only    fe818df130ec        22 minutes ago      24.55 MB
crossbario/autobahn-js       alpine              1958d8775956        22 minutes ago      27.57 MB
crossbario/autobahn-js       latest              6ca4f28def85        23 minutes ago      646.9 MB
crossbario/autobahn-python   cpy3-alpine         30d6d39532c9        About an hour ago   279.5 MB
crossbario/autobahn-python   cpy2                b328e97b854c        About an hour ago   726.3 MB
crossbario/autobahn-python   cpy2-alpine         faadcaee210a        About an hour ago   274.8 MB
crossbario/crossbar          latest              2e558aee8405        2 hours ago         366.9 MB
crossbario/autobahn-python   pypy2               cd49fb36ab64        22 hours ago        766.4 MB
crossbario/autobahn-python   cpy3                d8a61e17d280        22 hours ago        730.4 MB
python                       3                   70c16d34e4c8        3 days ago          689.6 MB
python                       2                   e4a554df875e        3 days ago          676.8 MB
pypy                         2                   d45ac503524a        3 days ago          725 MB
node                         latest              86cbce15c689        3 days ago          644.3 MB
python                       3-alpine            769e9328f383        8 days ago          89.74 MB
python                       2-alpine            dd22f748f304        8 days ago          72.59 MB
ubuntu                       latest              97434d46f197        9 days ago          188 MB
ubuntu                       trusty              97434d46f197        9 days ago          188 MB
alpine                       latest              70c557e50ed6        3 weeks ago         4.798 MB
```
