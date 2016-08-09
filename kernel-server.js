var http = require('http');

const PORT=80;

function handleRequest(request, response){
    response.end('Testing... ' + request.url);
}

var server = http.createServer(handleRequest);

server.listen(PORT, function(){
    console.log("Server listening on: http://localhost:%s", PORT);
});
