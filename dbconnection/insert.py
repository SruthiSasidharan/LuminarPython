import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123",
    database="zy"
)

cursor=db.cursor()
sql="insert into employees1 value(1002,'Aleena','qa',28000)"
cursor.execute(sql)
db.commit()
db.close()