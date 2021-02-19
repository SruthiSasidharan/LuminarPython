def add(*args):
  total=0
  for num in args:
      total+=num                    #*args-tuple
  print(total)                      #**args-dict

add(20,90,80,25,60)

def print_emp_data(**args):
    for k,v in args.items():           #print(args)   -> {datas}
        print(k,v)
print_emp_data(eid=100,job="kottayam",resid="mnply")

