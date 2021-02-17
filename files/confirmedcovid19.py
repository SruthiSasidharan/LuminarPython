f=open("covid19","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]
    confirmedcases=data[-1]

    dict[state]=confirmedcases

for k,v in dict.items():
        print(k,"=>",v)



