import sqlite3
## connect to sqlite 
connection=sqlite3.connect("student.db")
##Create a cursor object to insert record,create table ,retrieve record
cursor=connection.cursor()
##create a table
cursor.execute('''DROP TABLE IF EXISTS STUDENT''')
table_info= """ Create table STUDENT(Name VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT); """
cursor.execute(table_info)
##Insert some more records
cursor.execute('''INSERT INTO STUDENT VALUES('Krish','Data Science','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Sudhanshu','Data Science','B',100)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Darius','Data Science','A',86 )''')
cursor.execute('''INSERT INTO STUDENT VALUES('Vikash','Devops','A',50)''')
cursor.execute('''INSERT INTO STUDENT VALUES('Rohit','Devops','A',35)''')
##Display all the records
print("The insserted records are:")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
##Close the connection
connection.commit()
connection.close()