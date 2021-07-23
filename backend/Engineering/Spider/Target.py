
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
import SaleDAO



def trim(string):
    string = string.replace(" ", "")
    string = string.replace("\n", "")
    return string


data = {"车型": "", "配置": "", "空间": 0, "内饰": 0, "操控": 0,
        "舒适性": 0, "外观": 0, "性价比": 0, "购买时间": "", "购买地点": ""}
dataList = []
filename = "backend/temp/url.html"
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


outputFile = open("backend/temp/output.csv", "w")
writer = csv.writer(outputFile)
writer.writerow(("车型", "配置", "空间", "内饰", "操控",
                "舒适性", "外观", "性价比", "购买时间", "购买地点"))

#3-7没有经销商
def getCar(carIndex):
    url = F"https://k.autohome.com.cn/5273/index_{carIndex}.html#dataList"
    session = requests.Session()
    response = session.get(
        url, headers=headers)
    if not response:
        print("failed")
        return
    # print(chardet.detect(response.content))
    # fd.write(codecs.BOM_UTF8.decode(filename))
    soup = bs4.BeautifulSoup(response.content, 'html.parser')



    file = open(filename, "wb", buffering=1024*1024*4)
    file.write(response.content)
    file.close()
    html = open(filename, "r").read()

    # file = BytesIO()
    # file.write(response.content)
    # html=file.read()
    # file.close()






    # print(chardet.detect(html))
    soup = bs4.BeautifulSoup(html)
    comments = soup.find_all(class_="mouthcon-cont fn-clear")
    for comment in comments:
        rank = bs4.BeautifulSoup(
            comment.prettify()).find_all(class_="choose-dl")
        data = {"车型": "", "配置": "", "空间": 0, "内饰": 0, "操控": 0,
        "舒适性": 0, "外观": 0, "性价比": 0, "购买时间": "", "购买地点": ""}
        try:
            rank[14]
        except:
            print("one line not complete")
            continue
        # 车型爬取
        data["车型"] = trim(rank[0].find("a", target="_blank").text)
        data["配置"] = trim(rank[0].find("span", class_="font-arial").text)
        # 空间爬取
        data["空间"] = trim(rank[6].find("span", class_="font-arial c333").text)
        #内饰
        data["内饰"] = trim(rank[12].find("span", class_="font-arial c333").text)  
        #操控
        data["操控"] = trim(rank[8].find("span", class_="font-arial c333").text)
        #舒适性
        data["舒适性"] = trim(rank[10].find("span", class_="font-arial c333").text)
        #外观
        data["外观"] = trim(rank[11].find("span", class_="font-arial c333").text)
        #性价比
        data["性价比"] = trim(rank[13].find("span", class_="font-arial c333").text)
        #购买时间
        temp = trim(rank[3].find("dd").contents[0])
        temp = temp.replace("年","-")
        temp = temp.replace("月", "-1 0:0:0")
        data["购买时间"] = temp
        #购买地点
        data["购买地点"] = trim(rank[1].find("dd").contents[0])
        print("one line finished")
        # dataList.append(data)
        # writer.writerow(data.values())
        saleDAO = SaleDAO
        saleDAO.insert(data["车型"]+data["配置"], data["购买时间"],data["购买地点"])


def getAllCar(carNumber):
    for carIndex in range(1,carNumber,1):
        getCar(carIndex)






# getAllCar(1)
getAllCar(179)
print("-------------------------------------------")
for item in dataList:
    print(item)
