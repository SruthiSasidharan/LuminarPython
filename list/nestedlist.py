#append-to add new values to a list
employees=[
    [100,"tom","developer",25000],
    [101,"abhi","qa",50000],
    [102,"anu","ba",23000]
]
for emp in employees:
    print(emp[1])
for emp in employees:
    if(emp[2]=="developer"):
     print(emp)

total=0
for emp in employees:
   total+=emp[3]
print(total)


sallist=[]
for emp in employees:
    sallist.append(emp[3])
print("high sal=",max(sallist))



