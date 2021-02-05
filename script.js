
//contact page
function test(){
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("phone").value;
    var comment = document.getElementById("comment").value;
    var error = document.getElementById("error")
    var text;

    if (name.length < 8 || name.length> 40)
    {text = "Please enter your full name";
    error.innerHTML = text;
    return false}

    if (email.length <8 || email.length> 40)
    {text = "Please enter a correct email address";
    error.innerHTML = text;
    return false}

    if (phone.length <11 || phone.length>12)
    {text = "Please enter a correct phone number";
    error.innerHTML = text;
    return false}

    if (comment.length <10|| comment.length>500)
    {text = "Please makesure your comment is less than 500 characters";
    error.innerHTML = text;
    return false}

    return true;
}


function conversion (){
//conversion

var fa = prompt("Please enter the temperature in farenheit")
var c = (5/9)*(fa -32)

document.write(c)
}

function conversion2 (){
 //conversion2
 var ce = prompt("Please enter the temperture in celsius")
 var f = ce *9 / 5 + 32
    
document.write(f)
    }