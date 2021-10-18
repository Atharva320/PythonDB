
#Importing module for database

import mysql.connector

#Importing module to display table

from prettytable import PrettyTable

#Making connection with database

con=mysql.connector.connect(host='localhost',user='root',password='123456789',database='bookstoredb',auth_plugin='mysql_native_password')
curs=con.cursor()

#Error handling

try:
    curs.execute('SELECT Bookname FROM Books ')
    data=curs.fetchone()
    my_table = PrettyTable()
    my_table.field_names = ['Book']
    print('Welcome to book store!!')
    while data:
        for i in range(len(data)):
            my_table.add_row([data[i]])
        data=curs.fetchone()
    print(my_table)
    print("Thank you for using virtual Book store...")
    con.close()
except:
    print("Some error occured...please try again!!!")