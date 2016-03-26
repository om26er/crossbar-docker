FROM ubuntu:trusty

MAINTAINER The Crossbar.io Project <support@crossbario.com>

ENV DEBIAN_FRONTEND noninteractive
ENV HOME /var/crossbar

# add the official Crossbar.io project repositories
RUN apt-key adv --keyserver hkps.pool.sks-keyservers.net --recv D58C6920
RUN echo 'deb http://package.crossbar.io/ubuntu trusty main' > /etc/apt/sources.list.d/crossbar.list

# update the system
RUN apt-get update -y
RUN apt-get dist-upgrade -y

# install Crossbar.io
RUN apt-get install crossbar

# patch to make log output from Crossbar.io unbuffered
RUN sed -i '1 s/^.*$/\#\!\/opt\/crossbar\/bin\/pypy -u/g' /opt/crossbar/bin/crossbar

# create a new Crossbar.io node directory from the default template
RUN /opt/crossbar/bin/crossbar init --template default --appdir /var/crossbar

# entrypoint for the Docker image is the Crossbar.io executable
ENTRYPOINT ["/opt/crossbar/bin/crossbar", "start", "--cbdir", "/var/crossbar/.crossbar"]
