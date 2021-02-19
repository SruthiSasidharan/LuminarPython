employee={
    1000:{"eid":1000,"ename":"raj","desig":"developer","salary":30000},
    1001:{"eid":1001,"ename":"ram","desig":"qa","salary":25000},
    1002:{"eid":1002,"ename":"rohit","desig":"ba","salary":35000}
}

def print_employee(**args):
    id=args["eid"]
    if id in employee:
        print(employee[id]["ename"])
        if "property" in args:
            prop=args["property"]
            print(employee[id][prop])
    else:
        print("id not exist")
print_employee(eid=1000,property="desig")