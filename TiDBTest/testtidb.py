import pymysql

db = pymysql.connect(host='127.0.0.1', port=4000,user='zyh',password='zyh',db='test')
cursor = db.cursor()
cursor.execute('show tables')
rsp = cursor.fetchall()
cursor.close()
db.close()
