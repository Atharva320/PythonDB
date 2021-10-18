#Importing module for database

import mysql.connector

#Importing module to display table

from prettytable import PrettyTable

#Making connection with Database

con=mysql.connector.connect(host='localhost',user='root',password='123456789',database='bookstoredb',auth_plugin='mysql_native_password')
curs=con.cursor()

#Logic

print("Welcome to Bookstore")
print('-'*30)



while True:
    BookName=input('Enter bookname here : ')
    print('-'*30)
    Category=input('Enter books category here : ')
    print('-'*30)
    Author=input('Enter author name here : ')
    print('-'*30)
    Publication=input('Enter publication here : ')
    print('-'*30)
    Edition=input('Enter edition here : ')
    print('-'*30)
    try:
        Price=int(input('Enter price here : '))
    except:
        print("Please enter valid price")
        exit()
    print('-'*30)
    Bookcode=input('Enter book code here : ')
    my_table = PrettyTable()
    my_table.field_names = ["Book", "Category", "Author","Edition","Price"]
    my_table.add_row([BookName,Category,Author,Edition,Price])
    print(my_table)
    choice=input('Are you sure you want to add this book : ')
    choice=choice.upper()
    if choice=='Y':
        curs.execute("INSERT INTO Books(Bookcode,Bookname,Category,Author,Publication,Edition,Price) VALUES('%s','%s','%s','%s','%s','%s',%d)"%(Bookcode,BookName,Category,Author,Publication,Edition,Price))
        con.commit()
        con.close()
        print('Book added succesfully!!')
        print("Thank you for using virtual Book store...")
        exit()
    else:
        exit()
   
    









