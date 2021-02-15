text="hello hai hello hai hello"
words=text.split(" ")
dict={}

for word  in words:
    if word not in dict:
        dict[word]=1
    else:
        dict[word]+=1
print(sorted(dict,key=dict.get))   #reverse=true(decending order)




#print(max(dict,key=dict.get))         #.get[to get values]


#print(dict[word])

      #  dict[word]+=1
#print(dict)

#sort  sort(dict,key=dict.get)


dict={"this":3,"an":4,"yard":9}
data=sorted(dict,key=dict.get,reverse=True)
print(data)