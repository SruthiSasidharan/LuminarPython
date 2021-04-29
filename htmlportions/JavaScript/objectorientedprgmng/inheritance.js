//inheritance

// class parent{
//     phone()
//     {
//         console.log("have nokia");
//     }
// }
// class child extends parent{

// }
// var ch=new child()
// ch.phone()


//multilevel

class parent{
    m1(){
        console.log("have nokia");
    }
}
class SubChild extends parent{
    m2(){
        console.log("m2");
        }
}
class Child extends SubChild{
    m3(){
        console.log("m3");
    }
}

var ch=new Child()
ch.m3()
ch.m2()
ch.m1()