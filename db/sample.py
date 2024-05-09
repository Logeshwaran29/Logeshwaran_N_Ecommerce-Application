import mysql.connector as sql

#connecting with db
conn=sql.connect(host='localhost',database='sample',user='root',password='log123@#')

#Checking whether db is connected or not
if conn.is_connected:
    print("Database Is Connected:")
#
# stmt=conn.cursor()
# stmt.execute()
'''
import mysql.connector as sql
conn=sql.connect(host='localhost',database='mydatabase',user='root',password='123456')#connecting with database
if conn.is_connected:#checking for successful database connection
    print("Database Is Connected:")
stmt=conn.cursor()
#stmt.execute('create table student1(name varchar(20),roll int)')
#stmt.execute('insert into student values("sumit",102)')

#print('Inserted records:')
#conn.commit()

stmt.execute('select * from student')
row = stmt.fetchall()
print(row)

'''


# import mysql.connector as sql
# class dbConnection:
#
#         def open(self):
#             try:# connecting with database
#                # print("--Database Is Connected:--")
#                 self.conn = sql.connect(host='localhost', database='shoptech', user='root',password='123456')
#                 if self.conn.is_connected():
#                    print('Database connected..')
#                 else:
#                    print('Not Connected with Database')
#                 self.stmt = self.conn.cursor()
#             except Exception as e:
#                 print(str(e)+"---Database Not Is Connected:--")
#         def close(self):
#             self.conn.close()
#             #print('Connection Close:')
# obj=dbConnection()
# obj.open()
#
#
#
#
# class Customer(dbConnection):
#         def _init_(self):
#             self.name=''
#             self.email =''
#             self.phone=''
#             print(self.name,self.email,self.name)
#
#         def create(self):
#             create_str='''create  table  if not exists customer(cust_id int primary key auto_increment,
#             name varchar(50),
#             email varchar(50),
#             phone varchar(50))'''
#             self.open()
#             self.stmt.execute(create_str)
#             self.stmt.close()
#             print('Table created successfully------:')
#
#         def addCustomer(self):
#             self.name = input('Enter Name :')
#             self.email = input('Enter Name email:')
#             self.phone = input('Enter phone :')
#             print(self.name, self.email, self.name)
#             data=[(self.name,self.email,self.phone)]
#             insert_str='''insert into customer(name,email,phone) values(%s,%s,%s)'''
#             self.open()
#             self.stmt.executemany(insert_str,data)
#             self.conn.commit()
#             print('Records Inserted Successfully..')
#             self.close()
#
#         def select(self):
#             self.open()
#             select_str='''select * from customer'''
#             self.stmt.execute(select_str)
#             recods=self.stmt.fetchall()
#             print('')
#             print('Records In Customer Table_')
#             for i in recods:
#                 print(i)
#             self.close()
#
#
#         def update(self):
#             self.select()
#             Id=int(input('Input Emp ID to be Updated'))
#             self.name = input('Enter Name :')
#             self.email = input('Enter Name email:')
#             self.phone = input('Enter phone :')
#             update_str='update customer set name=%s,email=%s,phone=%s where cust_id=%s'
#             self.open()
#             data=[(self.name, self.email, self.phone,Id)]
#             self.stmt.executemany(update_str,data)
#             self.conn.commit()
#             print(update_str,data)
#             print('Records updated Successfully..')
#         def delete(self):
#             Id=int(input('Enter the Eid to be deleted:'))
#             delete_str=f'delete from customer where cust_id={Id}'
#             #data=[(Id,)]
#             self.open()
#             #self.stmt.executemany(delete_str,data)
#             self.stmt.execute(delete_str)
#             self.conn.commit()
#             print('Records Deleted Successfully..')
#
#
#
#
# Myobject=Customer()
# #Myobject.addCustomer()
# #Myobject.update()
# Myobject.delete()
#     #Myobject.select()
#     #Myobject.create()