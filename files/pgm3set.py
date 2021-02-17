f1=open("word","r")
lst=[]
for lines in f1:
   word=lines.rstrip("\n").split(" ")
   for words in word:
     lst.append(words)
for words in lst:
       print(words)
