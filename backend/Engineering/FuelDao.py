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

    def query(inputData):
        db = pymysql.connect(host="rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com", user="root",
                             password="Password123", database="car_big_data", charset="utf8")
        cursor = db.cursor()
        sql = "SELECT car_energy_type,car_fuel_consumption_per_hundred_kilometers,car_comprehensive_fuel_consumption FROM car_fuel_table where car_model ='%s'"%(inputData)
        cursor.execute(sql)
        results = cursor.fetchall()
        print(type(results))  # 返回<class 'tuple'> tuple元组类型
        print(results)
        print(json.dumps(results))
        return json.dumps(results, ensure_ascii=False)

        db.commit()
        cursor.close()
        db.close()


if __name__ == '__main__':
    query("奔驰GLE 2021款 GLE 350 4MATIC 豪华型")
