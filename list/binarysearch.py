arr=[11,10,12,13,14,15,16,17,18,19,20]
element=int(input("enter element for search"))
arr.sort()
flag=0
low=0
upp=len(arr)-1
while(upp>low):
    mid=(upp+low)//2
    if(element>arr[mid]):
        low=mid+1
    elif(element<arr[mid]):
        upp=mid-1
    elif(element==arr[mid]):
        flag=1
        break
if (flag==0):
    print("element not found")
else:
    print("element found")





