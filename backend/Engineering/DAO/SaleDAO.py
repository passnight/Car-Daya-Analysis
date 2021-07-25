import pymysql

import pymysql

# 打开数据库连接
db = pymysql.connect(host="rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com", user="root",
                     password="Password123", database="car_big_data", charset="utf8")

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

class SaleDAO:
    host = "localhost"
    user="root"
    password = "123456"
    charset = "utf8"
    database="car_big_data"

    def insert(self, carModel, carPrice, saleDatetime, saleRegion):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        # print(F"INSERT INTO `sale_info_table1sale_info_table` (`car_model`, `car_price`, `sale_datetime`, `sale_region`) VALUES ('{carModel}', '{carPrice}', '{saleDatetime}', '{saleRegion}')")
        cursor.execute(F"INSERT INTO `sale_info_table` (`car_model`, `car_price`, `sale_datetime`, `sale_region`) VALUES ('{carModel}', '{carPrice}', '{saleDatetime}', '{saleRegion}')")
        db.commit()
        cursor.close()
        db.close()
#test
# saleDAO = SaleDAO
# saleDAO.insert(saleDAO, "1", "1", "2001-10-01 00:00:00", "1")
