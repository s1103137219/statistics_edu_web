
$('document').ready(function(){
    
    
    //start css
    $('img').hide()
    $('#plot').css('background','#bfbcbc')
    $('#plot').hover(function(){
        $(this).css('background','#ebebeb')
    },function(){
        $(this).css('background','#bfbcbc')
    })

    //new editor
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.getSession().setMode("ace/mode/python");
    document.getElementById('editor').style.fontSize='20px';
    editor.container.style.fontFamily = "monospace"
    
    //get editor to textarea
    editor.getSession().on('change', function(){ 
        var code= editor.getSession().getValue(); 

        $('#p').val(code)
});
    //new editor_output
    var editor_output = ace.edit("ace-editor");
    editor_output.setTheme("ace/theme/tomorrow_night");//iplastic的字體顏色喜歡
    editor_output.getSession().setMode("ace/mode/python");
    document.getElementById('ace-editor').style.fontSize='20px';
    editor_output.container.style.fontFamily = "monospace"



// output to plot
$('#plot').click(function(){
    $('#img').show()
    $('img').show()
    $('#ace-editor').hide()
    $('#output').css('background','#bfbcbc')
    
    $('#output').hover(function(){
      $(this).css('background','#25282c')
    },function(){
        $(this).css('background','#bfbcbc')
    })
    
    $('#plot').hover(function(){
      $(this).css('background','')
    },function(){
        $(this).css('background','')
    })
    
    $('#plot').css('background','#25282c')
})
//plot to output
$('#output').click(function() {
    $('#ace-editor').show()
    $('#img').hide()
    $('img').hide()
    $('#plot').css('background','#bfbcbc')
    
    $('#plot').hover(function(){
      $(this).css('background','#25282c')
    },function(){
        $(this).css('background','#bfbcbc')
    })
    $('#output').hover(function(){
      $(this).css('background','')
    },function(){
        $(this).css('background','')
    })
    $('#output').css('background','#25282c')
})
})

