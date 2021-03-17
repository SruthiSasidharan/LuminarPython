class employee:
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

f=open("/home/sruthy/PycharmProjects/LumiarPython/objectorientedprmng/employee","r")
employees=[]
for line in f:
    eid,ename,desig,sal,exp=line.rstrip("\n").split(",")
    employees.append(employee(eid,ename,desig,sal,exp))
ename=list(map(lambda emp:emp.ename,employees))
print(ename)
