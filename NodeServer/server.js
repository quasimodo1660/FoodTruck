// Import express and path modules.
var express = require( "express");
var path = require( "path");
var app = express();
var bodyParser = require('body-parser');
//set nodemailer
const nodemailer = require('nodemailer');
var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: 'bentoman1660@gmail.com',
      pass: 'syxqG2103'
    }
  });
var mailOptions = {
    from: 'bentoman1660@gmail.com',
    to: 'quasimodo1660@gmail.com',
    subject: 'Client socket is connected!',
    text: 'Client socket is connected!! Check it please.'
  };
  
const g = require('node-unique-id-generator');



var server=require('http').Server(app);
server.listen(6789, function() {
 console.log("listening on port 6789");
})
var guset_id=0;
function makeid() {
    var text = "";
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
  
    for (var i = 0; i < 5; i++)
      text += possible.charAt(Math.floor(Math.random() * possible.length));
  
    return text;
  }

class Message{
    constructor(sender,sender_username,sender_img,receiver,content,mid=g.generateGUID()){
        this.sender=sender;
        this.sender_username=sender_username
        this.sender_img=sender_img
        this.receiver=receiver;
        this.content=content  
        this.mid=mid
        this.createdAt=new Date()
    }
}

// class Conversation{
//     constructor(id){
//         this.chat_user_id=id;
//         this.messages=[];
//     }
// }

class Client{
    constructor(cid,isuser,id='G'+guset_id,username='GUEST',img='https://api.adorable.io/avatars/135/'+makeid()+'.png'){
        this.user_id=id;
        this.cid=cid;
        this.username=username
        this.conversations=[];
        this.isUser=isuser;
        this.img=img
        this.platform='Web Browser'
    }
}

var users=[];
var userList=[];
var messages=[];
var userCounter=0;
var io = require('socket.io')(server);
io.sockets.on('connection',function(socket){
    userCounter++;
    guset_id++;
    // console.log(socket)
    console.log('Client socket is connected!');
    var temp=socket.id
    console.log(userCounter);
    
    socket.on('authentication',function(data){  
        console.log(data);
        var user=users.find(function(x){
            return x.user_id==data.client
        })
        // console.log('user in users'+user)
        if(user==undefined){
            // transporter.sendMail(mailOptions, function(error, info){
        //     if (error) {
        //       console.log(error);
        //     } else {
        //       console.log('Email sent: ' + info.response);
        //     }
        //   });
            var client;
            if(data.isUser){
                client = new Client(temp,true,data['user_id'],data['username'],data['img'])
                users.push(client);
                userList.push(client)
            }
            else{            
                client = new Client(temp,false)
            
                users.push(client);
                userList.push(client)      
            }
            if(data.platform)  
                client.platform=data.platform
            else
                client.platform='Web Browser'
            socket.emit('generate_id',{'client_id':client.user_id,'client_name':client.username,'client_img':client.img})
        }
        else{
            user.cid=temp
            if(data.platform)
                user.platform=data.platform
            else
                user.platform='Web Browser'
            userList.push(user)
        }
           



        
        console.log(userList)
        io.emit( "my_full_broadcast_event",{count:userCounter,users:userList});
    })
    
    
    
    socket.on('disconnect',function(){
        userCounter--;
        console.log(userCounter);
        var dis_client=userList.find(function(x){
            return x.cid==socket.id
        })
        // console.log(dis_client)
        userList=userList.filter(function(x){
            // console.log(x)
            return x.cid!=socket.id;
        })
        // console.log(userList)
        // messages=messages.filter(function(x){
        //     return x.sender!=dis_client.user_id
        // }).filter(function(x){
        //     return x.receiver!=dis_client.user_id
        // })
        // console.log(messages)
        io.emit( "my_full_broadcast_event",{count:userCounter,users:userList});
    })
    
    socket.on('load_conversation',function(data){
        // var found = userList.find(function(x){
        //     return x.cid==socket.id
        // }).conversations.find(function(y){
        //     return y.chat_user_id == data.index
        // })
        // if(found)
        //     io.emit('return_conversations',{'messages':found.messages})
        // else{
        //     var con = new Conversation(data.index)
        //     userList.find(function(x){
        //         return x.cid==socket.id
        //     }).conversations.push(con)
        //     io.emit('return_conversations',{'messages':con.messages})
        // }
        // console.log(data)
        var conversation=messages.filter(function(x){
            return (x.sender==data.sender&&x.receiver==data.receiver)||(x.sender==data.receiver&&x.receiver==data.sender)
        })
        console.log('conversation'+conversation)
        socket.emit('return_conversations',{'messages':conversation})
            
    })


    socket.on('new_message', function(data) {
        data['sender_id']=socket.id
        var receiver=users.find(function(x){
            return x.user_id==data.client_id.replace('chat','')
        })
        socket.broadcast.to(receiver.cid).emit( "received_message",data);
    })
    socket.on('new_message_node',function(data){
        // console.log(data)
        // var msg = new Message(true,false,data.content)
        // userList.find(function(x){
        //     return x.user_id==data.receiver_id
        // }).conversations.find(function(y){
        //     return y.chat_user_id==data.receiver
        // }).messages.push(msg);
        // socket.broadcast.to(data.sender.cid).emit('add_message',{'dbb':'sbb'})
        var receiver=users.find(function(x){
            return x.user_id==data.receiver
        })
        // console.log(receiver)
        var msg = new Message(data.sender.user_id,data.sender.username,data.sender.img,data.receiver,data.content,data.mid)
        messages.push(msg)
        console.log(messages)
    
        var rdata={}
        rdata['username']=data.sender.username
        rdata['sender_id']=socket.id
        rdata['img']=data.sender.img
        rdata['user_id']=data.sender.user_id
        rdata['msg']=data.content
        socket.broadcast.to(receiver.cid).emit( "received_message",rdata);
        socket.broadcast.to(receiver.cid).emit( "rn_received_message",msg);
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
