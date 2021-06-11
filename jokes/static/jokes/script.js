//For dark mode
function darkFunction() {
   var element = document.body;
   element.classList.toggle("dark-mode");
}/*window.onload = darkFunction;*/




//<!--################## Ajax jokes ################################-->

/*readMore();
// For adding jokes at the bottom

/*function getJokes(){
//alert("What is this?");
  //Jokes repeating

         //alert('I want her')
         // This detaches the scroll so doStuff() won't run more than once
         //$(window).off('scroll');
         //alert('I am getting her')
       
     

/*
  $(window).scroll(function() {  
       if($(window).scrollTop() + $(window).height() == $(document).height()) {  *
         
         //Runs when at the bottom of page
         //alert("bottom!");
         //console.log('I want her')
          
          $.ajax({
              type: 'GET',
              url: "{% url 'get_jokes' %}",
              data: {"last_joke_id": newMax},
              success: function (response) {
                  // if not valid user, alert the user
                  //alert("What is this?");
                  /*if(!response["valid"]){
                      alert("You cannot create a friend with same nick name");
                      var nickName = $("#id_nick_name");
                      nickName.val("")
                      nickName.focus()
                  }/
                  
                  var instance = JSON.parse(response["jokes"]);
                  console.log(instance)
                  var jokes = instance[0]["fields"];
                  //console.log();
                  //console.log(jokes);
                  for (i=0;i<10;i++){
                    //console.log(instance[i]['fields']['title']);
                    //############### Nested divs Here ########################
                    
                    function createParagraph() {
                      let section = document.createElement('section');
                    
                    
                    //let section.textContent = 'You clicked the button!';
                    section.setAttribute("id", newMax+1);
                    document.body.appendChild(section);
                    
                    let header = document.createElement('header');
                    header.setAttribute("class", "title-header");
                    header.textContent = instance[i]['fields']['title'];
                    section.appendChild(header);
                    //console.log(instance[i]['fields']['title']);
                    
                    let content = document.createElement('div');
                    content.setAttribute("class", 'content');
                    section.appendChild(content);
                    
                    let truncContent = document.createElement('div');
                    truncContent.setAttribute("id", 'truncatedDiv');
                    truncContent.textContent = instance[i]['fields']['body'].substring(0,250);
                    content.appendChild(truncContent);
  
                    
                    let hiddenContent = document.createElement('div');
                    hiddenContent.setAttribute("id", 'hiddenDiv');
                    hiddenContent.setAttribute("class", 'hidden');
                    hiddenContent.textContent = instance[i]['fields']['body'];
                    content.appendChild(hiddenContent);
                    
                    let readMoreBtn = document.createElement('button');
                    readMoreBtn.setAttribute("class", 'read-more-btn');
                    readMoreBtn.textContent = 'Read More';
                    content.appendChild(readMoreBtn);
                    
                    
                    
                    br=document.createElement('br')
                    document.body.append(br)
                    
                    newMax += 1;
                  /*$("#my_friends tbody").prepend(
                      `<tr>
                      <td>${jokes["nick_name"]||""}</td>
                      <td>${jokes["first_name"]||""}</td>
                      <td>${jokes["last_name"]||""}</td>
                      <td>${jokes["likes"]||""}</td>
                      <td>${jokes["dob"]||""}</td>
                      <td>${jokes["lives_in"]||""}</td>
                      </tr>`
                  )/
                  
                  };
                  createParagraph();
                  readMore();
              }
  
          },            error: function (response) {
                  console.log(response)
              }
          
          
     })}*/

