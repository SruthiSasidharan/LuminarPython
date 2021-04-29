//overriding
class parent{
    phone(){
        console.log("phone methode");
    }
}
class child extends parent{
    phone(){
        console.log("inside child");
    }
}
var ch=new child
ch.phone()