

const {PythonShell} = require("python-shell");
    var path = require("path")

    var options = {
        scriptPath : path.join(__dirname, '../python/')
    }

    var websocketcode = new PythonShell('get_MQTT_data.py', options)

    websocketcode.on('message', function(message) {
        console.log(message)
        
        window.location.href = "temperature.html"
    
        
    })
