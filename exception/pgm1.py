num=int(input("enter any number"))
try:
    if num<0:
     raise Exception("invalid")
except Exception as e:
    print(e.args)
