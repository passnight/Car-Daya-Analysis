
from io import BytesIO, StringIO
from bs4 import builder
import chardet
import os
import time
import codecs
import csv
import bs4
import re
import requests
import pymysql
import json


class SaleDAO:
    host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
    user = "root"
    password = "Password123"
    charset = "utf8"
    database = "car_big_data"

    def insert(self, carModel, saleDatetime, saleRegion):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"INSERT INTO `basic_sale_info_table` (`car_model`, `sale_datetime`, `sale_region`) VALUES ('{carModel}', '{saleDatetime}', '{saleRegion}')")
        db.commit()
        cursor.close()
        db.close()



class CustomerCommentDAO:
    host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
    user = "root"
    password = "Password123"
    charset = "utf8"
    database = "car_big_data"

    def insert(self, carModel, carSpace, carDecoration, carControl, carConfortableness, carAppearance, carValueForMoney):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"INSERT INTO `customer_comment_table` (`car_model`, `car_space`, `car_decoration`, `car_control`, `car_confortableness`, `car_appearance`, `car_value_for_money`) VALUES('{carModel}', '{carSpace}', '{carDecoration}', '{carControl}', '{carConfortableness}', '{carAppearance}', '{carValueForMoney}')")
        db.commit()
        cursor.close()
        db.close()



class PurchasingPurposeDAO:
    host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
    user = "root"
    password = "Password123"
    charset = "utf8"
    database = "car_big_data"

    def insert(self, carModel, purchasePurpose, comment):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"INSERT INTO `purchasing_purpose_table` (`car_model`, `purchase_purpose`, `comment`) VALUES ('{carModel}', '{purchasePurpose}', '{comment}');")
        db.commit()
        cursor.close()
        db.close()

purchasingPurposeDAO = PurchasingPurposeDAO()
saleDAO = SaleDAO()
customerCommentDAO = CustomerCommentDAO()
class TargetSpider:
    carCount = 0
    pageCount = 0
    itemCount = 0
    data = {"车型": "", "配置": "", "空间": 0, "内饰": 0, "操控": 0,
            "舒适性": 0, "外观": 0, "性价比": 0, "购买时间": "", "购买地点":"", "购车目的":[],"用户评价":""}
    dataList = []
    soupFile = "soup.html"
    headers = {
        "Host": "k.autohome.com.cn",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    def trim(self, string):
        string = string.replace(" ", "")
        string = string.replace("\n", "")
        return string

    def trimComment(self, string):
        end = len(string)-1
        begin = end
        for i in range(end,-1,-1):
            if string[i] == "【":
                begin = i
                break
        string = string[0:begin]
        if string == "":
            return "无评价"
        return string

    def writeToCSV(self):
        outputFile = open("backend/temp/output.csv", "w")
        writer = csv.writer(outputFile)
        writer.writerow(("车型", "配置", "空间", "内饰", "操控",
                         "舒适性", "外观", "性价比", "购买时间", "购买地点"))

    def readContent(self, content):
        filename = "backend/temp/url.html"
        file = open(filename, "wb", buffering=1024*1024*4)
        file.write(content)
        file.close()
        html = open(filename, "r").read()
        return html
        # print(content)
    def logItem(self):
        self.itemCount = self.itemCount + 1
        print(F"item {self.itemCount} is finished")

    def getCar(self, webIndex, pageIndex):
        url = F"https://k.autohome.com.cn/{webIndex}/index_{pageIndex}.html#dataList"
        session = requests.Session()
        response = session.get(
            url, headers=self.headers)
        if not response:
            print("failed")
            return
        html = self.readContent(response.content)
        soup = bs4.BeautifulSoup(html)
        comments = soup.find_all(class_="mouthcon-cont fn-clear")
        for comment in comments:
            rank = bs4.BeautifulSoup(
                comment.prettify()).find_all(class_="choose-dl")
            data = {"车型": "", "配置": "", "空间": 0, "内饰": 0, "操控": 0,
                    "舒适性": 0, "外观": 0, "性价比": 0, "购买时间": "", "购买地点": "", "购车目的": [], "用户评价": ""}
            try:
                rank[14]
            except:
                print("one line not complete")
                continue
        # 车型爬取
            data["车型"] = self.trim(rank[0].find("a", target="_blank").text)
            self.logItem()
            data["配置"] = self.trim(rank[0].find("span", class_="font-arial").text)
            self.logItem()
        # 空间爬取
            data["空间"] = self.trim(rank[6].find(
                "span", class_="font-arial c333").text)
            self.logItem()
        # 内饰
            data["内饰"] = self.trim(rank[12].find(
                "span", class_="font-arial c333").text)
            self.logItem()
        # 操控
            data["操控"] = self.trim(rank[8].find(
                "span", class_="font-arial c333").text)
            self.logItem()
        # 舒适性
            data["舒适性"] = self.trim(rank[10].find(
                "span", class_="font-arial c333").text)
            self.logItem()
        # 外观
            data["外观"] = self.trim(rank[11].find(
                "span", class_="font-arial c333").text)
            self.logItem()
        # 性价比
            data["性价比"] = self.trim(rank[13].find(
                "span", class_="font-arial c333").text)
            self.logItem()
        # 购买时间
            temp = self.trim(rank[3].find("dd").contents[0])
            temp = temp.replace("年", "-")
            temp = temp.replace("月", "-1 0:0:0")
            data["购买时间"] = temp
            self.logItem()
        # 购买地点
            data["购买地点"] = self.trim(rank[1].find("dd").contents[0])
        # 购车目的
            commentSet = comment.find_all(
                "dl", class_="choose-dl border-b-no")[0].find_all("p", class_="obje")
            if not commentSet[0]:
                temp = "无评论"
            else:
                temp = commentSet[0].text
            for i in range(1, len(commentSet)):
                temp = temp + ";" + commentSet[i].text
            data["购车目的"]=temp    
        # 用户评价
            data["用户评价"] = self.trimComment(comment.find("div", class_="text-cont").text)
        # insert into database
            print(data)
            # saleDAO.insert(data["车型"], data["购买时间"], data["购买地点"])
            # customerCommentDAO.insert(data["车型"],data["空间"], data["内饰"],data["操控"],data["舒适性"],data["外观"],data["性价比"])
            # purchasingPurposeDAO.insert(data["车型"],data["购车目的"],data["用户评价"])
        # count
        self.pageCount = self.pageCount + 1
        self.itemCount = 0
        print("-------------------------------------------")
        print(F"page {self.pageCount} is finished")

    def getAllCar(self, webIndex, carNumber):
        for pageIndex in range(1, carNumber, 1):
            self.getCar(webIndex, pageIndex)
            self.carCount = self.carCount+1
        print("-------------------------------------------")
        print(F"car {self.carCount} is finished")

    def startSpider(self):
        with open('backend/data/temp.json', 'r', encoding='utf8')as fp:
            webList = json.load(fp)
            for webItem in webList:
                self.getAllCar(webItem["index"], webItem["number"])
                self.carCount = 0
                


targetSpider=TargetSpider()
targetSpider.getAllCar(3462, 601)
#targetSpider.startSpider()

# for item in dataList:
#     print(item)
