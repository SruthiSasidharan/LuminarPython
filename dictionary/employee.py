employee={"id":1000,"name":"anu","desig":"qa","salary":30000}
print(employee["name"])
print(employee["salary"])

if "gender" in employee:
    print("gnder exist")
else:
    employee["gender"]="female"
    print(employee)

employee["salary"]+=5000
print(employee)

for k in employee:
    print(k,",",employee[k])
print()
for k,v in employee.items():
   print(k,",",v)