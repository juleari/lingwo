var fs     = require('fs'),
    parseD = require('./lab3').stat;

function route (response, pathname, data) {

    function writeJSON(data) {

        var str  = JSON.stringify(data);

        response.writeHead(200, {"Content-Type": "application/json"});
        response.write(str);
        response.end();
    }

    function index() {
        var html = fs.readFileSync(__dirname + '/index.html', {encoding: 'utf-8'});

        response.writeHead(200, {"Content-Type": "text/html"});
        response.write(html);
        response.end();
    }

    function stat() {

        var type  = 'application/json',
            style = /\/css(.*\.css)/,
            js    = /\/js(.*\.js)/,
            img   = /\/img(.*\..*)/;

        if ( style.test(pathname) ) type = 'text/css';
        if ( js.test(pathname)    ) type = 'text/javascript';
        if ( img.test(pathname)   ) type = 'image/png';
  
        fs.readFile(__dirname + pathname, "binary", function(error, file) {
            
            if (error) {

                response.writeHead(500, {"Content-Type": "text/plain"});
                response.write(error + "\n");
                response.end();

            } else {

                response.writeHead(200, {"Content-Type": type});
                response.write(file, "binary");
                response.end();
            }
        });
    }

    function update() {
        var text = fs.readFileSync(__dirname + '/data/data.json', {encoding: 'utf-8'})
            json = JSON.parse(text);

        console.log('json', json);
        response.writeHead(200, {"Content-Type": "application/json"});
        response.write(json);
        response.end();
    }

    console.log('data', !!data);

    if (data) update() 
    else {

        if (pathname == '/') index()
        else if (pathname == '/data') parseD('MM.txt', writeJSON);
            else stat()

    }
}

exports.route = route;