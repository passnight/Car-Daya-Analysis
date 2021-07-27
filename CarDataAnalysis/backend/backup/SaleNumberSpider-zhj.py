from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import pymysql
import io


class PriceDAO:
    host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
    user = "root"
    password = "Password123"
    charset = "utf8"
    database = "car_big_data"

    def insert(self, carModel, saleMonth, saleNumber):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"INSERT INTO `sale_number` (`car_model`, `sale_month`, `sale_number`) VALUES('{carModel}', '{saleMonth}', '{saleNumber}')")
        db.commit()
        cursor.close()
        db.close()


priceDao = PriceDAO()


class SaleNumberSpider:


    findLink = re.compile(r'href="(.*?)" style="color: #007bcd">')
    findName = re.compile(r'<td style="display:none">(.*?)</td>')
    findNumber = re.compile(r'</td>\s<td>(.\d*)</td>')
    findNUMBER2 = re.compile(r'<td>(.*?)</td>')
    findTime = re.compile(r'article>\s<h1>(.*)月')

    mytotalnumber = 100
    myindex = 20

    def askURL(self, url):
        head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
        }
        request = urllib.request.Request(url, headers=head)
        html = ""
        try:
            response = urllib.request.urlopen(request)
            html = response.read().decode("utf-8")
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        return html
    # 保存数据到表格


    def saveData(datalist, savepath):
        print("save.......")
        book = xlwt.Workbook(encoding="utf-8", style_compression=0) 
        sheet = book.add_sheet('汽车销量数据', cell_overwrite_ok=True) 
        col = ("时间", "名称", "销量")
        for i in range(0, 3):
            sheet.write(0, i, col[i]) 
        for i in range(0, mytotalnumber):
            data = datalist[i]
            for j in range(0, 3):
                sheet.write(i+1, j, data[j])
        book.save(savepath) 

    def saveToHtml(self, html):
        filename = "backend/temp/temp.html"
        file = open(filename, "w", buffering=1024*1024*4)
        file.write(html)
        file.close()

    def getSaleNumber(self):

        webIndex = 61697
        mydate = ""
        # 1.爬取网页
        datalist = []  # 用来存储爬取的网页信息
        for i in range(0, self.myindex):  # 调用获取页面信息的函数，10次
            check = True
            webIndex = webIndex+i*i
            # 要爬取的网页链接
            baseurl = F"https://m.gasgoo.com/qcxl/article/{webIndex}.html"
            url = baseurl
            html = self.askURL(url)  # 保存获取到的网页源码
            # print(html)
            # 2.逐一解析数据
            soup = BeautifulSoup(html, "html.parser")
            for item in soup.find_all('tr', align="center", height="34", bgcolor=""):  # 查找符合要求的字符串
                data = {"型号":"","销售时间":"", "销售数量":0}  # 保存一行销售信息
                item = str(item)
                if check:
                    for item2 in soup.find_all('div', class_="inner"):  # 查找符合要求的字符串
                        item2 = str(item2)
                        mydate = re.findall(self.findTime, item2)[0] + "月"
                    check = False

                link = re.findall(self.findLink, item)[0]  # 通过正则表达式查找
            #  print("link:"+link+"   //")
                data["销售时间"] = (mydate).replace("年", "-").replace("月", "-") + "1 0:0:0"
                #data.append(link)

                myname = re.findall(self.findName, item)[0]
            #  print(myname+"                                 ////")
                data["型号"] = (myname)
                mynumber = re.search(self.findNumber, item)[0]
                mynumber2 = re.findall(self.findNUMBER2, mynumber)[0]
                data["销售数量"] = int(mynumber2)
                datalist.append(data)
                print(data)
                # priceDao.insert(data["型号"], data["销售时间"], data["销售数量"])



saleNumberSpider = SaleNumberSpider()
saleNumberSpider.getSaleNumber()
