#re-pattern matching

from re import *
pattern="ab"               #both ab
source="abababbbbbabbabbab"
matcher=finditer(pattern,source)
cnt=0
for match in matcher:
    print(match.start())
    print(match.group())
    cnt+=1
print(cnt)
