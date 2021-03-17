class Employees:
    def __init__(self,eid,ename,desig,sal,exp):
         self.eid=eid
         self.ename=ename
         self.desig=desig
         self.sal=sal
         self.exp=exp
    def print_details(self):
         print(self.eid,self.ename,self.desig,self.sal,self.exp)

    def __str__(self):
        return self.sal
f=open("employee","r")
employees=[]
for line in f:
    eid,ename,desig,sal,exp=line.rstrip("\n").split(",")
    employees.append(Employees(eid,ename,desig,sal,exp))

develop=list(filter(lambda emp:emp.desig=="developer",employees))
name=list(map(lambda emp:emp.ename,develop))
print(name)