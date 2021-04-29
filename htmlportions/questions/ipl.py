iplpoints=[
    {"team":"csk","mp":6,"won":5,"los":1,"pts":10},
    {"team":"srh","mp":6,"won":1,"los":5,"pts":2},
    {"team":"rcb","mp":6,"won":5,"los":1,"pts":10},
    {"team":"csk","mp":6,"won":5,"los":1,"pts":10},
    {"team":"rr","mp":5,"won":2,"los":3,"pts":4},
    {"team":"dc","mp":6,"won":4,"los":2,"pts":8},
    {"team":"pbks","mp":6,"won":2,"los":4,"pts":4}

]

#1)number of participent
total=0
for point in iplpoints:
    total+=point["mp"]
print(total)

#2)name in uppercase
point=list(map(lambda dict:dict["team"].upper(),iplpoints))
print(point)

#3)team details having highest point
highestpoint=max(list(map(lambda dict:dict["pts"],iplpoints)))
print(highestpoint)
point=list(filter(lambda dict:dict["pts"]==highestpoint,iplpoints))
print(point)

#4)team details having lowest point
lowestpoint=min(list(map(lambda dict:dict["pts"],iplpoints)))
print(lowestpoint)
pt=list(filter(lambda dict:dict["pts"]==lowestpoint,iplpoints))
print(pt)

#5sort according with points
for point in iplpoints:

   lst=sorted(list(map(lambda dict:dict["pts"],iplpoints)))

print(lst)

