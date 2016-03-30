Put your microservice code and assets in here.

The container will automatically start the script:

    node client.js

The environment will have these variables set:

    CBURL = ws://crossbar:8080/ws
    CBREALM = realm1

where the host `crossbar` resolves to a linked Docker container running Crossbar.io.
