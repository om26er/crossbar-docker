build_aarch64_community_cpy3:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build \
		-t crossbario/crossbar-aarch64:latest \
		-t crossbario/crossbar-aarch64:community-cpy3 \
		-t crossbario/crossbar-aarch64:community-cpy3-17.3.1 \
		-f Dockerfile.community-cpy3 .

build:
	# enforce auto-generating a new key when using the images
	sudo rm -f node/.crossbar/node.key
	time sudo docker build \
		--build-arg BASEIMAGE='aarch64/python:3.5' \
		-f Dockerfile.community .

qemu_deps:
	sudo apt-get update
	sudo apt-get install -y --no-install-recommends qemu-user-static binfmt-support
	sudo update-binfmts --enable qemu-arm
	sudo update-binfmts --enable qemu-aarch64
	sudo update-binfmts --display qemu-arm
	sudo update-binfmts --display qemu-aarch64
	mkdir -p ./.qemu
	cp /usr/bin/qemu-aarch64-static ./.qemu
	cp /usr/bin/qemu-arm-static ./.qemu
