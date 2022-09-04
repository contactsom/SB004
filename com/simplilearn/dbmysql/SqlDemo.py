import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root12345",
    database="PYTHONDB"
    )
mycursor=mydb.cursor()
#mycursor.execute("CREATE database PYTHONDB")
#mycursor.execute("SHOW databases")
#mycursor.execute("CREATE TABLE Employees(id int NOT NULL PRIMARY KEY,age int NOT NULL,firstName varchar (255),lastName varchar (255))")
#sqlQuery="INSERT INTO Employees VALUES (%s, %s, %s, %s,)"
#sqlValue=(100, 21, 'JACK', 'EDITION')
#mycursor.execute("INSERT INTO Employees VALUES (100, 21, 'JACK', 'EDITION')")
mycursor.execute("select * from Employees")
print(mycursor)
for x in mycursor:
    print(x)
mydb.commit()
mycursor.close()