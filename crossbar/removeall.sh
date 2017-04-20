#!/bin/bash

# Delete all containers
sudo docker rm --force $(sudo docker ps -a -q)

# Delete all images
sudo docker rmi --force $(sudo docker images -q)
