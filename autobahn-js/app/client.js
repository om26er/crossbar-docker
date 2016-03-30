// Example WAMP client for AutobahnJS connecting to a Crossbar.io WAMP router.

// AutobahnJS, the WAMP client library to connect and talk to Crossbar.io:
var autobahn = require('autobahn');

// We read the connection parameters from the command line in this example:
const url = process.argv[2];
const realm = process.argv[3];

// Make us a new connection ..
var connection = new autobahn.Connection({url: url, realm: realm});

// .. and fire this code when we got a session
connection.onopen = function (session, details) {
   console.log("session open!", details);

   // Your code goes here: use WAMP via the session you got to
   // call, register, subscribe and publish ..

   connection.close();
};

// .. and fire this code when our session has gone
connection.onclose = function (reason, details) {
   console.log("session closed: " + reason, details);
}

// Don't forget to actually trigger the opening of the connection!
connection.open();
