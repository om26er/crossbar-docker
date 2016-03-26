.PHONY: crossbar autobahnjs

HOSTIP=$(shell ip route get 1 | awk '{print $$NF;exit}')

crossbar:
	sudo docker run -it -p 8080:8080 crossbario/crossbar

autobahnjs:
	sudo docker run -it crossbario/autobahn-js node /root/client.js ws://$(HOSTIP):8080/ws realm1
