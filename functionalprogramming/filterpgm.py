#filter

#lst=[1,2,3,4,5,6,7,8,9,10]
#even=list(filter(lambda no:no%2==0,lst))
#print(even)
#num=list(filter(lambda no:no>3,lst))
#print(num)

players=[
    {"name":"sachin","matches":500,"rank":1},
    {"name":"msd","matches":200,"rank":7},
    {"name":"dravid","matches":360,"rank":12},
    {"name":"sehwag","matches":250,"rank":6}
]
matches=list(filter(lambda dict:dict["matches"]>320,players))
print(matches)



