
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
import datetime

class PriceDAO:
    host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
    user = "root"
    password = "Password123"
    charset = "utf8"
    database = "car_big_data"

    def insert(self,carModel, saleDatetime,saleNumber,minPrice,maxPrice ):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"INSERT INTO `sale_info` (`car_model`, `sale_datetime`, `sale_number`, `min_price`, `max_price`) VALUES ('{carModel}', '{saleDatetime}', '{saleNumber}', '{minPrice}', '{maxPrice}');")
        db.commit()
        cursor.close()
        db.close()
    def insert(self, dataList):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        for item in dataList:
            carModel = item["车型"]
            saleDatetime = item["销售时间"]
            saleNumber = item["销量"]
            minPrice = item["最低售价"]
            maxPrice = item["最高售价"]
            cursor.execute(
                F"INSERT INTO `sale_info` (`car_model`, `sale_datetime`, `sale_number`, `min_price`, `max_price`) VALUES ('{carModel}', '{saleDatetime}', '{saleNumber}', '{minPrice}', '{maxPrice}');")
        db.commit()
        cursor.close()
        db.close()       



priceDao = PriceDAO()


class SaleNumberSpider:
    carCount = 0
    pageCount = 0
    itemCount = 0
    data={"车型":"未知车型","销售时间":"未知时间","销量":0,"最低售价":0,"最高售价":0}
    dataList = []
    headers = {
        "Host": "xl.16888.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1"
    }

    def saveToHtml(self, html):
        filename = "backend/temp/temp.html"
        file = open(filename, "w", buffering=1024*1024*4)
        file.write(html)
        file.close()
    def writeToCSV(self):
        outputFile = open("backend/temp/output.csv", "w")
        writer = csv.writer(outputFile)
        writer.writerow(("车型", "销售时间", "销量", "最低售价", "最高售价"))
        for item in self.dataList:
            writer.writerow((item["车型"], item["销售时间"], item["销量"], item["最低售价"],item["最高售价"]))
        outputFile.close()

    def dateRange(self, beginDate, endDate):
        dateList = []
        date = beginDate
        while date.__le__(endDate):
            dateList.append(date)
            if date.month < 12:
                date = datetime.datetime(date.year,date.month+1,date.day)
            else:
                date = datetime.datetime(date.year+1,1,date.day)
        return dateList
    def getSaleNumber(self, year, month, pageNumber):
        if month >9:
            startDate = str(year)+str(month)
        else:
            startDate =  str(year) + "0" + str(month)

        if month < 9:
            endDate = str(year)+"0"+str(month+1)
        elif month < 12:
            endDate = str(year)+str(month+1)
        else:
            endDate = str(year+1)+"01"
        for i in range(1,pageNumber+1):
            url = F"https://xl.16888.com/style-{startDate}-{endDate}-{i}.html"
            print(url)
            session = requests.Session()
            response = session.get(url, headers=self.headers)
            if not response:
                print("no response")
                return
            html = response.content.decode("utf-8")
            soup = bs4.BeautifulSoup(html)
            table = soup.find("table", class_="xl-table-def xl-table-a")
            cols = table.find_all("tr")
            for i in range(1, len(cols), 1):
                data={"车型":"未知车型","销售时间":"未知时间","销量":0,"最低售价":0,"最高售价":0}
                item = cols[i].find_all("td")
                data["车型"] = item[1].text
                data["销售时间"] = str(year)+"-"+str(month)+"-1 0:0:0"
                data["销量"] = int(item[2].text)
                data["最低售价"] = float(item[4].text.split("-")[0])*10000
                data["最高售价"] = float(item[4].text.split("-")[1])*10000
                self.dataList.append(data)
                self.itemCount = self.itemCount+1
                print("item "+ str(self.itemCount) +" is finished")
    def getAllSaleNumber(self, startYear, startMonth, endYear, endMonth, pageSize):
        dateList=self.dateRange(datetime.datetime.strptime(str(startYear) + str(startMonth), '%Y%m'),datetime.datetime.strptime(str(endYear) + str(endMonth), '%Y%m'))
        for date in dateList:
            self.getSaleNumber(date.year, date.month,pageSize)
            self.pageCount = self.pageCount+1
            self.itemCount = 0
            print("---------------page "+ str(self.pageCount) +" is finished-------------------")
    def startSpider(self):
        self.getAllSaleNumber(2015,1,2021,3,6)
        priceDao.insert(self.dataList)

            

saleNumberSpider = SaleNumberSpider()
# saleNumberSpider.getSaleNumber(2020, 3,1)
saleNumberSpider.startSpider()

