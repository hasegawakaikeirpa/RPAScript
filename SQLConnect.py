def MySQLFind(user):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db'
 conn = MySQLdb.connect(host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db')
 conn.close
import MySQLdb