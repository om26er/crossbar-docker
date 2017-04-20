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
