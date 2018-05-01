$(document).ready(function(){
    var server='http://127.0.0.1:6789'
    // var server='http://13.57.221.111:6789';
    var socket = io.connect(server);
    var img=$('.own-img');
    jsuser['img']=img;
    // console.log(img)
    socket.once('connect',function(){
        socket.emit('authentication',jsuser)
    })

    socket.on('my_full_broadcast_event',function(data){
        if(data.count>2)  
            $('#chat_title').text('You and '+data.count-1+' users are online');
        else if(data.count==2)
            $('#chat_title').text('You and 1 user are online');
        else
            $('#chat_title').text('You are online');
        var l='';
        for(x=0;x<data.users.length;x++){
            if(jsuser.user_id==data.users[x].user_id)
            l+="<li class='collection-item'><div>"+data.users[x].username+"</div></li>"
            else
            l+="<li class='collection-item'><div>"+data.users[x].username+"<a href='#!' class='secondary-content'><i class='material-icons'>send</i></a></div></li>"
        }
        $('#user_list').html(l)
    })

    // socket.on('disconnect',function(){
    //     socket.emit('clear',jsuser)
    // })
})
