import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="123456", database="car_big_data", charset="utf8")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
# `car_big_data`.
sql = "select * from `test_table`"
try:
   # 执行sql语句
   cursor.execute(sql)
   results = cursor.fetchall()
   print(results)
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()
