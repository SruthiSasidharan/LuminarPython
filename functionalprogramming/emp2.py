class Employee:
    def __init__(self,eid,ename,desig,sal,exp):
         self.eid=eid
         self.ename=ename
         self.desig=desig
         self.sal=int(sal)
         self.exp=int(exp)
    def print_details(self):
         print(self.eid,self.ename,self.desig,self.sal,self.exp)

    def __str__(self):
        return self.ename
f=open("employee","r")
employees=[]
for line in f:
    eid,ename,desig,sal,exp=line.rstrip("\n").split(",")
    employees.append(Employee(eid,ename,desig,sal,exp))
exp=list(filter(lambda emp:emp.exp>2,employees))
for emp in exp:
  print(emp)
