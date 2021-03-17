import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="zy"
)

cursor=db.cursor()
f=open("emp","r")
for lines in f:
    data=lines.rstrip("\n").split(",")
    sql="insert into employees1 value(%s,%s,%s,%s)"
    cursor.execute(sql,data)
    db.commit()