class employee:

    company_name="ctc"

    def __init__(self,age,name): #constructor
        self.name=name
        self.age=age

    def print_person(self):
      print(self.name)
      print(self.age)
      print(employee.company_name)

emp=employee(20,"anu")
print(emp.name)
print(employee.company_name)


