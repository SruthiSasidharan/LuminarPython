#lst=[3,4,2,6,7,8]
#lst1=[i-1 if i<5 else i+1 for i in lst]
#print(lst1)

lst=[[10,20],[30,40],[40,50],[50,60]]
lst1=[num for ls in lst for num in ls]
print(lst1)
