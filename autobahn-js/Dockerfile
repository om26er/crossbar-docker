FROM node

MAINTAINER The Crossbar.io Project <support@crossbario.com>

ENV HOME /root
ENV DEBIAN_FRONTEND noninteractive
ENV NODE_PATH /usr/local/lib/node_modules/

# install AutobahnJS globally from https://www.npmjs.com/package/autobahn
RUN npm install -g autobahn

# add an example client
ADD client.js /root/client.js
