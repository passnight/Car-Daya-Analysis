# -*- coding = utf-8 -*-
# @Time : 2021/7/23 10:57
# @Author : ChenDuowen
# @File : xlsMake.py
# @Software : PyCharm


import json
import os
import re
import xlwt
'''
第七步读取数据文件，生成excel
'''
if __name__ == "__main__":
    rootPath = "C:\\Users\\90643\\Desktop\\autoHome\\newJson\\"
    workbook = xlwt.Workbook(encoding = 'ascii')#创建一个文件
    worksheet = workbook.add_sheet('汽车之家')#创建一个表
    files = os.listdir(rootPath)
    startRow = 0
    isFlag = True #默认记录表头
    for file in files:
        list = []
        carItem = {}
        print("fileName=="+file.title())
        text = ""
        for fi in open(rootPath+file,'r',encoding="utf-8"):
            text = text+fi
        # else:
            # print("文件内容=="+text)
        #解析基本参数配置参数，颜色三种参数，其他参数
        #keyLink = "var KeyLink = (.*?);"
        config = "var config = (.*?);"
        option = "var option = (.*?);var"
        bag = "var bag = (.*?);"

        #keyLinkRe = re.findall(keyLink,text)
        configRe = re.findall(config,text)
        optionRe = re.findall(option,text)
        bagRe = re.findall(bag,text)
        for a in configRe:
            config = a
        print("++++++++++++++++++++++\n")
        for b in optionRe:
            option = b
            print("---------------------\n")
        for c in bagRe:
            bag = c
        # for a in keyLinkRe:
        #     keyLink = a
        # print("++++++++++++++++++++++\n")
        # for b in configRe:
        #     config = b
        #     print("---------------------\n")
        # for c in optionRe:
        #     option = c
        #     print("*********************\n")
        # for d in bagRe:
        #     bag = d
        # print(config)
        # print(option)
        # print(bag)

        # print(bag)
        try:
            #keyLink = json.loads(keyLink)
            config = json.loads(config)
            option = json.loads(option)
            bag = json.loads(bag)
            # print(config)
            # print(option)
            # print(bag)
            path = "C:\\Users\\90643\\Desktop\\autoHome\\autoHome.xls"

            configItem = config['result']['paramtypeitems'][0]['paramitems']
            optionItem = option['result']['configtypeitems'][0]['configitems']
        except Exception as e:
            f =  open("C:\\Users\\90643\\Desktop\\autoHome\\异常数据\\exception.txt","a",encoding="utf-8")
            f.write(file.title()+"\n")
            continue

        #解析基本参数
        for car in configItem:
            carItem[car['name']]=[]
            for ca in car['valueitems']:
                carItem[car['name']].append(ca['value'])
        # print(carItem)
        #解析配置参数
        for car in optionItem:
            carItem[car['name']]=[]
            for ca in car['valueitems']:
                carItem[car['name']].append(ca['value'])

        if isFlag:
            co1s = 0

            for co in carItem:
                co1s = co1s +1
                worksheet.write(startRow,co1s,co)
            else:
                startRow = startRow+1
                isFlag = False

        #计算起止行号
        endRowNum = startRow + len(carItem['车型名称']) #车辆款式记录数
        for row in range(startRow,endRowNum):
            print(row)
            colNum = 0
            for col in carItem:

                colNum = colNum +1
                print(str(carItem[col][row-startRow]),end='|')
                worksheet.write(row,colNum,str(carItem[col][row-startRow]))

        else:
            startRow  = endRowNum
    workbook.save('C:\\Users\\90643\\Desktop\\autoHome\\Mybook.xls')