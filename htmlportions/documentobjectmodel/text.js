

function eliAge(){
    var one=document.querySelector("button")
    one.addEventListener("click",()=>{
        var nme=document.querySelector("#name").value;
        var age=document.querySelector("#age").value
  
    
    if(age>18)
    {
        window.alert("Eligible")
    }
    else{
        window.alert("not eligible")
    }


})
}
