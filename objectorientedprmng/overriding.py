#overriding
class parent:
    def phone(self):
        print("have nokia phone")

class child(parent):
    def phone(self):
        print("have iphone")
ch=child()
ch.phone()


class person:                          #class person(object):
    def __init__(self,age,name):
        self.age=age
        self.name=name
    def __str__(self):                          #overriding
        return self.name+str(self.age)          #coverting int -> str
p=person(25,"Arun")
print(p)




#class object:
#def__str__(self)
#return("main object at" xxxx)