//###################For Read More button -############################
/*
function readMore() {	
    var button = document.getElementsByClassName("read-more-btn");
    var i;
    //console.log(button.length)
    for (i=0; i<button.length; i++ ){
		var hiddenn = button[i].previousElementSibling;
		var truncated = button[i].previousElementSibling.previousElementSibling;
		
		if(truncated.innerHTML.length + 5 >= hiddenn.innerHTML.length) button[i].style.display="none";
		
		button[i].addEventListener("click", function() {
			
			//Truncated string lies two div behind button
			var truncated = this.previousElementSibling.previousElementSibling;
			if (truncated.style.display === "none") {
				truncated.style.display = "block";
				this.innerHTML = "Read More";
			} else {
				truncated.style.display = "none";
				this.innerHTML = "Read Less";
			}

			//hidden string lies one div behind button			
			var hiddenn = this.previousElementSibling;
			if (hiddenn.style.display === "block") {
				hiddenn.style.display = "none";
			} else {
				hiddenn.style.display = "block";
			}
		})}};//#####################################################

*/












/*function readMoreOne(id){	
  //console.log(this.textContent);
  main = document.getElementById(id);
  //console.log(main.querySelector('.truncatedDiv').textContent);
  truncatedDiv = main.querySelector('.truncatedDiv');
  
  //console.log('truncatedDiv: '+truncatedDiv);
  
  hiddenDiv = main.querySelector('.hiddenDiv');
  
  //console.log('hiddenDiv: '+hiddenDiv.textContent.length);
  
  button = main.querySelector('.read-more-btn');

			
  //truncatedDiv string lies two div behind button
  if (truncatedDiv.style.display === "none") {
  	truncatedDiv.style.display = "block";
  	button.textContent = "Read More";
  } else {
  	truncatedDiv.style.display = "none";
  	button.textContent = "Read Less";
  }

  //hiddenDiv string lies one div behind button  
  
  if (hiddenDiv.style.display === "block") {
  	hiddenDiv.style.display = "none";
  } else {
  	hiddenDiv.style.display = "block";
  }
}*/














//####################### For collapsable button #########################
function getCategories(){
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    } 
  });
}}

//#######################################################################



//###################For Comments -############################

function getCommentss(){
  input = document.createElement('input');
  input.appendChild('type','text');
  document.body.appendChild(input)
}


///////////////////////////////////////////////////////////////////////
//################### For appending jokes -############################
//\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

function appendJoke(title, truncatedContent, fullContent, jokeId, newMax) {
  //console.log('\n\n\n\n\nReceived:'+newMax);
  let main_div = document.createElement('div');
  main_div.setAttribute('id', "joke_count_" + String(parseInt(newMax) ));
  main_div.setAttribute('class', 'joke-container');
  document.body.appendChild(main_div);

  //let section.textContent = 'You clicked the button!';
  let section = document.createElement('section');
  section.setAttribute("id", 'section_'+jokeId);
  main_div.appendChild(section);
  
  let header = document.createElement('header');
  header.setAttribute("class", "title-header");
  header.textContent = title;
  section.appendChild(header);
  //console.log(instance[i]['fields']['title']);
  
  let content = document.createElement('div');
  content.setAttribute("class", 'content');
  section.appendChild(content);
  
  let truncContent = document.createElement('div');
    //setting id for readMore function
  truncContent.setAttribute("id", 'trunc_' + jokeId);
  truncContent.textContent = truncatedContent;
  content.appendChild(truncContent);
  
  style="display:none";  
  
  let hiddenContent = document.createElement('div');
    //setting id for readMore function
  hiddenContent.setAttribute("id", 'hidden_' + jokeId);
  hiddenContent.setAttribute("style", 'display:none;');
  hiddenContent.textContent = fullContent;
  content.appendChild(hiddenContent);
  
  let readMoreBtn = document.createElement('button');
  readMoreBtn.setAttribute("class", 'read-more-btn');
  readMoreBtn.setAttribute("onClick", 'readMoreOne('+jokeId+')');
  //if (jokeId==25){console.log('hi')
  if (fullContent.length <= 250 || truncatedContent.length +2 >= fullContent.length ) {
    readMoreBtn.setAttribute("style", 'display:none;');
  }
  readMoreBtn.textContent = 'Read More';
  content.appendChild(readMoreBtn);
  
  let love = document.createElement('div');
  love.setAttribute("class","love-icon");
  love.setAttribute("onClick","Love(" + jokeId + ")");
  love.setAttribute("id",'love_icon_' + jokeId);
  love.textContent = '♡';
  content.appendChild(love);
  
  let comment = document.createElement('div');
  comment.setAttribute("class", "comment-icon");
  comment.setAttribute("onClick","Comment(" + jokeId + ")");
  comment.textContent = "💬";//chat-emojis:💬💬🗯️💭💭👁️‍🗨️🗨️
  content.appendChild(comment);
  //<div class="love-icon" id={{joke.id}} onClick="Love()">♡</div>
  
  let br=document.createElement('br');
  main_div.append(br);
};

