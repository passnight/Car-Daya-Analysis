# -*- coding = utf-8 -*-
# @Time : 2021/7/23 10:01
# @Author : ChenDuowen
# @File : json.py
# @Software : PyCharm

import os
import re
'''
第三步 解析出每个车型的数据json，保存到本地。
'''
if __name__=="__main__":
    print("Start...")
    rootPath = "C:\\Users\\90643\\Desktop\\autoHome\\html\\"
    files = os.listdir(rootPath)
    for file in files:
        print("fileName=="+file.title())
        text = ""
        for fi in open(rootPath+file,'r',encoding="utf-8"):
            text = text+fi
        else:
            print("fileName=="+file.title())
        #解析数据的json
        jsonData = ""
        config = re.search('var config = (.*?){1,};',text)
        if config!= None:
            print(config.group(0))
            jsonData = jsonData+ config.group(0)
        option = re.search('var option = (.*?)};',text)
        if option != None:
            print(option.group(0))
            jsonData = jsonData+ option.group(0)
        bag = re.search('var bag = (.*?);',text)
        if bag != None:
            print(bag.group(0))
            jsonData = jsonData+ bag.group(0)
        # jsonData = ""
        # keyLink = re.search('var keyLink = (.*?)', text)
        # if keyLink != None:
        #     print(keyLink.group(0))
        #     jsonData = jsonData + keyLink.group(0)
        # config = re.search('var config = (.*?){1,};', text)
        # if config != None:
        #     print(config.group(0))
        #     jsonData = jsonData + config.group(0)
        # option = re.search('var option = (.*?)};', text)
        # if option != None:
        #     print(option.group(0))
        #     jsonData = jsonData + option.group(0)
        # bag = re.search('var bag = (.*?);', text)
        # if bag != None:
        #     print(bag.group(0))
        #     jsonData = jsonData + bag.group(0)
        # print(jsonData)
        f = open("C:\\Users\\90643\\Desktop\\autoHome\\json\\"+file,"a",encoding="utf-8")
        f.write(jsonData)
        f.close()