num=int(input("enter a number"))
low=int(input("enter lower limit"))
upp=int(input("enter upper limit"))


for i in range(1,(upp+1)):
    if i**num in range(low,upp+1):

        print(i**num)

