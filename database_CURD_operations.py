import pymysql
import database_connectivity
import sys

conn = database_connectivity.connect()
cur_obj = conn.cursor()

def create_table(cur_obj):
	
	sql_query = 'Create table IF NOT EXISTS USER(id int(11) AUTO_INCREMENT PRIMARY KEY,Name varchar(20),User_passwd varchar(10),User_email varchar(20),User_address varchar(20))'
			
	cur_obj.execute(sql_query)
		

def add_user(cur_obj, conn):
	user_name = input('Enter user name:')
	user_passwd = input('Enter user password:')
	user_email = input('Enter User email address:')
	user_address = input('Enter users address:')
	try:

			sql_query = "Insert into USER(Name,User_passwd,User_email,User_address) values(%s,%s,%s,%s)"
			cur_obj.execute(sql_query,(user_name,user_passwd,user_email,user_address))
			conn.commit()
			print("Successfully inserted data!")
			structure(cur_obj,conn)
	except:
		    print("Error in inserting data in a table")
		    conn.rollback()



def delete_user(cur_obj,conn):
	print("Delete user by:")
	print("1.ID")
	print("2.Name")
	opt = input("Enter option:")
	if opt == '1':
		getopt = input('Enter ID:')
		mysql = "Delete from USER where id={0}".format(getopt)
	elif opt == '2':
		getopt = input('Enter name:')
		mysql = "Delete from USER where Name='{0}'".format(getopt)
	else:
		print("wrong option")
		structure(cur_obj,conn)
	try:
		cur_obj.execute(mysql)
		conn.commit()
		print("Entry deleted Successfully!")
	except:
		print("something went wrong")
		conn.rollback()
	structure(cur_obj,conn)

def modify_user(cur_obj,conn):
	getuserid = input("Enter user id:")
	mysql = "Select * from user where id={0}".format(getuserid)
	cur_obj.execute(mysql)
	data = cur_obj.fetchone()
	print("-----------------------------------------------------------")
	print("ID\tName\tPassd\tEmail\t\tAddress")
	print("%d\t%s\t%s\t%s\t%s" % (data[0],data[1],data[2],data[3],data[4]))
	print("-----------------------------------------------------------")	
	print("1.Name\n2.password\n3.Email\n4.Address")
	direct = {'1':'Name','2':'User_passwd','3':'User_email','4':'User_address'}
	getopt=input("Enter Field you want to modify:")
	getvalue=input("Enter Value:")
	myval = '{0}'.format(direct[getopt])
	mysql = "Update USER SET {0}='{1}' where id={2}".format(myval,getvalue,getuserid)
	try:
		cur_obj.execute(mysql)
		conn.commit()
		print("Entry updated Successfully!")
	except:
		print("Error in Modifying entry!")
		conn.rollback()			

	structure(cur_obj,conn)

def view_users(cur_obj,conn):
	sql_query = "select * from USER"
	cur_obj.execute(sql_query)
	results = cur_obj.fetchall()
	print("-----------------------------------------------------------")
	print("ID\tName\tPassd\tEmail\t\tAddress")
	for row in results:
		print("%d\t%s\t%s\t%s\t%s" % (row[0],row[1],row[2],row[3],row[4]))
	print("-----------------------------------------------------------")
	structure(cur_obj,conn)


def continue_program():
	structure()

def exit_program(cur_obj, conn):
	conn.close()
	exit()

def structure(cur_obj, conn):
	print('1.Add user')
	print('2.Delete user')
	print('3.Modify user')
	print('4.View user')
	print('5.Exit')
	mychoice = {
			'1': add_user,
			'2': delete_user,
			'3': modify_user,
			'4': view_users,
			'5': exit_program
	}
	choice=input("Enter your choice:")
	mychoice[choice](cur_obj, conn)


if __name__ == '__main__':
	create_table(cur_obj)
	structure(cur_obj, conn)
	conn.close()
