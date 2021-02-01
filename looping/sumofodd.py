num=int(input("enter limit"))
i=1
ototal=0
etotal=0
while(i<=num):
    if i%2==0:
        etotal+=i
    else:
        ototal+=i
    i+=1
print(etotal)
print(ototal)


