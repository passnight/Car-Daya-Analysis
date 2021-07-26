from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3






########################################

# #findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，标售规则   影片详情链接的规则
# findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
# findTitle = re.compile(r'<span class="title">(.*)</span>')
# findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# findJudge = re.compile(r'<span>(\d*)人评价</span>')
# findInq = re.compile(r'<span class="inq">(.*)</span>')
# findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

findLink = re.compile(r'href="(.*?)" style="color: #007bcd">')
findName=re.compile(r'<td style="display:none">(.*?)</td>')
findNumber=re.compile(r'</td>\s<td>(.\d*)</td>')
findNUMBER2=re.compile(r'<td>(.*?)</td>')
findTime =re.compile(r'article>\s<h1>(.*)月')

#<a style="color: #007bcd" href="https://m.gasgoo.com/qcxl/cxxl/2021/6/1540">
 #                               瑞虎8
#   #                          </a>
#   <tr align="center" height="34" bgcolor="">
#                         <td>5</td>
                        
#                         <td style="display:none">吉利汽车</td>
#                         <td style="display:none">吉利</td>
#                         <td>
#                             <a style="color: #007bcd" href="https://m.gasgoo.com/qcxl/cxxl/2021/6/1817">
#                                 豪越
#                             </a>
#                         </td>
                        
#                         <td>3806</td>
#                         <td>22437</td>
#                         <td style="display:none">3605</td>
#                         <td>5.58%</td>
#                         <td style="display:none">2372</td>
#                         <td>60.46%</td>
#                     </tr>
mytotalnumber=1
myindex=2
def main():
   




    mynum=61697
    mydate=""
    baseurl = F"https://m.gasgoo.com/qcxl/article/{mynum}.html"  #要爬取的网页链接
    # 1.爬取网页
   # datalist = getData(baseurl)
    datalist = []  #用来存储爬取的网页信息
    for i in range(0, myindex):  # 调用获取页面信息的函数，10次
        check=True
        mynum = mynum+i*i
        baseurl = F"https://m.gasgoo.com/qcxl/article/{mynum}.html"  #要爬取的网页链接
        url = baseurl 
        html = askURL(url)  # 保存获取到的网页源码
       # print(html)
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
       # print("HELLLLLLLLLLLLLLLLLLLLLLL")
       # print(mynum)
        for item in soup.find_all('tr', align="center", height="34", bgcolor=""):  # 查找符合要求的字符串
             data = []  # 保存一行销售信息
             item = str(item)
            #  print("item:::"+item)
            #  if item=="":
            #     # print("根本就没有！！！！！！！！！！！！！！！！！！")
            #      break
            #  else:
             if check:
                for item2 in soup.find_all('div', class_="inner"):  # 查找符合要求的字符串
                    item2 = str(item2)
                 #   print("头  item2222222        "+item2+"         尾")
                    #if item2==" ":
                  #   print("根本就没有！！！！！！！！！！！！！！！！！！")
                  #   break
                    mydate=re.findall(findTime,item2)[0] +"月"
                   # print(mydate)
                check=False
         
             link = re.findall(findLink, item)[0]  # 通过正则表达式查找
           #  print("link:"+link+"   //") 
             data.append(mydate)
             #data.append(link)
            
             myname=re.findall(findName,item)[0]
           #  print(myname+"                                 ////")
             data.append(myname)
             mynumber=re.search(findNumber,item)[0]
             mynumber2=re.findall(findNUMBER2,mynumber)[0]
             data.append(mynumber2)
            # print('myn:'+mynumber2+"////////////////////////////////////////")
        #     imgSrc = re.findall(findImgSrc, item)[0]
        #     data.append(imgSrc)
        #     titles = re.findall(findTitle, item)
        #     if (len(titles) == 2):
        #         ctitle = titles[0]
        #         data.append(ctitle)
        #         otitle = titles[1].replace("/", "")  #消除转义字符
        #         data.append(otitle)
        #     else:
        #         data.append(titles[0])
        #         data.append(' ')
        #     rating = re.findall(findRating, item)[0]
        #     data.append(rating)
        #     judgeNum = re.findall(findJudge, item)[0]
        #     data.append(judgeNum)
        #     inq = re.findall(findInq, item)
        #     if len(inq) != 0:
        #         inq = inq[0].replace("。", "")
        #         data.append(inq)
        #     else:
        #         data.append(" ")
        #     bd = re.findall(findBd, item)[0]
        #     bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
        #     bd = re.sub('/', "", bd)
        #     data.append(bd.strip())
             datalist.append(data)

    #return datalist
    
    savepath = F"test.xls"    #当前目录新建XLS，存储进去
    # dbpath = "movie.db"              #当前目录新建数据库，存储进去
    # 3.保存数据
    saveData(datalist,savepath)      #2种存储方式可以只选择一种
    # saveData2DB(datalist,dbpath)



