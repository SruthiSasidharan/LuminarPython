#num1=int(input("enter num1"))
#num2=int(input("enter num2"))
#num3=int(input("enter num3"))
#if(num1>num2>=num3):
 #   print("num1 is largest")
#elif(num1<=num2<num3):
 #print("num3 is largest")
#elif(num1<=num2>=num3):
 #   print("num2 is largest")
  #  pass
num1=int(input())
num2=int(input())
num3=int(input())
if(num1>num2)&(num1>num3):
    print(num1)
elif(num2>num1)&(num2>num3):
    print(num2)
elif(num3>num1)&(num3>num1):
    print(num3)
elif(num1==num2)&(num1==num3):
    print("3 numbers are equel")