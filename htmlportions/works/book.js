function create(){
  let book= document.querySelector("#bn").value
   let author=document.querySelector("#ar").value
   let category=document.querySelector("#ct").value
   let price=document.querySelector("#pr").value

    let val={
        book:book,
        author:author,
        category:category,
        price:price
    }
    display(val)
}
function display(val){
    let html_data=" "
    html_data=`<tr><td>${val.book}</td><td>${val.author}</td><td>${val.category}</td><td>${val.price}</td></tr>`
    document.querySelector(".dis").innerHTML=html_data
}
