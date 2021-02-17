expense={"jan":20000,"feb":30000,"march":40000,"april":24000,"may":35000}
print(expense["feb"])

expense["april"]-=2000
print(expense)

if "july" in expense:
    print("entry exist")
else:
    expense["july"]=52000
print(expense)