const {PythonShell} = require("python-shell");
    var path = require("path")

    var options = {
        scriptPath : path.join(__dirname, '../python/')
    }

    var barcode = new PythonShell('bcode.py', options)

    barcode.on('message', function(message) {
        console.log(message)  
        window.location.href = "final.html"    
    })
