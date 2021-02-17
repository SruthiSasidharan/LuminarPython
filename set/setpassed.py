#to find passed students
students={"vidhya","jino","neethu","aish","sruthy","ajin"}
fail={"jino","sruthy"}
diff=students.difference(fail)
print("pass",diff)

lst=[10,20,"hello",30,50]
lst[1]=60
st=set(lst)
res=list(st) #cant predict the value,coz set is not preserved
print(res[2])