/*function createParagraph() {
                      let section = document.createElement('section');
                    
                    
                    //let section.textContent = 'You clicked the button!';
                    section.setAttribute("id", newMax+1);
                    document.body.appendChild(section);
                    
                    let header = document.createElement('header');
                    header.setAttribute("class", "title-header");
                    header.textContent = instance[i]['fields']['title'];
                    section.appendChild(header);
                    //console.log(instance[i]['fields']['title']);
                    
                    let content = document.createElement('div');
                    content.setAttribute("class", 'content');
                    section.appendChild(content);
                    
                    let truncContent = document.createElement('div');
                    truncContent.setAttribute("id", 'truncatedDiv');
                    truncContent.textContent = instance[i]['fields']['body'].substring(0,250);
                    content.appendChild(truncContent);
  
                    
                    let hiddenContent = document.createElement('div');
                    hiddenContent.setAttribute("id", 'hiddenDiv');
                    hiddenContent.setAttribute("class", 'hidden');
                    hiddenContent.textContent = instance[i]['fields']['body'];
                    content.appendChild(hiddenContent);
                    
                    let readMoreBtn = document.createElement('button');
                    readMoreBtn.setAttribute("class", 'read-more-btn');
                    readMoreBtn.setAttribute("onClick", 'readMoreOne()');
                    readMoreBtn.textContent = 'Read More';
                    content.appendChild(readMoreBtn);
                    
                    
                    
                    br=document.createElement('br')
                    document.body.append(br)
                    
                    
                  /*$("#my_friends tbody").prepend(
                      `<tr>
                      <td>${jokes["nick_name"]||""}</td>
                      <td>${jokes["first_name"]||""}</td>
                      <td>${jokes["last_name"]||""}</td>
                      <td>${jokes["likes"]||""}</td>
                      <td>${jokes["dob"]||""}</td>
                      <td>${jokes["lives_in"]||""}</td>
                      </tr>`
                  )*
                  
                  };
                  //createParagraph();*/


//################ For adding spinners to the end #######################

function appendSpinner(){
  
  //To remove previous spinner
  document.getElementById('spinner').remove();
  
  let spinner = document.createElement('div');
  spinner.setAttribute('class', 'spinner-grow text-secondary mx-auto d-block');
  spinner.setAttribute('id', 'spinner');
  spinner.setAttribute('style', 'width: 3rem; height: 3rem;');
  spinner.setAttribute('role', "status");
  
  let span = document.createElement('span');
  span.setAttribute("class", "visually-hidden");
  span.textContent = 'Loading...';
  document.body.append(spinner);
}

