num=int(input("enter the num"))
pattern=""
total=0
for i in range(1,(num+1)):
    pattern=str(num)*i
    total+=int(pattern)
print(total)
