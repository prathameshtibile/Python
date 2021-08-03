import mysql.connector
mydb = mysql.connector.connect(host="localhost", user= "root",password="Varsha@1805",database="payroll_service")
mycursor = mydb.cursor()
mycursor.execute("select * from employee_payroll")
result = mycursor.fetchall()
for i in result:
    print(i)