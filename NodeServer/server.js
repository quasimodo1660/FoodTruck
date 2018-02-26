// Import express and path modules.
var express = require( "express");
var path = require( "path");
var app = express();

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
        socket.broadcast.emit( "my_broadcast_event",{message:data.message});
    })
})
