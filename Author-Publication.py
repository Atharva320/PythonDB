#Importing module to display table

import texttable

#Importing module for database

import mysql.connector

#Making connection with database

con=mysql.connector.connect(host='localhost',user='root',password='123456789',database='bookstoredb',auth_plugin='mysql_native_password')
curs=con.cursor()

#Logic

print('Welcome to Book store!!')

#Error handling

try:
    author=input("Enter Book's Author name here : ")
    publication=input("Enter Book's publication here : ")
    curs.execute("SELECT Bookname,Author,Publication FROM Books WHERE Author='%s' and Publication='%s'"%(author,publication))
    data=curs.fetchall()
    tableObj=texttable.Texttable()
    tableObj.add_rows([
    ["Book name","Author","Publication"],
    [data[0][0], data[0][1], data[0][2]]
    ])
    print(tableObj.draw())
    print("Thank you for using virtual Book store...")
    con.close()
except:
    print("Some error occured...please try again!!!")
