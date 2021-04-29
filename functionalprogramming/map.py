#map

lst=[2,4,6,8,10]
#sq=lambda num:num**2
#square=list(map(sq,lst))
square=list(map(lambda num:num**2,lst))
print(square)


names=["ram","raju","ravi"]
u=list(map(lambda name:name.upper(),names))
print(u)


