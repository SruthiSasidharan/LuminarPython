//method overloading
class calculation{
    add(){
        console.log("single argument");

    }
    add(num1,num2){
        console.log("two argument");
    }
}
var obj=new calculation
//obj.add()            //calls recent method
obj.add(10,20)