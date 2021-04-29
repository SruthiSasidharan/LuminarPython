

var dbc=document.querySelector("#dbclkid")
dbc.addEventListener("dblclick",()=>{
    dbc.textContent="double clicked";
})



var clk=document.getElementById("clkid")
function clickchange()
{
    clk.textContent="Clicked"
    clk.style.color="green"
}
clk.addEventListener("click",clickchange)

var mouse=document.querySelector("#mo")
mouse.addEventListener("mouseover",()=>{
    mouse.textContent="mousemoved"
})