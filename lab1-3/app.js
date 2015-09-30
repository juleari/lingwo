var http = require('http'),
    url  = require('url'),
    views= require('./views');

(function() {
    
    function onRequest(request, response) {

        var callback_error = function(number) {

            console.log('callback_error', number);
            
            response.writeHead(number, {"Content-Type": "text/plain"});
            response.write('error' + number);
            response.end();
        }

        var pathname = url.parse(request.url).pathname,
            data = "";
        
        request.setEncoding("utf8");

        request.addListener("data", function(dataChunk) {
          
            data += dataChunk;
        });

        request.addListener("end", function(dataChunk) {

            console.log(dataChunk, pathname);
            
            views.route(response, pathname, data);
        });
    }

    http.createServer(onRequest).listen(3003);
    console.log("Server has started.");
})();