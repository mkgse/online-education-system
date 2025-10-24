filterSelection("all")
function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("column");
  if (c == "all") c = "";
  for (i = 0; i < x.length; i++) {
    w3RemoveClass(x[i], "show");
    if (x[i].className.indexOf(c) > -1) w3AddClass(x[i], "show");
  }
}

function w3AddClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {element.className += " " + arr2[i];}
  }
}

function w3RemoveClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);     
    }
  }
  element.className = arr1.join(" ");
}


// Add active class to the current button (highlight it)
var btnContainer = document.getElementById("myBtnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function(){
    var current = document.getElementsByClassName("active1");
    current[0].className = current[0].className.replace(" active1", "");
    this.className += " active1";
  });
}

//  Read More Js
function myFunction() {
  var dots = document.getElementById("dots");
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("myBtn1");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}

function myFunction1() {
  var dots = document.getElementById("dots1");
  var moreText = document.getElementById("more1");
  var btnText = document.getElementById("myBtn2");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}
function myFunction2() {
  var dots = document.getElementById("dots2");
  var moreText = document.getElementById("more2");
  var btnText = document.getElementById("myBtn3");

  if (dots.style.display === "none") {
    dots.style.display = "inline";
    btnText.innerHTML = "Read more"; 
    moreText.style.display = "none";
  } else {
    dots.style.display = "none";
    btnText.innerHTML = "Read less"; 
    moreText.style.display = "inline";
  }
}



// course page JS

function display(){
  var x = document.getElementById('SelectA').value;
   var sections = ['a','b','c','d','e','f','g','h','i','j',
                  'k','l','m','n','o','p','q','r','s','t','z'];

  sections.forEach(function(id) {
    var el = document.getElementById(id);
    if (el) el.style.display = "none";
  });

  // Show only the selected one(s)
  switch(x) {
    case "aa": document.getElementById('a').style.display = "block"; break;
    case "bb": document.getElementById('b').style.display = "block"; break;
    case "cc": document.getElementById('c').style.display = "block"; break;
    case "dd": document.getElementById('d').style.display = "block"; break;
    case "ee": document.getElementById('e').style.display = "block"; break;
    case "ff": document.getElementById('f').style.display = "block"; break;
    case "gg": document.getElementById('g').style.display = "block"; break;
    case "hh": document.getElementById('h').style.display = "block"; break;
    case "ii": document.getElementById('i').style.display = "block"; break;
    case "jj": document.getElementById('j').style.display = "block"; break;
    case "kk": document.getElementById('k').style.display = "block"; break;
    case "ll": document.getElementById('l').style.display = "block"; break;
    case "mm": document.getElementById('m').style.display = "block"; break;
    case "nn": document.getElementById('n').style.display = "block"; break;
    case "oo": document.getElementById('o').style.display = "block"; break;
    case "pp": document.getElementById('p').style.display = "block"; break;
    case "qq": document.getElementById('q').style.display = "block"; break;
    case "rr": document.getElementById('r').style.display = "block"; break;
    case "ss": document.getElementById('s').style.display = "block"; break;
    case "tt": document.getElementById('t').style.display = "block"; break;
    case "zz": document.getElementById('z').style.display = "block"; break;
  }
}

