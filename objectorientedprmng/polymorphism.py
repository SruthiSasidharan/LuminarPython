#method overloading

class maths:
    def add(self):
        print("inside no arg math method")

    def add(self,num1):
        print("inside one arg math method")

    def add(self,num1,num2):
        print("inside two arg math method")

math=maths()
math.add(11,99)           #it calls only last method(recent)



