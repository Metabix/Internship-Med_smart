let json = require('../js/bcode.json');

let name = document.getElementById("detect-name");

name.innerHTML = json["camera"]

var delayInMilliseconds = 10000; //5 second

	setTimeout(function() {
		window.location.href = "index.html"
	}, delayInMilliseconds);
