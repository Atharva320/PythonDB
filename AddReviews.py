#Importing module to display table

import texttable

#Importing module for connection

import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='123456789',database='bookstoredb',auth_plugin='mysql_native_password')
curs=con.cursor()

#Logic

print('Welcome to Book store!!')
print('-'*30)
print('Want to write review about any book')
choice=input('Press Y for yes and N for no : ')
choice=choice.upper()
if choice=='Y':
    Bookcode=input('Enter Book code here : ')
elif choice=='N':
    exit()
else:
    print('Enter correct option!!')
    exit()

#Error handaling

try:
    review=input("You can write review here : ")
    curs.execute("UPDATE Books SET Review='%s' WHERE Bookcode='%s'"%(review,Bookcode))
    con.commit()
    print("Review added succesfully...You can check from below")
    curs.execute("SELECT Bookname,Review FROM Books WHERE Bookcode='%s'"%(Bookcode))
    data=curs.fetchall()
    tableObj=texttable.Texttable()
    tableObj.add_rows([
    ["Book name","Review"],
    [data[0][0], data[0][1]]
    ])
    print(tableObj.draw())
    print("Thank you for using virtual Book store...")
    con.close()
except:
    print("Some error occured...please try again!!!")