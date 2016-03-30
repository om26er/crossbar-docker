FROM node

MAINTAINER The Crossbar.io Project <support@crossbario.com>

ENV HOME /app
ENV DEBIAN_FRONTEND noninteractive

ENV NODE_PATH /usr/local/lib/node_modules/

# Crossbar.io connection defaults
ENV CBURL ws://crossbar:8080/ws
ENV CBREALM realm1

# make sure HOME exists!
RUN mkdir /app

# install AutobahnJS globally
RUN npm install -g autobahn

# add example service
COPY ./app/* /app/

# run service entry script by default
WORKDIR /app
CMD ["node", client.js"]
