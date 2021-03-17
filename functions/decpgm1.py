def ph(fun):
    def inner(phno):
        if len (phno)>10:
            raise Exception("invalid")
        else:
            return fun(phno)
    return inner

@ph
def val_ph(phno):
    return "valid"+phno
print(val_ph("123456789000000"))

