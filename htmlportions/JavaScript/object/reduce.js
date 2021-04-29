//reduce single value
//2 parameters

var arr=[10,12,14,8]
// var sum=arr.reduce((n1,n2)=>n1+n2)
// console.log(sum);

var min=arr.reduce((n1,n2)=>n1<n2?n1:n2)
console.log(min);

var max=arr.reduce((n1,n2)=>n1>n2?n1:n2)
console.log(max);
