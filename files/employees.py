employee={
    1000:{"eid":1000,"ename":"raj","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"ram","desig":"qa","salary":25000},
    1002:{"eid":1002,"ename":"rohit","desig":"ba","salary":35000}
}
eid=int(input("enter eid"))
property=input("enter property")
if eid in employee:
    print(employee[eid]["ename"])
    if property in employee[eid]:
        print(employee[eid][property])
    else:
        print("invalid property")

else:
    print("invalid eid")