var autobahn = require('autobahn');

const url = process.argv[2];
const realm = process.argv[3];

var connection = new autobahn.Connection({url: url, realm: realm});

connection.onopen = function (session, details) {
   console.log("session open!", details);
   connection.close();
};

connection.onclose = function (reason, details) {
   console.log("session closed: " + reason, details);
}

connection.open();
