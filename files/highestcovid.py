f=open("covid19","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirmedcases=int(data[-1])                                          #string->int

    dict[state]=confirmedcases

for k,v in dict.items():
        print(k,"=>",v)
data=max(dict,key=dict.get)
print(data) #key
#print(dict[data]) value

