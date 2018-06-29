$(document).ready(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    // console.log(csrftoken);
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
     });
//=================== UI staff =========================   
    // var userList_display=sessionStorage.getItem('userlist_is_display')
    // console.log(sessionStorage.getItem('userlist_is_display'));
    if(sessionStorage.getItem('userlist_is_display')=='1'){
        // console.log(userList_display)
        $('.userList').show()
    }
   
    var chatwindow_display=sessionStorage.getItem('chatwindow_id_display')
    var lc=sessionStorage.getItem('last_chat_id')
    var lcn=sessionStorage.getItem('last_chat_name')
    var clinet=sessionStorage.getItem('user_id')


    
        

    
    

//=================== INIT USER =========================
    
    jsuser.client=clinet;
    if(!jsuser.username==''){
        var img=$('.own-img').prop('src');
        jsuser['img']=img;
        jsuser.isUser=true;  
        jsuser.client=jsuser.user_id  
    }
       
    

    // var server='http://127.0.0.1:6789'
    // var server='http://13.57.221.111:6789';
    var socket = io.connect('http://127.0.0.1:6789',{
        reconnection: true,
        reconnectionDelay: 1000,
        reconnectionDelayMax : 5000,
        reconnectionAttempts: Infinity
      });
    // console.log(jsuser)
    
    socket.once('connect',function(){
        socket.emit('authentication',jsuser)
        if(chatwindow_display=='1'){
            $('.chat_window').show()
            $('.chat-avatar').text(lcn)
            $('.render_uid').val(lc)
            // if(lc.includes('G')||clinet.includes('G')){
                socket.emit('load_conversation',{'sender':clinet,'receiver':lc})
                socket.on('return_conversations',function(data){
                    $('.chat_content').html("<ul class='messages'></ul>")
                    $('.messages').attr('id','chat'+lc)
                    // console.log(data.messages.length)
                    for(var x=0;x<data.messages.length;x++){
                        if(jsuser.user_id==data.messages[x].sender)
                            $('.messages').append("<li class='message right appeared'><div class='avatar'><img src=\'"+jsuser.img+"\' class='circle responsive-img hoverable'></div><div class='text_wrapper'><div class='text'>"+data.messages[x].content+"</div></div></li>")
                        else
                            $('.messages').append("<li class='message left appeared'><div class='avatar'><img src=\'"+$('#'+lc).find('img').prop('src')+"\' class='circle responsive-img hoverable'></div><div class='text_wrapper'><div class='text'>"+data.messages[x].content+"</div></div></li>")   
                    }
                    $('.messages').animate({scrollTop: $('.messages').prop("scrollHeight")}, 500);
                })
            //}
            // else{
            //     $.ajax({
            //         url:'/chat/users',
            //         method:'post',
            //         data:{'uid':lc,'cid':clinet},
            //         // type:'clone',
            //         success: function(serverResponse){
            //             $('.chat_content').html(serverResponse)
            //             $('.messages').animate({scrollTop: $('.messages').prop("scrollHeight")}, 500);
            //             }
            //         })
            // }
        }
    })

    socket.on('generate_id',function(data){
        // console.log(data)
        sessionStorage.setItem('user_id',data.client_id)
    })


    socket.on('my_full_broadcast_event',function(data){
        if(data.count>=2)  
            $('#chat_title').text('You and '+(data.count-1)+ ' users are online');
        else
            $('#chat_title').text('You are online');
        var l='';
       
    //    console.log(data.users)
        $('#user_list').empty();
        for(x=0;x<data.users.length;x++){
            if(!jsuser.isUser&&socket.id==data.users[x].cid)
                jsuser=data.users[x]
            if(socket.id!=data.users[x].cid){
                if(!jsuser.isUser){
                    l+="<li class='collection-item avatar show_btn_node' id=\'"+data.users[x].user_id+"\'><img src=\'"+data.users[x].img+"\' class='circle'><span class='title'>"+data.users[x].username+"</span><p>"+data.users[x].platform+"</p><p class='nn' style='display:none'>0</p><input class='cid' type='hidden' value=\'"+data.users[x].cid+"\'><a href='#' class='secondary-content orange-text'><i class='material-icons orange-text'>chat</i></a></li>";
                }
                else{
                    if(data.users[x].isUser)
                    l+="<li class='collection-item avatar show_btn_node' id=\'"+data.users[x].user_id+"\'><img src=\'"+data.users[x].img+"\' class='circle'><span class='title'>"+data.users[x].username+"</span><p>"+data.users[x].platform+"</p><p class='nn' style='display:none'>0</p><input class='cid' type='hidden' value=\'"+data.users[x].cid+"\'><a href='#' class='secondary-content orange-text'><i class='material-icons orange-text'>chat</i></a></li>";
                    else
                    l+="<li class='collection-item avatar show_btn_node' id=\'"+data.users[x].user_id+"\'><img src=\'"+data.users[x].img+"\' class='circle'><span class='title'>"+data.users[x].username+"</span><p>"+data.users[x].platform+"</p><p class='nn' style='display:none'>0</p><input class='cid' type='hidden' value=\'"+data.users[x].cid+"\'><a href='#' class='secondary-content orange-text'><i class='material-icons orange-text'>chat</i></a></li>";
                }                
            }
                
        }
        
        $('#user_list').append(l)
        $('.show_btn').on('click',function(event){  
            var me=$(this)
            if($('.chat_window').is(':hidden')){
                $('.chat_window').slideToggle();
            }
            $('.chat-avatar').text($(this).find('.title').text())
            $('.render_uid').val($(this).attr('id'))
            if(!$(this).find('.nn').is(':hidden')){
                $(this).find('.nn').fadeOut();
            }
            $(this).find('.nn').text('0')
            $.ajax({
            url:'/chat/users',
            method:'post',
            data:{'uid':$(this).attr('id'),'cid':$(this).find('.cid').val()},
            // type:'clone',
            success: function(serverResponse){
                $('.chat_content').html(serverResponse)
                $('.messages').animate({scrollTop: $('.messages').prop("scrollHeight")}, 500);
                }
            })
            sessionStorage.setItem('chatwindow_id_display','1')
            sessionStorage.setItem('last_chat_id',$(this).attr('id'))
            sessionStorage.setItem('last_chat_name',$(this).find('.title').text())
         });
         $('.show_btn_node').on('click',function(event){
            var me=$(this)
            if($('.chat_window').is(':hidden')){
                $('.chat_window').slideToggle();
            }
            
            // $('.chat_content').empty()
           

            $('.chat-avatar').text($(this).find('.title').text())
            $('.render_uid').val($(this).attr('id'))
            if(!$(this).find('.nn').is(':hidden')){
                $(this).find('.nn').fadeOut();
            }
            $(this).find('.nn').text('0')
            socket.emit('load_conversation',{'sender':jsuser.user_id,'receiver':$(this).attr('id')})
            socket.on('return_conversations',function(data){
                $('.chat_content').html("<ul class='messages'></ul>")
                $('.messages').attr('id','chat'+me.attr('id'))
                // console.log(data.messages.length)
                for(var x=0;x<data.messages.length;x++){
                    if(jsuser.user_id==data.messages[x].sender)
                        $('.messages').append("<li class='message right appeared'><div class='avatar'><img src=\'"+jsuser.img+"\' class='circle responsive-img hoverable'></div><div class='text_wrapper'><div class='text'>"+data.messages[x].content+"</div></div></li>")
                    else
                        $('.messages').append("<li class='message left appeared'><div class='avatar'><img src=\'"+me.find('img').prop('src')+"\' class='circle responsive-img hoverable'></div><div class='text_wrapper'><div class='text'>"+data.messages[x].content+"</div></div></li>")   
                }
                $('.messages').animate({scrollTop: $('.messages').prop("scrollHeight")}, 500);
            })
            sessionStorage.setItem('chatwindow_id_display','1')
            // console.log($('.messages').attr('id'))
            sessionStorage.setItem('last_chat_id',$(this).attr('id'))
            sessionStorage.setItem('last_chat_name',$(this).find('.title').text())
     })
    })

    socket.on('received_message',function(data){
       console.log(data);
       M.toast({html:data.username+' sent you a message.'})
       var last_left=''
       if(jsuser.isUser)
            last_left="<li class='message left appeared'><div class='avatar'><a href='/accounts/profile/"+data.user_id+"\'><img src=\'"+data.img+"\' class='circle responsive-img hoverable'></a></div><div class='text_wrapper'><div class='text'>"+data.msg+"</div></div></li>"
       else
            last_left="<li class='message left appeared'><div class='avatar'><img src=\'"+data.img+"\' class='circle responsive-img hoverable'></div><div class='text_wrapper'><div class='text'>"+data.msg+"</div></div></li>"
       if($('.messages').attr('id')=='chat'+data.user_id){
            $('.messages').append(last_left)   
            $('.messages').animate({scrollTop: $('.messages').prop("scrollHeight")}, 500);
       }
       else
       $('#'+data.user_id).find('.nn').text(parseInt($('#'+data.user_id).find('.nn').text())+1+' new').fadeIn();
       
       $('#'+data.user_id).find('img').fadeTo(1000, 0.3 ).fadeTo(1000, 1).fadeTo(1000, 0.3 ).fadeTo(1000, 1).fadeTo(1000, 0.3 ).fadeTo(1000, 1).fadeTo(1000, 0.3 ).fadeTo(1000, 1); 
       
       if($('.userList').is(':hidden')){
            $('#total_new').text(parseInt($('#total_new').text())+1).fadeIn();
       }
    })


    $('.chat_wrapper').on('click',function(event){  
       $('.userList').slideToggle('slow',function(){
        if($('.userList').is(':hidden')){
            sessionStorage.setItem('userlist_is_display','0')
        }
        else
            sessionStorage.setItem('userlist_is_display','1')
       });
       $('#total_new').fadeOut();
    });
    
    $('#close-chat').click(function(){
        $('.chat-avatar').empty();
        $('.chat_window').fadeOut();
        sessionStorage.setItem('chatwindow_id_display','0')
    })
    
    $('#send_msg_btn').click(function(){
        if($('#msg_type_content').val()!==''){
            // if(!$('.render_uid').val().includes('G')&&jsuser.isUser){
            // $.ajax({
            //         url:'/chat/users',
            //         method:'post',
            //         data:{'rid':$('.render_uid').val(),'msg_type_content':$('#msg_type_content').val(),'purpose':'add a message'},
                   
            //         // type:'clone',
            //         success: function(serverResponse){
            //             if(serverResponse['success']){
            //                 var last_right="<li class='message right appeared'><div class='avatar'><a href='/accounts/profile/"+jsuser.user_id+"\'><img src=\'"+jsuser.img+"\' class='circle responsive-img hoverable'></a></div><div class='text_wrapper'><div class='text'>"+$('#msg_type_content').val()+"</div></div></li>"
            //                 $('.messages').append(last_right)   
            //                 $('.messages').animate({scrollTop: $('.messages').prop("scrollHeight")}, 500);
            //                 jsuser['client_id']=$('.messages').attr('id');
            //                 jsuser['msg']=$('#msg_type_content').val()
            //                 socket.emit('new_message',jsuser)
            //                 $('#msg_type_content').val('')
            //             }   
            //         }
            //     })
            // }
            // else{
                console.log($('.messages').attr('id'))
                socket.emit('new_message_node',{'sender':jsuser,'receiver':$('.render_uid').val(),'receiver_id':$('.messages').attr('id'),'content':$('#msg_type_content').val()})
                // socket.on('add_message',function(data){
                    // console.log(data)
                    var last_right="<li class='message right appeared'><div class='avatar'><img src=\'"+jsuser.img+"\' class='circle responsive-img hoverable'></div><div class='text_wrapper'><div class='text'>"+$('#msg_type_content').val()+"</div></div></li>" 
                    $('.messages').append(last_right)   
                    $('.messages').animate({scrollTop: $('.messages').prop("scrollHeight")}, 500);  
                    $('#msg_type_content').val('')
                // })
            }
        // }
    })
    // console.log('sb')
    
    

    
})
