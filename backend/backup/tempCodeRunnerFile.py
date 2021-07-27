            # # 2.逐一解析数据
            # soup = BeautifulSoup(html, "html.parser")
            # for item in soup.find_all('dl', class_="t95_preferential_dl"):  # 查找符合要求的字符串
            #     data = []  # 保存一行销售信息
            #     #print(item)
            #     item = str(item)
            #     myName = re.findall(self.findName, item)[0]  # 通过正则表达式查找
            #     # print("name:"+myName+"                                       ///////////////////")
            #     data.append(myName)
            #     myPrice = re.findall(self.findPrice, item)[0]
            #     data.append(myPrice)
            #     print('price::'+myPrice+"                            ///////////")
            #     myname=re.findall(self.findName,item)[0].strip()
            #     print(myname+"                                 ////")
            #     data.append(myname)
            #     mynumber=re.findall(self.findNumber,item)[0]
            #     print(mynumber+"////////////////////////////////////////")
            #     imgSrc = re.findall(self.findImgSrc, item)[0]
            #     data.append(imgSrc)
            #     titles = re.findall(self.findTitle, item)
            #     if (len(titles) == 2):
            #         ctitle = titles[0]
            #         data.append(ctitle)
            #         otitle = titles[1].replace("/", "")  #消除转义字符
            #         data.append(otitle)
            #     else:
            #         data.append(titles[0])
            #         data.append(' ')
            #     rating = re.findall(self.findRating, item)[0]
            #     data.append(rating)
            #     judgeNum = re.findall(self.findJudge, item)[0]
            #     data.append(judgeNum)
            #     inq = re.findall(self.findInq, item)
            #     if len(inq) != 0:
            #         inq = inq[0].replace("。", "")
            #         data.append(inq)
            #     else:
            #         data.append(" ")
            #     bd = re.findall(self.findBd, item)[0]
            #     bd = re.sub('<br(\s+)?/>(\s+)?', "", bd)
            #     bd = re.sub('/', "", bd)
            #     data.append(bd.strip())
            # datalist.append(data)