// Import express and path modules.
var express = require( "express");
var path = require( "path");
var app = express();
var bodyParser = require('body-parser');

var server=app.listen(6789, function() {
 console.log("listening on port 6789");
})
var userCounter=0;
var io = require('socket.io').listen(server);
io.sockets.on('connection',function(socket){
    userCounter++;
    console.log('Client socket is connected!');
    console.log(userCounter);
    io.emit( "my_full_broadcast_event",{count:userCounter});
    socket.on('disconnect',function(){
        userCounter--;
        console.log(userCounter);
        io.emit( "my_full_broadcast_event",{count:userCounter});
    })
    socket.on('newMessage', function(data) {
        console.log(data);
        socket.broadcast.emit( "my_broadcast_event",{message:data.message,user:data.name});
    })
})

app.use(function (req, res, next) {

    // Website you wish to allow to connect
    res.setHeader('Access-Control-Allow-Origin', 'http://localhost:8000');
    res.setHeader('Access-Control-Allow-Origin', 'http://127.0.0.1:8000');

    // Request methods you wish to allow
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');

    // Request headers you wish to allow
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');

    // Set to true if you need the website to include cookies in the requests sent
    // to the API (e.g. in case you use sessions)
    res.setHeader('Access-Control-Allow-Credentials', true);

    // Pass to next layer of middleware
    next();
});



app.post('/test',function(req,res){
    console.log(req.body);
    res.send('sbb');
})
