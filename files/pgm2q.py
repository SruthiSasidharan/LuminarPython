f1=open("team","r")
f2=open("drop","r")
st1=set()
for lines in f1:
     st1.add(lines.rstrip("\n"))
st2=set()
for lines in f2:
    st2.add(lines.rstrip("\n"))
qu=st1-st2
print(qu)

