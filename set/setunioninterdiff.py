st1={10,11,12,13}
st2={10,11,100}

unionset=st1.union(st2)
print(unionset)

intersection=st1.intersection(st2)
print(intersection)

diff=st1.difference(st2)
print(diff)

diff2=st2.difference(st1)
print(diff2)