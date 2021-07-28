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
    sql1 = "SELECT car_model FROM car_brake_table"
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
    sql = "SELECT car_braking_efficiency, car_anti_lock, car_braking_force_distribution, car_active_braking FROM car_brake_table where car_model ='%s'"%(inputData)
    cursor.execute(sql)
    results = cursor.fetchall()
    #print(type(results))  # 返回<class 'tuple'> tuple元组类型
    #print(results)
    #print(json.dumps(results))
    res = str(json.dumps(results, ensure_ascii=False))
    data = res[1:-1]
    print(data)
    return data
    db.commit()
    cursor.close()
    db.close()

if __name__ == '__main__':
    getmodels()
    query("奔驰GLE 2021款 GLE 350 4MATIC 豪华型")
