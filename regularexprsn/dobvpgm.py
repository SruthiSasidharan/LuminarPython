from re import*
f=open("dob","r")

date=[]
lst=[]
for line in f:
 #print(line)
 date.append(line.rstrip("\n"))
#print(date)

rule='\d{2}/\d{2}/\d{4}'
for num in date:
    match=fullmatch(rule,num)

    if match!=None:
         lst.append(num)
print(lst)