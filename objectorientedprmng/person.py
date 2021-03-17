class person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
p1=person(27,"ram")
p2=person(26,"varun")
p3=person(24,"nikhil")
employees=[]
employees.append(p1)
employees.append(p2)
employees.append(p3)
age=[]
for emp in employees:
    age.append(emp.age)
print(max(age))
    # if emp.age>25:
    #   print(emp.name)




#highest=max(employees)
#print(highest)


