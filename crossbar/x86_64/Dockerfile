FROM ubuntu:trusty

MAINTAINER The Crossbar.io Project <support@crossbario.com>

ENV HOME /var/crossbar
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1

# install Crossbar.io from the official Crossbar.io binary package repositories
RUN apt-key adv --keyserver hkps.pool.sks-keyservers.net --recv D58C6920 \
    && echo 'deb http://package.crossbar.io/ubuntu trusty main' > /etc/apt/sources.list.d/crossbar.list \
    && apt-get update \
    && apt-get install -y crossbar

# create a new Crossbar.io node directory from the default template
RUN /opt/crossbar/bin/crossbar init --template default --appdir /var/crossbar

# entrypoint for the Docker image is the Crossbar.io executable
ENTRYPOINT ["/opt/crossbar/bin/crossbar", "start", "--cbdir", "/var/crossbar/.crossbar"]
