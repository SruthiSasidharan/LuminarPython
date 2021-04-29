function create(){
    let user=document.querySelector("#un").value
    let task=document.querySelector("#tk").value
    let status=document.querySelector("#sts").value


    let todo={
        user:user,
        task:task,
        status:status
    }
    display(todo)
}

function display(todo){
    let html_data=" "
    html_data=`<tr><td>${todo.user}</td><td>${todo.task}</td><td>${todo.status}</td></tr>`
    document.querySelector(".dataarea").innerHTML=html_data
}