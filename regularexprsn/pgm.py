from re import *
pattern="\W"
source="abaA@_678Hg"
matcher=finditer(pattern,source)
cnt=0
for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print(cnt)



