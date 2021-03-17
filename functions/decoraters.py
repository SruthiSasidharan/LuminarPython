def my_div(fun):
    def inner(num1,num2):
        if num1<num2:
            num1,num2=num2,num1
        return fun(num1,num2)
    return inner

@my_div
def div_num(num1,num2):
    return(num1/num2)

print(div_num(18,6))
