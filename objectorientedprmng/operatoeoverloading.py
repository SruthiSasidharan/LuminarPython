class Book:
    def __init__(self,page):
        self.page=page
    def __add__(self, other):
        return Book(self.page+other.page)

    def __str__(self):
        return str(self.page)

obj=Book(80)
obj1=Book(70)
obj2=Book(50)
print(obj+obj1+obj2)







#__add__
#__sub__
#__truediv__
#__mul__

# def __sub__(self, other):
#   return self.page-other.page
# def __truediv__(self, other):
#   return self.page/other.page
#print(obj-obj1)
#print(obj/obj1)

#def __add__(self, other):
 #   return Book(self.page + other.page)  -adding 3 num

#return str(self.page) -(self.page) is a numerical value.
#converting int to str
