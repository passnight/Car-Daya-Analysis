
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


class UserDAO:
    host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
    user = "root"
    password = "Password123"
    charset = "utf8"
    database = "car_big_data"

    def insert(self, name, password, status):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"INSERT INTO `user_table` (`user_name`, `user_password`, `user_status`) VALUES ('{name}', '{password}', '{status}');")
        db.commit()
        cursor.close()
        db.close()

    def changePassword(self, name, newPassword):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"UPDATE `user_table` SET `user_password`='{newPassword}' WHERE(`user_name`='{name}')")
        db.commit()
        cursor.close()
        db.close()

    def deleteUser(self, name):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"DELETE FROM `user_table` WHERE (`user_name` = '{name}');")
        db.commit()
        cursor.close()
        db.close()
    
    def getAllUser(self):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"SELECT id, user_name, user_password, user_status FROM user_table;")
        users = []
        saleList = cursor.fetchall()
        for item in saleList:
            data = {"id":"","name":"","password":"","status":""}
            if item[3] == 0:
                data["status"] = "普通用户"
            else:
                data["status"] = "管理员"
            data["id"] = item[0]
            data["name"] = item[1]
            data["password"] = item[2]
            users.append(data)
        cursor.close()
        db.close()
        return users

    def isUser(self, name, password):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"SELECT id, user_name, user_password, user_status FROM user_table WHERE `user_name` = '{name}' AND `user_password` = '{password}';")
        if not cursor.fetchall():
            return False
        else:
            return True

    def isAdmin(self, name, password):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"SELECT id, user_name, user_password, user_status FROM user_table WHERE `user_name` = '{name}' AND `user_password` = '{password}' AND `user_status` = 1;")
        if not cursor.fetchall():
            return False
        else:
            return True

userDAO = UserDAO()
# print(userDAO.isUser("name0","password0"))
# print(userDAO.isAdmin("name0", "password0"))
# userDAO.insert("rjx","123456",0)
# userDAO.changePassword("new user name","996")
# userDAO.deleteUser("new user name")