# 保存数据到表格
def saveData(datalist,savepath):
    print("save.......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) #创建workbook对象
    sheet = book.add_sheet('汽车销量数据', cell_overwrite_ok=True) #创建工作表
    col = ("时间","名称","销量")
    for i in range(0,3):
        sheet.write(0,i,col[i])  #列名
    for i in range(0,mytotalnumber):
        # print("第%d条" %(i+1))       #输出语句，用来测试
        data = datalist[i]
        for j in range(0,3):
            sheet.write(i+1,j,data[j])  #数据
    book.save(savepath) #保存


# def saveData2DB(datalist,dbpath):
#     init_db(dbpath)
#     conn = sqlite3.connect(dbpath)
#     cur = conn.cursor()
#     for data in datalist:
#             for index in range(len(data)):
#                 if index == 4 or index == 5:
#                     continue
#                 data[index] = '"'+data[index]+'"'
#             sql = '''
#                     insert into movie250(
#                     info_link,pic_link,cname,ename,score,rated,instroduction,info)
#                     values (%s)'''%",".join(data)
#             # print(sql)     #输出查询语句，用来测试
#             cur.execute(sql)
#             conn.commit()
#     cur.close
#     conn.close()


# def init_db(dbpath):
#     sql = '''
#         create table movie250(
#         id integer  primary  key autoincrement,
#         info_link text,
#         pic_link text,
#         cname varchar,
#         ename varchar ,
#         score numeric,
#         rated numeric,
#         instroduction text,
#         info text
#         )
#
#
#     '''  #创建数据表
#     conn = sqlite3.connect(dbpath)
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()

# 保存数据到数据库




# # 爬取网页
# def getData(baseurl):
#     datalist = []  #用来存储爬取的网页信息
#     for i in range(0, 10):  # 调用获取页面信息的函数，10次
#         url = baseurl + str(i * 25)
#         html = askURL(url)  # 保存获取到的网页源码
#         # 2.逐一解析数据
#         soup = BeautifulSoup(html, "html.parser")
#         for item in soup.find_all('div', class_="item"):  # 查找符合要求的字符串
#             data = []  # 保存一部电影所有信息
#             item = str(item)
#             link = re.findall(findLink, item)[0]  # 通过正则表达式查找
#             data.append(link)
#             imgSrc = re.findall(findImgSrc, item)[0]
#             data.append(imgSrc)
#             titles = re.findall(findTitle, item)
#             if (len(titles) == 2):
#                 ctitle = titles[0]
#                 data.append(ctitle)
#                 otitle = titles[1].replace("/", "")  #消除转义字符
#                 data.append(otitle)
#             else:
#                 data.append(titles[0])
#                 data.append(' ')
#             rating = re.findall(findRating, item)[0]
#             data.append(rating)
#             judgeNum = re.findall(findJudge, item)[0]
#             data.append(judgeNum)
#             inq = re.findall(findInq, item)
#             if len(inq) != 0:
#                 inq = inq[0].replace("。", "")
#                 data.append(inq)
#             else:
#                 data.append(" ")
#             bd = re.findall(findBd, item)[0]
#             bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
#             bd = re.sub('/', "", bd)
#             data.append(bd.strip())
#             datalist.append(data)

#     return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

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





if __name__ == "__main__":  # 当程序执行时
    # 调用函数
     main()
    # init_db("movietest.db")
     print("爬取完毕！")
# <tr align="center" height="34" bgcolor="#f3f3f3">
#                         <td>4</td>
                        
#                         <td style="display:none">长城汽车</td>
#                         <td style="display:none">哈弗</td>
#                         <td>
#                             <a style="color: #007bcd" href="https://m.gasgoo.com/qcxl/cxxl/2021/6/1923">
#                                 哈弗赤兔
#                             </a>
#                         </td>
                        
#                         <td>4090</td>
#                         <td>7348</td>
#                         <td style="display:none">3258</td>
#                         <td>25.54%</td>
#                         <td style="display:none">0</td>
#                         <td>0%</td>
#                     </tr>