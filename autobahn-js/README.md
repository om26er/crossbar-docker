# AutobahnJS for Docker

Here you find the Dockerfiles for creating the [AutobahnJS for Docker images](https://hub.docker.com/r/crossbario/autobahn-js/) maintained by the Crossbar.io Project.

These images come with NodeJS and AutobahnJS preinstalled and are intended to base application service containers on. The images

* derive of `node` and `alpine` images
* install AutobahnJS via npm
* copy over the `app` folder to `/app` in the container
* run `npm init && node client.js` in `/app` by default

## Images

1. `autobahnjs`: Default variant, deriving of standard Node image.
2. `autobahnjs:alpine`: Alpine Linux based variant.

## Build, test and deploy

**Note: this only relevant for Crossbar.io Project members which deploy images to our Dockerhub presence.**

To build, test and deploy the AutobahnJS images to DockerHub, do:

```console
make build
make test
make test_alpine
make publish
```
