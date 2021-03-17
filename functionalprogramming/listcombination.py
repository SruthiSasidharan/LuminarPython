lst1=[1,2,3]
lst2=[3,4,5]

lst=[(i,j) for i in lst1 for j in lst2]      #pair
print(lst)

op=[i**2 for i in lst2]     #square of lst
print(op)

common=[i for i in lst1 for j in lst2 if i==j]
print(common)






#for i in lst1:                             #pair
#    for j in lst2:
#       lst.append((i,j))
#print(lst)

