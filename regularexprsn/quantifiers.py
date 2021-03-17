#a+ -->checking for one or morethan one a (consecutive)
#a* -->a+ +zero nuber of a
#a{2}-->maximum 2 a
#a{2,3}-->minimum2 maximum3

from re import *
pattern="a{2,3}"
matcher=finditer(pattern,"aaaacaaabbbaa")
for match in matcher:
    print(match.start())
    print(match.group())