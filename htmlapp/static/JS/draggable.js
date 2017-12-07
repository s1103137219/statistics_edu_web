 $(function() {
    $("#draggable").draggable();
    
  });
  $(document).ready(function(){
      $(".close").click(function(){
           $("#draggable").hide();
          
      })
    $("#help").click(function(){
        $("#draggable").show();
    })
  })
    