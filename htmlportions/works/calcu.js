function enternum(num){
    var inp=document.querySelector("#no")
    var inpt=inp.value
    inp.value=inpt+num
 
 }
 
 function result(){
     let inp=document.querySelector("#no").value
     let res=eval(inp)
     document.querySelector("#no").value=res
 }
 function clr(){
     document.querySelector("#no").value=" "
 }
 function bck()
 {
     let data=document.querySelector("#no").value
     data=data.slice(0,-1)
     document.querySelector("#no").value=data
}