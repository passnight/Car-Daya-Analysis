from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import pymysql


class SaleDAO:
    host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
    user = "root"
    password = "Password123"
    charset = "utf8"
    database = "car_big_data"

    def insert(self, carModel, minPrice, maxPrice):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"INSERT INTO `sale_price` (`car_model`, `min_price`, `max_price`) VALUES('{carModel}', '{minPrice}', '{maxPrice}')")
        db.commit()
        cursor.close()
        db.close()


saleDao = SaleDAO()


class SalePriceSpider:
    findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
    findTitle = re.compile(r'<span class="title">(.*)</span>')
    findRating = re.compile(
        r'<span class="rating_num" property="v:average">(.*)</span>')
    findJudge = re.compile(r'<span>(\d*)人评价</span>')
    findInq = re.compile(r'<span class="inq">(.*)</span>')
    findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
    # findLink = re.compile(r'href="(.*?)" style="color: #007bcd">')
    findPrice = re.compile(r'<dd>原价：(.*?)</dd>')
    findName = re.compile(r'<dt>(.*)</dt>')
    findNumber = re.compile(r'</td>\s<td>(.\d*)</td>')
    myttnumber = 360
    myindex = 30

    def askURL(self, url):
        head = {
            "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
        }
        request = urllib.request.Request(url, headers=head)
        html = ""
        try:
            response = urllib.request.urlopen(request)
            html = response.read().decode("GBK")
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                print(e.code)
            if hasattr(e, "reason"):
                print(e.reason)
        return html
    # 保存数据到表格

    def saveData(self, datalist, savepath):
        savepath = "nihao1.xls"
        print("save.......")
        book = xlwt.Workbook(
            encoding="utf-8", style_compression=0)  # 创建workbook对象
        sheet = book.add_sheet('汽车售价', cell_overwrite_ok=True)  # 创建工作表
        col = ("名称", "价格")
        for i in range(0, 2):
            sheet.write(0, i, col[i])  # 列名
        for i in range(0, myttnumber):
            # print("第%d条" %(i+1))       #输出语句，用来测试
            data = datalist[i]
            for j in range(0, 2):
                sheet.write(i+1, j, data[j])  # 数据
        book.save(savepath)  # 保存

    def formPrice(self, price):
        prices = price.split("-")
        if(len(prices) == 1):
            prices[0] = float(prices[0].replace("万", ""))*10000
            prices.append(prices[0])
            return prices
        else:
            prices[0] = float(prices[0])*10000
            prices[1] = float(prices[1].replace("万", ""))*10000
            return prices

    def getPrice(self):
        mynum = 0
        mymum2 = 0
     # 要爬取的网页链接
        baseurl = F"https://price.xcar.com.cn/city9999-0-0-0-{mynum}.htm"
     # 1.爬取网页
    # datalist = getData(baseurl)
        datalist = []  # 用来存储爬取的网页信息
        for i in range(0, self.myindex):  # 调用获取页面信息的函数，10次
            mynum = mynum+1
        # 要爬取的网页链接
            baseurl = F"https://price.xcar.com.cn/city9999-0-0-0-{mynum}.htm"
        # 1.爬取网页
            url = baseurl
            html = self.askURL(url)  # 保存获取到的网页源码
        # print(html)
        # 2.逐一解析数据
            soup = BeautifulSoup(html, "html.parser")
            for item in soup.find_all('dl', class_="t95_preferential_dl"):  # 查找符合要求的字符串
                data = {"型号": "", "最低价格": 0, "最高价格": 0}  # 保存一行销售信息
                # print(item)
                item = str(item)
                myName = re.findall(self.findName, item)[0]  # 通过正则表达式查找
                data["型号"] = myName
                myPrice = self.formPrice(re.findall(self.findPrice, item)[0])
                data["最低价格"] = myPrice[0]
                data["最高价格"] = myPrice[1]
                # priceDao.insert(data["型号"], data["最低价格"], data["最高价格"])
                datalist.append(data)
                print("one page is finished")
            print(
                "---------------------------------------------one line is finished---------------------------------------------")


salePriceSpider = SalePriceSpider()
salePriceSpider.getPrice()

