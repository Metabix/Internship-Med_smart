let successDiv = document.getElementById("success-div");
let failureDiv = document.getElementById("failure-div");

let json = require('../js/temperature.json');

if(parseFloat(json['temperature']) > 98.60) 
{
	failureDiv.style.display = "initial";
	
	var delayInMilliseconds = 10000; //5 second

	setTimeout(function() {
		window.location.href = "index.html"
	}, delayInMilliseconds);
} 
else 
{
	successDiv.style.display = "initial";
	
	var delayInMilliseconds = 5000; //5 second

	setTimeout(function() {
		window.location.href = "bcode.html"
	}, delayInMilliseconds);
}
