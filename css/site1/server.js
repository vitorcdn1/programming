var http = require("http")
var dt = require("./index")

http.createServer(function (req, res){
        res.writeHead(200, {"Content-Type": "text/html"})
        res.end(req.url)
}).listen(8080)

console.log("running")