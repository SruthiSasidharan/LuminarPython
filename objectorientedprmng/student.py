class student:
    def set_student_details(self,roll,name,total):
        self.roll=roll
        self.name=name
        self.total=total
    def print_student_details(self):
        print(self.roll)
        print(self.name)
        print(self.total)
obj=student()
obj.set_student_details(101,"Anu",250)
obj.print_student_details()

obj1=student()
obj1.set_student_details(102,"Anil",252)
obj1.print_student_details()

