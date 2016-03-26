build:
	time sudo docker build --no-cache -t crossbario/autobahn-js .

node_version:
	sudo docker run -it crossbario/autobahn-js node -v

autobahn_version:
	sudo docker run -it crossbario/autobahn-js echo "console.log('autobahn-' + require('autobahn').version + ' is installed');" | node

ping:
	sudo docker run --add-host=crossbar:192.168.1.144 -it crossbario/autobahn-js ping crossbar

test:
	sudo docker run -it crossbario/autobahn-js node /root/client.js ws://192.168.1.144:8080/ws realm1

publish:
	sudo docker push crossbario/autobahn-js

list:
	sudo docker images
