num1=90
num2=87
num3=43
if((num1>num2)&(num1>num3))
{
    if(num2>num3){
        console.log("num1,num2,num3");
    }

    else{
        console.log("num1,num3,num2");
    }
}
if((num2>num1)&(num2>num3))
{
    if(num1>num3){
     console.log("num2,num1,num3");
    }


     else{
        console.log("num2,num3,num1");
     }
    }

if((num3>num1)&(num3>num2)){
    if(num2>num1){
        console.log("num3,num2,num1");
    }

    else{
        console.log("num3,num1,num2");
    }
}


