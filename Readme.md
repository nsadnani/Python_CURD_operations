# Python_CURD_operations
Create,Update,Retrieve,Display d operations with python  

## Description:

This project contains python menu driven program which can perform below operations:  
1.Add  
2.Update  
3)Retrieve  
4)Display  

### Requirements:   
It requires python3,Mysql and python modules like:PyMySql installed.  
Create database name mydb,user root with password 'root123'.Copy this project on your machine and execute database_CURD_OPERATIONS.  

#### Usage:    
Below is the syntax to run:  
C:\Users\python_db_examples>python database_CURD_operations.py  

####Output:  
C:\Users\sadnan\Desktop\python_db_examples>python database_CURD_operations.py  
C:\Python34\lib\site-packages\pymysql\cursors.py:166: Warning: (1050, "Table 'user' already exists")  
  result = self._query(query)  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:4  
-----------------------------------------------------------  
ID      Name    Passd   Email           Address  
-----------------------------------------------------------  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:1  
Enter user name:Rahul  
Enter user password:root123  
Enter User email address:rahul@gmail.com  
Enter users address:Al rigga,Dubai  
Successfully inserted data!  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:1  
Enter user name:Niki  
Enter user password:abc123  
Enter User email address:niki@gmail.com  
Enter users address:baner,Pune  
Successfully inserted data!  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:1  
Enter user name:Dugu  
Enter user password:xyz123  
Enter User email address:navi mumbai  
Enter users address:navi mumbai  
Successfully inserted data!  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:4  
-----------------------------------------------------------  
ID      Name    Passd   Email           Address  
1       Rahul   root123 rahul@gmail.com Al rigga,Dubai  
2       Niki    abc123  niki@gmail.com  baner,Pune  
3       Dugu    xyz123  navi mumbai     navi mumbai  
-----------------------------------------------------------  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:3  
Enter user id:3  
-----------------------------------------------------------  
ID      Name    Passd   Email           Address  
3       Dugu    xyz123  navi mumbai     navi mumbai  
-----------------------------------------------------------  
1.Name  
2.password  
3.Email  
4.Address  
Enter Field you want to modify:3  
Enter Value:Dugu@gmail.com  
Entry updated Successfully!  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:4  
-----------------------------------------------------------  
ID      Name    Passd   Email           Address  
1       Rahul   root123 rahul@gmail.com Al rigga,Dubai  
2       Niki    abc123  niki@gmail.com  baner,Pune  
3       Dugu    xyz123  Dugu@gmail.com  navi mumbai  
-----------------------------------------------------------  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:1  
Enter user name:Gita  
Enter user password:abc432  
Enter User email address:  
Enter users address:delhi  
Successfully inserted data!  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:4  
-----------------------------------------------------------  
ID      Name    Passd   Email           Address  
1       Rahul   root123 rahul@gmail.com Al rigga,Dubai  
2       Niki    abc123  niki@gmail.com  baner,Pune  
3       Dugu    xyz123  Dugu@gmail.com  navi mumbai  
4       Gita    abc432                  delhi  
-----------------------------------------------------------  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:2  
Delete user by:  
1.ID  
2.Name  
Enter option:1  
Enter ID:4  
Entry deleted Successfully!  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:4  
-----------------------------------------------------------  
ID      Name    Passd   Email           Address  
1       Rahul   root123 rahul@gmail.com Al rigga,Dubai  
2       Niki    abc123  niki@gmail.com  baner,Pune  
3       Dugu    xyz123  Dugu@gmail.com  navi mumbai  
-----------------------------------------------------------  
1.Add user  
2.Delete user  
3.Modify user  
4.View user  
5.Exit  
Enter your choice:5  

C:\Users\sadnan\Desktop\python_db_examples>  
