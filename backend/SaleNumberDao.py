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
    sql1 = "SELECT DISTINCT car_model FROM sale_info"
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

def query(model, time1, time2):
    db = pymysql.connect(host="rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com", user="root",
                             password="Password123", database="car_big_data", charset="utf8")
    cursor = db.cursor()
    sql = "SELECT sale_number FROM sale_info where sale_datetime >= '{time1}' and time2 car_model ='{model}'"
    cursor.execute(F"SELECT sale_number FROM sale_info where sale_datetime >= '{time1}' and sale_datetime <= '{time2}' and car_model ='{model}'")
    results = cursor.fetchall()
    #print(type(results))  # 返回<class 'tuple'> tuple元组类型
    #print(results)
    #print(json.dumps(results))
    #res = str(json.dumps(results, ensure_ascii=False))  # 默认输出格式为  [[],[],[],[]]
    #res = res[2:-2]                                     # 需去掉最外层的 [[]]
    #data = res.split('], [')                            # 去掉(], [) --> ['', '', '', ''] 
    #data = ', '.join(data)                              # 去掉('')并在最外层加[]

    datalist = []
    for s in results:
        datalist.append(s[0]/10000)
    #print(datalist)                           
    return datalist
    db.commit()
    cursor.close()
    db.close()

def getTime(time1, time2):
    db = pymysql.connect(host="rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com", user="root",
                             password="Password123", database="car_big_data", charset="utf8")
    cursor = db.cursor()
    cursor.execute(F"SELECT DISTINCT sale_datetime FROM sale_info where sale_datetime >= '{time1}' and sale_datetime <= '{time2}'")
    results = cursor.fetchall()

    timelist = []
    for s in results:
        timelist.append(s[0].__format__('%Y年%m月'))

    #print(timelist)                           
    return timelist
    db.commit()
    cursor.close()
    db.close()   

if __name__ == '__main__':
    #getmodels()
    query("五菱宏光","2015-01-01 00:00:00","2017-01-01 00:00:00")
