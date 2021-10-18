
#Importing module to display table

from prettytable import PrettyTable

#Importing module for database

import mysql.connector

#Making connection wth database

con=mysql.connector.connect(host='localhost',user='root',password='123456789',database='bookstoredb',auth_plugin='mysql_native_password')
curs=con.cursor()

#Logic

print('Welcome to book store!!')
print('-'*30)
print('Want to search any book')
choice=input('Press Y for yes and N for no : ')
choice=choice.upper()

#Error handling


if choice=='Y':
    Category=input('Enter Book category here : ')
elif choice=='N':
    exit()
else:
    print('Enter correct option!!')
    exit()
    
try:    
    curs.execute("SELECT Bookname FROM Books WHERE Category='%s'"%(Category))
    print('-'*30)
    my_table = PrettyTable()
    my_table.field_names = ['Book']
    data=curs.fetchone()
    while data:
        for i in range(len(data)):
            my_table.add_row([data[i]])
        data=curs.fetchone()
    print(f'Here are the books that belong to Category : {Category}...')
    print("Thank you for using virtual Book store...")
    print(my_table)
except:
    print('Not found!!..Try again')





















