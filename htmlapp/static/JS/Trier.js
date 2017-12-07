

$(document).ready(function(){
  var c=$(".card")
  
  var num=0
  
  var trlen=Math.round((c.length)/2)
  var trarray=Array(trlen)
  
  var tdlen=(c.length)
  var tdarray=Array(tdlen)
  
  for(var j=0;j<trarray.length;j++){
      var tr=$("<tr></tr>")
      trarray[j]=tr
      trarray[j]=Array(tdarray.length)
  for(var i=0 ; i<2;i++){
      var td=$("<td></td>")
      trarray[j][i]=td
      tr.append(trarray[j][i])
     trarray[j][i].append(c[num])
     num=num+1
     
     
     $(".course").append(tr) 
     }
      
  }
     
 

  
})