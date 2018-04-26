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
    console.log(csrftoken);
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
    

    $('#likeForm').on('submit',function(event){
        event.preventDefault();
        var me=$(this)
        $.ajax({
            url: $(this).attr('action'), /* Where should this go? */
            method: 'post', /* Which HTTP verb? */
            data: $(this).serialize(), /* Any data to send along? */
            success: function(serverResponse) { /* What code should we run when the server responds? */
              if(serverResponse['errors'])
                console.log(serverResponse['errors'])
              else{
                console.log(serverResponse)
                $(me).find('button').html("<i class='fas fa-thumbs-up fa-lg' style='color:orange'></i>");
                if($(me).next().length>0)
                    $(me).closest('div').append("<span><h6><a id='like_"+ serverResponse.userid +"{{u.id}}' href='/accounts/profile/"+ serverResponse.userid +"'>, "+ serverResponse.username +"</a></h6></span>")
                else
                $(me).closest('div').append("<span><h6><a id='like_"+ serverResponse.userid +"{{u.id}}' href='/accounts/profile/"+ serverResponse.userid +"'>"+ serverResponse.username +"</a></h6></span>")
              }          
            }
          })
    })




})