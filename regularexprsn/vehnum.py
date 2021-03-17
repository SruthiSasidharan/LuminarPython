from re import *

f=open("numbers","r")
numbers=[]
lst=[]
for num in f:
    numbers.append(num.rstrip("\n"))
    #numbers=num.rstrip("/n")
#print(numbers)
rule = "[K][L]\d{2}[A-Z]{2}\d{1,4}"
for word in numbers:
    match=fullmatch(rule,word)

    if match!=None:
        lst.append(word)
print(lst)


