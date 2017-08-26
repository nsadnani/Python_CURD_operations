import pymysql


def connect():
	try:
		con = pymysql.connect("localhost","root","root123","mydb")
		return con
	except:
		print("connection could not be established")
		return '-1'

if __name__ == '__main__':
		con=connect()
		if con != '-1':
				con.close()

	