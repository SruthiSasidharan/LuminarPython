var i=10
var j=1
function fact(num)
{
    fac=1
    for(let i=num;i>=1;i--){
        fac=fac*i
    }
    return fac
}
num=fact(4)
console.log(num);