//Love();
//########################## To display commenting box  ###############
function commentingBox (id) {
  
  section = document.getElementById('section_'+id);
  console.log('Commenting Box. Got id:'+id);
//let comment = document.createElement('div');
  
  
  //let section.textContent = 'You clicked the button!';
//comment.setAttribute("class", 'comment-test');
//comment.textContent='test comment';
//getcomments(id);
  //console.log('id' + id);
  //console.log('class = ' + this.classList);
  //console.log('id = ' + this.id);
//section.appendChild(comment);
  
  //if(document.getElementById("comment_" + id) == null){
  
  let commentMain = document.createElement('div');
  commentMain.setAttribute("class", "container mt-2");
  commentMain.setAttribute("id", "comment_main_" + id);
  section.appendChild(commentMain);

  let commentMainRow = document.createElement('div');
  commentMainRow.setAttribute("class", "row justify-content-center");
  commentMain.appendChild(commentMainRow);

  let commentMainColumn = document.createElement('div');
  commentMainColumn.setAttribute("class", "col-md-8");
  commentMainRow.appendChild(commentMainColumn);
  
  let commentInputRow = document.createElement('div');
  commentInputRow.setAttribute("class","d-flex mt-3")
  commentMainColumn.appendChild(commentInputRow);
  
  let inputForm=document.createElement('input');
  inputForm.setAttribute("type", "text");
  inputForm.setAttribute("id", "comment_" + id);
  inputForm.setAttribute("class", "form-control mr-3");
  inputForm.setAttribute("placeholder", "Add comment");
  commentInputRow.appendChild(inputForm);

  let commentBtn=document.createElement('input');
  commentBtn.setAttribute("type", "button");
  commentBtn.setAttribute("class", "btn btn-primary");
  commentBtn.setAttribute("onClick", "submitComment(" + id + ")");
  //commentBtn.setAttribute("onClick", "getComments("+id+")");
  commentBtn.setAttribute("value", "Comment");
  commentInputRow.appendChild(commentBtn);

}

  
  
  
function AppendComment(id, comments='', user=''){
  
  let commentDisplaColumn = document.createElement('div');
  commentDisplaColumn.setAttribute("class","display-comments")
  
  let commentMainColumn = document.getElementById("comment_main_" + id).querySelector('.col-md-8')
  commentMainColumn.appendChild(commentDisplaColumn);
  
  for (comment of comments) {
    console.log('comments')
    
    let commentsCard = document.createElement('div');
    commentsCard.setAttribute("class", "card p-3 mt-2");
    commentDisplaColumn.appendChild(commentsCard);
    
    let container = document.createElement('div');
    container.setAttribute("class", "d-flex justify-content-between align-items-center");
    commentsCard.appendChild(container);
    
    let imgDiv = document.createElement('div');
    imgDiv.setAttribute("class", "user d-flex flex-row align-items-center");
    commentsCard.appendChild(imgDiv);
    
    let img= document.createElement('img');
    img.setAttribute("src", 'https://i.imgur.com/stD0Q19.jpg');
    img.setAttribute("class", 'user-img rounded-circle mr-2');
    img.setAttribute("width", '30');
    imgDiv.appendChild(img);

    let span = document.createElement('span');
    imgDiv.appendChild(span);
    
    let small = document.createElement('small');
    small.setAttribute('class', 'font-weight-bold text-primary');
    
    //################################
    small.textContent = user + ' ';//'comment.title';
    span.appendChild(small);
    

    
    let small2 = document.createElement('small');
    small2.setAttribute('class', 'font-weight-bold');
    
    //################################
    small2.textContent = comment;//'comment.value';
    
    span.appendChild(small2);   
    
  }
  
  //}  else{
  //document.getElementById("comment_main_" + id).remove();
  }
  
  /*if (reload==true) {
    Comment(id,reload_flag=false)
  }
  
  }*/
 
function readMoreOne(id){
  //console.log('Received_id:'+id);
  truncated = document.getElementById('trunc_' + id);
  toggleDisplay(truncated, true);
  //truncated.style.display='none';
  
  //console.log(main.querySelector('.truncatedDiv').textContent);
  hidden = document.getElementById('hidden_' + id);
  //hidden.style.display='block';
  toggleDisplay(hidden, true);
}


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

function CreateJoke(){
  console.log('\n\nCreating Joke\n\n');
  toggleDisplay('upload_form');
  //document.getElementById('upload_form').style.display='block';
  //window.alert('Createing Joke');
}
