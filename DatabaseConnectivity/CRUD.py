from tabulate import tabulate
import mysql.connector


mydb = mysql.connector.connect(host="localhost", user= "root",password="Varsha@1805",database="payroll_service")
if mydb:
    print('Connection established')
else:
    print('Connection not established ')

def getdata(mydb):
    print("read")
    cursor = mydb.cursor();
    cursor.execute("select* from employee_CRUD")
    for row in cursor:
        print(f'{row}')
getdata(mydb);


def insert(Id, Name, Address):
    mycursor = mydb.cursor()  # Connecting Python and Sql
    sql = "Insert into employee_CRUD (id,name,address) values (%s,%s,%s)"
    users = (Id, Name, Address)
    mycursor.execute(sql, users)
    mydb.commit()  # It will insert automatically and saves
    print("Data Insert Success")

def update(Name, Address, Id):
    mycursor = mydb.cursor()  # Connecting Python and Sql
    sql = "update  employee_CRUD set name=%s,address=%s where id=%s"
    users = (Name, Address, Id)
    mycursor.execute(sql, users)
    mydb.commit()  # It will Updates automatically and saves
    print("Data Update Success")

def select():
    mycursor = mydb.cursor()  # Connecting Python and Sql
    sql = "select id , name , address from employee_CRUD"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    print(tabulate(result, headers=["ID", "name", "address"]))

def delete(Id):
    mycursor = mydb.cursor()  # Connecting Python and Sql
    sql = "delete from employee_CRUD where id=%s"
    users = (Id,)
    mycursor.execute(sql, users)
    mydb.commit()  # It will Updates automatically and saves
    print("Data Delete Success")


while True:
    print("****************************************************************")
    print("1. Insert Data")
    print("2. Update Data")
    print("3. Show Data")
    print("4. Delete Data")
    print("****************************************************************")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        Id = input("Enter the Id : ")
        Name = input("Enter the Name : ")
        Address = input("Enter the Address : ")
        insert(Id,Name, Address)

    elif choice == 2:
        Id = input("Enter the id : ")
        Name = input("Enter the name : ")
        Address = input("Enter the Address : ")
        update(Name, Address, Id)

    elif choice == 3:
        select()

    elif choice == 4:
        Id = input("Enter the Id to be Deleted :")
        delete(Id)

    else:
        print("Invalid input...!Please try again")


