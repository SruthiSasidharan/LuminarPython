class Student
{
    constructor(name,age){
        this.name=name;                   //instance variable-to initialize
        this.age=age;
    }


    printStudent()
    {
        console.log(this.name);
        console.log(this.age);
    }
}    
// var obj=new Student
// obj.setStudent=("sruthi",21)
// obj.printStudent()

var obj=new Student("sruthi",21)
obj.printStudent()
