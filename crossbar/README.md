# Crossbar.io for Docker

Crossbar.io for Docker is available from the official Dockerhub repository [here](https://hub.docker.com/r/crossbario/crossbar/).

The Docker images are built from a Debian Jessie base image and then simply install Crossbar.io from our own binary package repositories for Debian/Ubuntu.

> Because of the above approach, Docker images for Crossbar.io are always current, and hence only need republishing when the image build process steps change.

## Images

Supported:

Crossbar.io Edition | Architecture | Base OS | Python | Base Image | Dockerfile | Image Tag
---|---|---|---|---|---|---
C | amd64 | Alpine | CPy3 | `python:3-alpine` | [Dockerfile.amd64-community-cpy3](Dockerfile.amd64-community-cpy3) | `crossbario/crossbar:community-cpy3`
C | armhf | Debian/Jessie | CPy3 | `armhf/python:3.6` | [Dockerfile.armhf-community-cpy3](Dockerfile.armhf-community-cpy3) | `crossbario/crossbar-armhf:community-cpy3`
C | aarch64 | Debian/Jessie | CPy3 | `aarch64/python:3.6` | [Dockerfile.aarch64-community-cpy3](Dockerfile.aarch64-community-cpy3) | `crossbario/crossbar-aarch64:community-cpy3`
C | amd64 | Debian/jessie | PyPy3 | `debian:jessie` | [Dockerfile.amd64-community-pypy3](Dockerfile.amd64-community-pypy3) | `crossbario/crossbar:community-pypy3`

Upcoming:

We currently don't have images for PyPy3 on `armhf` or `aarch64`:

* PyPy does not yet support `aarch64`, see [here](https://bitbucket.org/pypy/pypy/issues/2331/armv8-aarch64-or-aarch32-support).
* PyPy does not yet have automated builders for PyPy3 on `aarch64`, see [here](https://bitbucket.org/pypy/pypy/issues/2540/missing-pypy3-armhf-builder)

Crossbar.io Edition | Architecture | Base OS | Python | Base Image | Dockerfile | Image Tag
---|---|---|---|---|---|---
C | armhf | Debian/Jessie | PyPy3 | `armhf/debian` | [Dockerfile.armhf-community-cpy3](Dockerfile.armhf-community-cpy3) | `crossbario/crossbar-armhf:community-cpy3`
C | aarch64 | Debian/Jessie | PyPy3 | `aarch64/debian` | [Dockerfile.aarch64-community-cpy3](Dockerfile.aarch64-community-cpy3) | `crossbario/crossbar-aarch64:community-cpy3


---

## Qemu crossbuilding

References:

* http://blog.ubergarm.com/run-arm-docker-images-on-x86_64-hosts/

armhf images:

* https://hub.docker.com/r/armhf/debian/tags/
* https://hub.docker.com/r/armhf/python/tags/

aarch64 images:

* https://hub.docker.com/r/aarch64/debian/tags/
* https://hub.docker.com/r/aarch64/python/tags/

Install the stuff

```console
sudo apt-get update && apt-get install -y --no-install-recommends \
        qemu-user-static \
        binfmt-support
sudo update-binfmts --enable qemu-arm
sudo update-binfmts --display qemu-arm
```

Test the baby:

```console
qemu-arm-static -version
curl -O http://ubergarm.com/dre/hello-world-arm
chmod a+x hello-world-arm
file hello-world-arm
qemu-arm-static hello-world-arm
./hello-world-arm
```

### Testing

#### Debian/armhf

```console
sudo docker pull armhf/debian:jessie
sudo docker run --rm -it -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static armhf/debian:jessie uname -a
```

should give you

```console
Linux 1300319df2a8 4.4.0-72-generic #93-Ubuntu SMP Fri Mar 31 14:07:41 UTC 2017 armv7l GNU/Linux
```

#### CPython3/armhf

```console
sudo docker pull armhf/python:3.6
sudo docker run --rm -it -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static armhf/python:3.6 python -V
```

should give you

```console
Python 3.6.1
```

#### Debian/aarch64


```console
sudo docker pull aarch64/debian:jessie
sudo docker run --rm -it -v /usr/bin/qemu-aarch64-static:/usr/bin/qemu-aarch64-static aarch64/debian:jessie uname -a
```

should give you

```console
Linux 10834da604c6 4.4.0-72-generic #93-Ubuntu SMP Fri Mar 31 14:07:41 UTC 2017 aarch64 GNU/Linux
```

#### CPython3/aarch64

```console
sudo docker pull aarch64/python:3.6
sudo docker run --rm -it -v /usr/bin/qemu-aarch64-static:/usr/bin/qemu-aarch64-static aarch64/python:3.6 python -V
```

should give you

```console
Python 3.6.1
```

-----

https://github.com/jedisct1/libsodium/blob/master/test/default/sodium_utils3.c


qemu: Unsupported syscall: 384
https://gist.github.com/oberstet/4b0f34b6765aa12ceee723def1f91e20#file-gistfile1-txt-L77


https://docs.resin.io/troubleshooting/troubleshooting/#unsupported-syscall-384-from-qemu-on-builder


FAIL: sodium_utils3
https://gist.github.com/oberstet/4b0f34b6765aa12ceee723def1f91e20#file-gistfile1-txt-L823



    See test/default/test-suite.log
    Please report to https://github.com/jedisct1/libsodium/issues



sudo docker run --rm -it -v /usr/bin/qemu-arm-static:/usr/bin/qemu-arm-static armhf/python:3.6-alpine
