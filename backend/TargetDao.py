# -*- coding = utf-8 -*-
# @Time : 2021/7/26 16:14
# @Author : ChenDuowen
# @File : test.py
# @Software : PyCharm
import json
from urllib import request
import pymysql
# class FuelDAO:
#     host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
#     user = "root"
#     password = "Password123"
#     charset = "utf8"
#     database = "car_big_data"

    # @app.route('/index1', methods=['POST'])
    # def input():
    #     inputData = request.get('inputData')
    #     data1 = query(inputData)
    #     return data1
def getmodels():
    db = pymysql.connect(host="rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com", user="root",
                             password="Password123", database="car_big_data", charset="utf8")
    cursor1 = db.cursor()
    sql1 = "SELECT car_model FROM car_power_table"
    cursor1.execute(sql1)
    results1 = cursor1.fetchall()
    jsonData = []
    #print(json.dumps(results1))
    for row in results1:
            data = {}
            data['model'] = str(row[0])
            jsonData.append(data)
    #print(json.dumps(jsonData, ensure_ascii=False))
    return json.dumps(jsonData, ensure_ascii=False)
    db.commit()
    cursor1.close()
    db.close()

def query(inputData):
    db = pymysql.connect(host="rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com", user="root",
                             password="Password123", database="car_big_data", charset="utf8")
    cursor = db.cursor()
    sql = F"SELECT avg(car_space), avg(car_decoration), avg(car_control), avg(car_confortableness), avg(car_appearance), avg(car_value_for_money) from customer_comment_table where car_model ='%s'"%(inputData)
    cursor.execute(sql)
    comment = []
    commentList = cursor.fetchall()
    for item in commentList[0]:
        comment.append(int(item * 20))
    print(json.dumps(comment, ensure_ascii=False))
    cursor.close()
    db.close()
    return json.dumps(comment, ensure_ascii=False)

if __name__ == '__main__':
    #getmodels()
    query("奔驰GLE 2021款 GLE 350 4MATIC 豪华型")
