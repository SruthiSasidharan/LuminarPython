#try,except,finally

#num1=int(input("enter num1"))
#num2=int(input("enter num2"))
#try:
 #   res=num1/num2
  #  print(res)
#except:
 #   print("exception occurs")
#finally:
#print("file operation")




lst=[5,10,15,20]
pos=int(input("enter position"))
try:
    print(lst[pos])
#except:
#    print("exception occurs")
except Exception as e:
  print(e.args)             #to print wt expn occurs















