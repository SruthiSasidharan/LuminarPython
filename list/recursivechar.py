data="ABCAB"
lst=[]
for i in data:
    if(i in lst):
        print(i,"is first recursive")
        break
    else:
        lst.append(i)

# dict={}
# for i in data:
#     if(i in dict):
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)
