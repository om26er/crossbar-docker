FROM ubuntu:trusty

MAINTAINER The Crossbar.io Project <support@crossbario.com>

ENV HOME /var/crossbar
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1
ENV PATH /opt/crossbar/bin:$PATH

# install Crossbar.io from the official Crossbar.io binary package repositories
RUN apt-key adv --keyserver hkps.pool.sks-keyservers.net --recv D58C6920 \
    && echo 'deb http://package.crossbar.io/ubuntu trusty main' > /etc/apt/sources.list.d/crossbar.list \
    && apt-get update \
    && apt-get install -y crossbar \
    && rm -rf /var/lib/apt/lists/*

# initialize a Crossbar.io node
COPY ./node /var/crossbar
RUN chown -R daemon:daemon /var/crossbar

# run under this user, and expose default port
USER daemon
EXPOSE 8080 8000

# entrypoint for the Docker image is the Crossbar.io executable
ENTRYPOINT ["crossbar", "start", "--cbdir", "/var/crossbar/.crossbar"]
