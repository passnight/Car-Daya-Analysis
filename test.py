import pymysql
host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
user = "root"
password = "Password123"
charset = "utf8"
database = "car_big_data"

#update purchasing_purpose_table set sale_price = 133105.5735 where car_model = '星瑞'
db = pymysql.connect(host=host, user=user,
                        password=password, database=database, charset=charset)
cursor = db.cursor()
cursor.execute(
        F"select distinct car_model from basic_sale_info_table")
modelList = cursor.fetchall()
for model in modelList:
    cursor.execute(
        F"select avg(sale_price) from basic_sale_info_table where car_model = '{model[0]}'")
    averagePrice = float((cursor.fetchall())[0][0])
    cursor.execute(F"update purchasing_purpose_table set sale_price = {averagePrice} where car_model = '{model[0]}'")
    db.commit()
# comments = []
# for item in datas:
#     comments.append({"carType": item[0], "price": "1万以上", "purchaseTarget": item[1]})
# cursor.close()
# db.close()