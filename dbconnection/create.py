import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="zy"
)

cursor=db.cursor()
sql="create table employees1(eid int,ename varchar(50),desig varchar(30),salary int)"
cursor.execute(sql)
print("table created")
