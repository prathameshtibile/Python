import mysql.connector
mydb = mysql.connector.connect(host="localhost", user= "root",password="Varsha@1805")
mycursor = mydb.cursor()
mycursor.execute("show databases")
for i in mycursor:
    print(i)