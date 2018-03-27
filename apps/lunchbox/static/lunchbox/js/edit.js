$(document).ready(function(){
    $("#update_info_form").on('submit',function(event){
        event.preventDefault();
        // $(this).find('#time').val($(this).find('#time').val().toString('%d %B, %Y'))
       
        var time=$(this).find('#date').val()+' '+convertDateTo24Hour($(this).find('#time').val())
        // $(this).find('#time').val(time)
        // console.log($(this).find('#time').val())
        // $('.clicked_me').addClass('dismiss_me');
        var me=this
        $.ajax({
            url: $(this).attr('action'), /* Where should this go? */
            method: 'post', /* Which HTTP verb? */
            data: $(this).serialize(), /* Any data to send along? */
            success: function(serverResponse) { /* What code should we run when the server responds? */
              if(serverResponse['errors'])
                console.log(serverResponse['errors'])
              else{
                console.log(serverResponse['success'])
              }          
            }
          })
       
    })
   

})

function convertDateTo24Hour(date){
    var elem = date
    var stSplit = elem[1].split(":");// alert(stSplit);
    var stHour = stSplit[0];
    var stMin = stSplit[1];
    var stAmPm = elem[2];
    var newhr = 0;
    var ampm = '';
    var newtime = '';
    //alert("hour:"+stHour+"\nmin:"+stMin+"\nampm:"+stAmPm); //see current values
    
    if (stAmPm=='PM')
    { 
        if (stHour!=12)
        {
            stHour=stHour*1+12;
        }
       
    }else if(stAmPm=='AM' && stHour=='12'){
       stHour = stHour -12;
    }else
        stHour=stHour;

    return elem[0]+" "+stHour+':'+stMin;
}