# Crossbar.io and Autobahn for Docker

The official Docker repository of the Crossbar.io Project can be found on DockerHub [here](https://hub.docker.com/r/crossbario/crossbar/).

The images there are built from the Docker files in this Git repository.

## Running

Obviously, [install Docker](https://docs.docker.com/linux/).

To test the end user experience, open a first terminal and type

```console
make crossbar
```

> This will run a single Docker command to download and start a Crossbar.io container.

In a second terminal, type

```console
make autobahnjs
```

> This will run a single Docker command to download and start a AutobahnJS container with an example client connecting to the former Crossbar.io running container.
