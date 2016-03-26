build:
	time sudo docker build --no-cache -t crossbario/crossbar .

test:
	sudo docker run -it -p 8080:8080 crossbario/crossbar

publish:
	sudo docker push crossbario/crossbar

start:
	sudo docker run --entrypoint=/opt/crossbar/bin/crossbar -it -p 8080:8080 crossbario/crossbar start --cbdir /var/crossbar/.crossbar

version:
	sudo docker run --entrypoint=/opt/crossbar/bin/crossbar -it crossbario/crossbar version

list:
	sudo docker images
