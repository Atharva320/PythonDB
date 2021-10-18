
#Importing module for database

import mysql.connector


#Making connection with database

con=mysql.connector.connect(host='localhost',user='root',password='123456789',database='bookstoredb',auth_plugin='mysql_native_password')
curs=con.cursor()

#Logic

print('Welcome to Book store!!!')
print('-'*30)

#Error handling

try:
    Bookcode=input('Enter Book code here : ')
    curs.execute("SELECT * FROM Books WHERE Bookcode='%s'"%(Bookcode))
    data=curs.fetchall()
    print('-'*30)
    print('Some details...')
    print(f"Book code : {data[0][0]}")
    print(f"Book name : {data[0][1]}")
    print(f"Book category : {data[0][2]}")
    print(f"Book author : {data[0][3]}")
    print(f"Book publication : {data[0][4]}")
    print(f"Book edition : {data[0][5]}")
    print(f"Book price : {data[0][6]}")
    print('Do you want to delete this book')
    choice=input('Press Y for yes and N for no : ')
    choice=choice.upper()
    if choice=='Y':
        curs.execute("DELETE FROM Books WHERE Bookcode='%s'"%(Bookcode))
        con.commit()
        con.close()
        print('Book deleted succesfully...')
        print("Thank you for using virtual Book store...")
    else:
        exit()
except:
    print("Some error occured...please try again!!!")