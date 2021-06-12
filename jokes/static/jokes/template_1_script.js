function toggleDisplay(id, element=false){
//to toggle display of any element
  if (element){
    element=id;
    console.log('\nElement True')
  } else{
    //console.log('\nElement False')
    element = document.getElementById(id);
  }
  if (element.style.display == "none"){
    //console.log('\ndisplays block')
    element.style.display = "block";
    //console.log(0)
  } else{
    //console.log(element);
    //console.log('\ndisplays none')
    element.style.display = "none";
    //console.log(1);
    //console.log(element);
  }
}


function store_and_display(joke){
  console.log('store_and_display:'+joke);
  var nascent_joke = joke;
  console.log('nascent_joke:'+joke);
}
