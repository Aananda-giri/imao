function AppendMeme(id, src, title) {

  let main_div = document.createElement('div');
  main_div.setAttribute('id', id);
  main_div.setAttribute("class", "text-center");
  document.body.appendChild(main_div);

  let img = document.createElement('img');
  img.setAttribute("src", src);
  img.setAttribute("class", "rounded");
  img.setAttribute("loading","lazy");
  img.setAttribute("alt", title);
  main_div.appendChild(img);
  
  let react_tab = document.createElement('div');
  react_tab.setAttribute('class', "d-flex mr-1");
  main_div.appendChild(react_tab);
  
  let love = document.createElement('div');
  love.setAttribute("class","love-icon mx-auto d-block");
  love.setAttribute("onClick","Love(" + id + ")");
  love.textContent = '♡';
  react_tab.appendChild(love);
  
  let comment = document.createElement('div');
  comment.setAttribute("class", "comment-icon mx-auto d-block");
  comment.setAttribute("onClick","Comment(" + id + ")");
  comment.textContent = "💬";//chat-emojis:💬💬🗯️💭💭👁️‍🗨️🗨️
  react_tab.appendChild(comment);
  
  /*let br=document.createElement('br');
  document.body.append(br);*/
}

function appendSpinner(){
  
  //To remove previous spinner
  console.log('spinner')
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


//########################## To display commenting box  ###############
function commentingBox (id) {
  section = document.getElementById(id);
  console.log('Commenting Box');
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
