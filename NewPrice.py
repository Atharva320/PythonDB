import texttable

#Importing module for database

import mysql.connector

#Making connection with database

con=mysql.connector.connect(host='localhost',user='root',password='123456789',database='bookstoredb',auth_plugin='mysql_native_password')
curs=con.cursor()

#Logic

print('Welcome to book store!!!')
print('-'*30)
print('Want to update price of any book')
choice=input('Press Y for yes and N for no : ')
choice=choice.upper()

if choice=='Y':
    Bookcode=input('Enter Book code here : ')
    curs.execute("SELECT * FROM Books WHERE Bookcode='%s'"%(Bookcode))
    data=curs.fetchone()
    if data:
        price=int(input('Enter new price here : '))
    else:
        print('Book does not exist!!')
        exit()
elif choice=='N':
    exit()
else:
    print('Enter correct option!!')
    exit()

#Error handling


try:
    curs.execute("SELECT Bookcode,Bookname,Price FROM Books WHERE Bookcode='%s'"%(Bookcode))
    dat1=curs.fetchall()
    curs.execute("UPDATE Books SET Price=%d WHERE Bookcode='%s'"%(price,Bookcode))
    con.commit()

    print('Price updation succesfull...')
    curs.execute("SELECT Bookcode,Bookname,Price FROM Books WHERE Bookcode='%s'"%(Bookcode))
    data=curs.fetchall()
    print('-'*30)
    print('Before updation.....')
    tableObj=texttable.Texttable()
    tableObj.add_rows([
    ["Book code","Book name","Book price"],
    [dat1[0][0], dat1[0][1], dat1[0][2]]
    ])
    print(tableObj.draw())
    print('-'*30)
    print('After updation.....')
    tableObj=texttable.Texttable()
    tableObj.add_rows([
    ["Book code","Book name","Book price"],
    [data[0][0], data[0][1], data[0][2]]
    ])
    print(tableObj.draw())
    print("Thank you for using virtual Book store...")
    con.close()  
except:
    print("Some error occured...please try again!!!")









