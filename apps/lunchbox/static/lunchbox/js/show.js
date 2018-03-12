// function showhide()
// {
//       var div = document.getElementById("newpost");
// if (div.style.display !== "none") {
//    div.style.display = "none";
// }
// else {
//    div.style.display = "block";
// }
// }

$('#post-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    console.log('Sending Ajax request to', $(this).attr('action'))
    console.log('Submitting the following data', $(this).serialize())
    $.ajax({
        url: $(this).attr('action'), /* Where should this go? */
        method: 'post', /* Which HTTP verb? */
        data: $(this).serialize(), /* Any data to send along? */
        success: function(serverResponse) { /* What code should we run when the server responds? */
          if(serverResponse['errors'])
            console.log(serverResponse['errors'])
          else{
            $('#lunchboxID').val(serverResponse['lID'])
            $('#lunchBoxID2').val(serverResponse['lID'])
          }          
        }
      })
});
//this should change
function showDiv() {
    document.getElementById('welcomeDiv').style.display = "block";
 }

 //var languages = ["d","fr","en","es","it",];
 
//  $('#langtabs').tabSelect({
//    tabElements: languages,
//    selectedTabs: [ ]
//  });
//  $('#langtabs2').tabSelect({
//    tabElements: languages,
//    selectedTabs: [ ]
//  });
 
