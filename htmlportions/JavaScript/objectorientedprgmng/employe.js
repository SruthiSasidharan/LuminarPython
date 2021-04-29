class employee
{
    constructor(eid,name,desig,salary)
    {
    this.eid=eid;
    this.name=name;
    this.desig=desig;
    this.salary=salary;
    }

    printemployee()
    {
        console.log(this.eid);
        console.log(this.name);
        console.log(this.desig);
        console.log(this.salary);

    }
}
var emp=new employee(101,"Anu","qa",25000)
var emp1=new employee(102,"ali","developer",28000)
var emp2=new employee(103,"Abhi","mrkt",24000)
//emp.printemployee()
var employees=[]
employees.push(emp)                                  
employees.push(emp1)
employees.push(emp2)

enames=employees.map(emp=>emp.name)
console.log(enames);

var edesig=employees.filter(emp=>emp.desig=="developer")
console.log(edesig);


var maxsal=employees.reduce((emp1,emp2)=>emp1.salary>emp2.salary?emp1:emp2)
console.log(maxsal);

var sal=employees.sort((emp,emp1)=>emp.salary-emp1.salary)
console.log(sal);


//forEach -
var arr=[10,20,30]
arr.forEach(arr=>console.log(arr))                 //for loop -->
//documentobmodel