$(function () {
  console.log('progress-bar');
  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType: 'json',
    url:'/dish/uplaods/',
    sequentialUploads: true,

    start: function (e) {
      $("#modal-progress").modal("show");
    },

    stop: function (e) {
      $("#modal-progress").modal("hide");
    },

    progressall: function (e, data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);
    },

    done: function (e, data) {
      console.log(data.result.is_valid);
      console.log(data);
      if (data.result.is_valid) {
        console.log(data.result.is_valid);
        console.log('\"' + data.result.url+'\"');
        $("#gallery tbody").prepend(
          "<tr><td><img src="+data.result.url+"></td></tr>"
        )
      }
    }

  });

});
