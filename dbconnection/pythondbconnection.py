#install mysql connector
#1,import package
import mysql.connector
#2,establish connection
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password@123"
    #auth_plugin="mysql_native_password"
)
#cursor object
cursor=db.cursor()
sql="select version()"
cursor.execute(sql)
data=cursor.fetchone()
print(data)