$(document).ready(function(){
    console.log('showImg working');
    // init Masonry
    // https://codepen.io/craigwheeler/pen/MYjBga
    var $grid = $('.grid').masonry({
        
        // set itemSelector so .grid-sizer is not used in layout
        // itemSelector: '.grid-item',
        // use element for option
        // columnWidth: '.grid-sizer',
        // percentPosition: true
        
        itemSelector: '.grid-item',
        isFitWidth: true,
        columnWidth: 5
    });
    // layout Masonry after each image loads
    $grid.imagesLoaded().progress( function() {
      $grid.masonry('layout');
    });            


});
// emily's. for close button.
var targetArea = document.getElementById("ShowArea").style;

function closead() {
    targetArea.display = 'none';
}

// for add button
var bodyfrm = (document.compatMode.toLowerCase() == "css1compat") ? document.documentElement : document.body;

var addbutton = document.getElementById("addLunboxButton").style;
addbutton.top = (bodyfrm.clientHeight - 530 - 22) + "px";

function moveR() {
    addbutton.top = (bodyfrm.scrollTop + bodyfrm.clientHeight - 530 - 22) + "px";
}
setInterval("moveR();", 80);