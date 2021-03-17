#from re import *

#rule="[a-kA-K][369][a-zA-Z0-9]*"
#variablename=input("enter variable name")
#match=fullmatch(rule,variablename)
#if match!=None:
#    print("valid variable name")
#else:
#    print("invalid variable name")
#rule="[K][L][\d]{2}[A-Z]{2}[\d]{1,4}"
#rule='\w{1,64}@gmail.com'







from re import*
rule='\d{10}'

variablename=input("enter variable name")
match=fullmatch(rule,variablename)

if match!=None:
 print("valid variable name")
else:
 print("invalid variable name")

