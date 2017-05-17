build:
	docker build \
		-t autobahn-java \
		-t autobahn-java:latest \
		-f Dockerfile.Android .

run:
	docker run \
		--volume ${PWD}/../../autobahn-java:/workspace/ autobahn-java
