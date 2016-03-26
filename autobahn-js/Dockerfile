FROM node

MAINTAINER The Crossbar.io Project <support@crossbario.com>

ENV DEBIAN_FRONTEND noninteractive

ENV HOME /root
ENV NODE_PATH /usr/local/lib/node_modules/

RUN npm install -g autobahn

ADD client.js /root/client.js
