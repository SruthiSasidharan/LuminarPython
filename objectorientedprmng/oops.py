class person:
    def set_person(self,age,name):
        self.name=name
        self.age=age
    def print_person(self):
        print(self.name)
        print(self.age)

obj=person()
obj.set_person("ram",23)
obj.print_person()

obj1=person()
obj1.set_person("rohit",25)
obj1.print_person()

obj2=person()
obj2.set_person("rohul",34)
obj2.print_person()
