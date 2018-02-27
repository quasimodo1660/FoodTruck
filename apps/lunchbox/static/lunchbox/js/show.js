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
    create_post();
});
function create_post() {
    console.log("create post is working!") // sanity check
    console.log($('#post-title').val())
    console.log($('#post-description').val())
};
function showDiv() {
    document.getElementById('welcomeDiv').style.display = "block";
 }

 var languages = ["d","fr","en","es","it",];
 
//  $('#langtabs').tabSelect({
//    tabElements: languages,
//    selectedTabs: [ ]
//  });
//  $('#langtabs2').tabSelect({
//    tabElements: languages,
//    selectedTabs: [ ]
//  });
 
