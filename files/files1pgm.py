f=open("demo","r")
lst=[]
for lines in f:
    print(lines)
    lst.append(lines.rstrip("\n"))           #list
print(lst)                                   #.rstrip/lstrip (to remove)




