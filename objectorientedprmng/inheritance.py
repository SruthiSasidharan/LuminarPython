#single inheritance
class parent:
    def phone(self):
        print("inside parents phone method")
class child(parent):
    pass
ch=child()
ch.phone()


#multilevel inheritance
class parent:
    def m1(self):
        print("inside m1")
class SubChild(parent):
    def m2(self):
        print("inside m2")
class Child(SubChild):
    def m3(self):
        print("inside m3")
ch=Child()
ch.m1()
ch.m2()
ch.m3()


#multiple inheritance
class parent:
    def m1(self):
        print("m1")
class SubChild:
    def m2(self):
        print("m2")
class Child(SubChild,parent):
    def m3(self):
        print("m3")
ch=Child()
ch.m1()
ch.m2()
ch.m3()
