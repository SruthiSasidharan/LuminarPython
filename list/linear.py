arr1=[10,20,24,78,98]
arr2=[19,20,56,78,99]
pos1=0
pos2=0
while((pos1<len(arr1))&(pos2<len(arr2))):
    if arr1[pos1]==arr2[pos2]:
          print(pos1[arr1])
         pos1+=1
         pos2+=1
    elif arr1[pos1]>arr2[pos2]:
        pos2+=1
    else:
        pos1+=1