HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

SUBDIRS = crossbar autobahn-js/x86_64 autobahn-js/armhf autobahn-js/aarch64 autobahn-python/x86-64 autobahn-python/armhf autobahn-python/aarch64


subdirs: $(SUBDIRS)

BUILDDIRS = $(SUBDIRS:%=build-%)
VERSIONDIRS = $(SUBDIRS:%=version-%)
TESTDIRS = $(SUBDIRS:%=test-%)
PUBLISHDIRS = $(SUBDIRS:%=publish-%)

build: $(BUILDDIRS)
version: $(VERSIONDIRS)
test: $(TESTDIRS)
publish: $(PUBLISHDIRS)

$(BUILDDIRS):
	$(MAKE) -C $(@:build-%=%) build

$(VERSIONDIRS):
	$(MAKE) -C $(@:version-%=%) version

$(TESTDIRS):
	$(MAKE) -C $(@:test-%=%) test

$(PUBLISHDIRS):
	$(MAKE) -C $(@:publish-%=%) publish

.PHONY: subdirs $(BUILDDIRS) $(VERSIONDIRS) $(TESTDIRS) $(PUBLISHDIRS)
.PHONY: build version test publish


requirements: docker docker_compose

# install docker
docker:
	sudo apt-get install -y apt-transport-https ca-certificates
	sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
	sudo sh -c "echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' > /etc/apt/sources.list.d/docker.list"
	sudo apt-get update
	sudo apt-get purge lxc-docker
	sudo apt-cache policy docker-engine
	sudo apt-get install -y linux-image-extra-$$(uname -r)
	sudo apt-get install -y docker-engine

# install docker compose (see: https://github.com/docker/compose/releases)
docker_compose:
	sudo sh -c "curl -L https://github.com/docker/compose/releases/download/1.7.0-rc1/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"
	sudo chmod +x /usr/local/bin/docker-compose
