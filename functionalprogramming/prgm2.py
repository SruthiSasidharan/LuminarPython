#map
players=[
    {"name":"sachin","matches":500,"rank":1},
    {"name":"msd","matches":450,"rank":7},
    {"name":"dravid","matches":360,"rank":12},
    {"name":"sehwag","matches":480,"rank":6}
]
#names=list(map(lambda dict:dict["names"],players))
#print(names)
rank=list(map(lambda dict:dict["rank"],players))
print(rank)