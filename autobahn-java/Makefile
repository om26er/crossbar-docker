build:
	docker build \
		-t autobahn-java \
		-t autobahn-java:latest \
		-f Dockerfile.Android .

run:
	docker run \
		--volume ${PWD}/../../autobahn-java:/workspace/ autobahn-java
	echo "Generated: ../../autobahn-java/demo-gallery/build/outputs/apk/demo-gallery-release-unsigned.apk"
