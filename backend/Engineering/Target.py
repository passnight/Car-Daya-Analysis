
from io import BytesIO, StringIO
from bs4 import builder
import csv
import bs4
import requests
import pymysql
import json
from geopy.geocoders import Nominatim


def tansfromCityToProvince(city):

    areaData = {
        '北京市': ['北京市', '朝阳区', '海淀区', '通州区', '房山区', '丰台区', '昌平区', '大兴区', '顺义区', '西城区', '延庆县', '石景山区', '宣武区', '怀柔区', '崇文区', '密云县',
                '东城区', '门头沟区', '平谷区'],
        '广东省': ['广东省', '东莞市', '广州市', '中山市', '深圳市', '惠州市', '江门市', '珠海市', '汕头市', '佛山市', '湛江市', '河源市', '肇庆市', '潮州市', '清远市', '韶关市', '揭阳市', '阳江市', '云浮市', '茂名市', '梅州市', '汕尾市'],
        '山东省': ['山东省', '济南市', '青岛市', '临沂市', '济宁市', '菏泽市', '烟台市', '泰安市', '淄博市', '潍坊市', '日照市', '威海市', '滨州市', '东营市', '聊城市', '德州市', '莱芜市', '枣庄市'],
        '江苏省': ['江苏省', '苏州市', '徐州市', '盐城市', '无锡市', '南京市', '南通市', '连云港市', '常州市', '扬州市', '镇江市', '淮安市', '泰州市', '宿迁市'],
        '河南省': ['河南省', '郑州市', '南阳市', '新乡市', '安阳市', '洛阳市', '信阳市', '平顶山市', '周口市', '商丘市', '开封市', '焦作市', '驻马店市', '濮阳市', '三门峡市', '漯河市', '许昌市', '鹤壁市', '济源市'],
        '上海市': ['上海市', '松江区', '宝山区', '金山区', '嘉定区', '南汇区', '青浦区', '浦东新区', '奉贤区', '闵行区', '徐汇区', '静安区', '黄浦区', '普陀区', '杨浦区', '虹口区', '闸北区', '长宁区', '崇明县', '卢湾区'],
        '河北省': ['河北省', '石家庄市', '唐山市', '保定市', '邯郸市', '邢台市', '河北区', '沧州市', '秦皇岛市', '张家口市', '衡水市', '廊坊市', '承德市'],
        '浙江省': ['浙江省', '温州市', '宁波市', '杭州市', '台州市', '嘉兴市', '金华市', '湖州市', '绍兴市', '舟山市', '丽水市', '衢州市'],
        '陕西省': ['陕西省', '西安市', '咸阳市', '宝鸡市', '汉中市', '渭南市', '安康市', '榆林市', '商洛市', '延安市', '铜川市'],
        '湖南省': ['湖南省', '长沙市', '邵阳市', '常德市', '衡阳市', '株洲市', '湘潭市', '永州市', '岳阳市', '怀化市', '郴州市', '娄底市', '益阳市', '张家界市', '湘西州'],
        '重庆市': ['重庆市', '江北区', '渝北区', '沙坪坝区', '九龙坡区', '万州区', '永川市', '南岸区', '酉阳县', '北碚区', '涪陵区', '秀山县', '巴南区', '渝中区', '石柱县', '忠县', '合川市', '大渡口区', '开县', '长寿区', '荣昌县', '云阳县', '梁平县', '潼南县', '江津市', '彭水县', '璧山县', '綦江县',
                '大足县', '黔江区', '巫溪县', '巫山县', '垫江县', '丰都县', '武隆县', '万盛区', '铜梁县', '南川市', '奉节县', '双桥区', '城口县'],
        '福建省': ['福建省', '漳州市', '泉州市', '厦门市', '福州市', '莆田市', '宁德市', '三明市', '南平市', '龙岩市'],
        '天津市': ['天津市', '和平区', '北辰区', '河北区', '河西区', '西青区', '津南区', '东丽区', '武清区', '宝坻区', '红桥区', '大港区', '汉沽区', '静海县', '宁河县', '塘沽区', '蓟县', '南开区', '河东区'],
        '云南省': ['云南省', '昆明市', '红河州', '大理州', '文山州', '德宏州', '曲靖市', '昭通市', '楚雄州', '保山市', '玉溪市', '丽江地区', '临沧地区', '思茅地区', '西双版纳州', '怒江州', '迪庆州'],
        '四川省': ['四川省', '成都市', '绵阳市', '广元市', '达州市', '南充市', '德阳市', '广安市', '阿坝州', '巴中市', '遂宁市', '内江市', '凉山州', '攀枝花市', '乐山市', '自贡市', '泸州市', '雅安市', '宜宾市', '资阳市', '眉山市', '甘孜州'],
        '广西壮族自治区': ['广西壮族自治区', '贵港市', '玉林市', '北海市', '南宁市', '柳州市', '桂林市', '梧州市', '钦州市', '来宾市', '河池市', '百色市', '贺州市', '崇左市',  '防城港市'],
        '安徽省': ['安徽省', '芜湖市', '合肥市', '六安市', '宿州市', '阜阳市', '安庆市', '马鞍山市', '蚌埠市', '淮北市', '淮南市', '宣城市', '黄山市', '铜陵市', '亳州市', '池州市', '巢湖市', '滁州市'],
        '海南省': ['海南省', '三亚市', '海口市', '琼海市', '文昌市', '东方市', '昌江县', '陵水县', '乐东县', '五指山市', '保亭县', '澄迈县', '万宁市', '儋州市', '临高县', '白沙县', '定安县', '琼中县', '屯昌县'],
        '江西省': ['江西省', '南昌市', '赣州市', '上饶市', '吉安市', '九江市', '新余市', '抚州市', '宜春市', '景德镇市', '萍乡市', '鹰潭市'],
        '湖北省': ['湖北省', '武汉市', '宜昌市', '襄樊市', '荆州市', '恩施州', '孝感市', '黄冈市', '十堰市', '咸宁市', '黄石市', '仙桃市', '随州市', '天门市', '荆门市', '潜江市', '鄂州市', '神农架林区'],
        '山西省': ['山西省', '太原市', '大同市', '运城市', '长治市', '晋城市', '忻州市', '临汾市', '吕梁市', '晋中市', '阳泉市', '朔州市'],
        '辽宁省': ['辽宁省', '大连市', '沈阳市', '丹东市', '辽阳市', '葫芦岛市', '锦州市', '朝阳市', '营口市', '鞍山市', '抚顺市', '阜新市', '本溪市', '盘锦市', '铁岭市'],
        '台湾省': ['台湾省', '台北市', '高雄市', '台中市', '新竹市', '基隆市', '台南市', '嘉义市'],
        '黑龙江省': ['黑龙江', '齐齐哈尔市', '哈尔滨市', '大庆市', '佳木斯市', '双鸭山市', '牡丹江市', '鸡西市', '黑河市', '绥化市', '鹤岗市', '伊春市', '大兴安岭地区', '七台河市'],
        '内蒙古自治区': ['内蒙古自治区', '赤峰市', '包头市', '通辽市', '呼和浩特市', '乌海市', '鄂尔多斯市', '呼伦贝尔市', '兴安盟', '巴彦淖尔盟', '乌兰察布盟', '锡林郭勒盟', '阿拉善盟'],
        '香港特别行政区': ["香港", "香港特别行政区"],
        '澳门特别行政区': ['澳门', '澳门特别行政区'],
        '贵州省': ['贵州省', '贵阳市', '黔东南州', '黔南州', '遵义市', '黔西南州', '毕节地区', '铜仁地区', '安顺市', '六盘水市'],
        '甘肃省': ['甘肃省', '兰州市', '天水市', '庆阳市', '武威市', '酒泉市', '张掖市', '陇南地区', '白银市', '定西地区', '平凉市', '嘉峪关市', '临夏回族自治州', '金昌市', '甘南州'],
        '青海省': ['青海省', '西宁市', '海西州', '海东地区', '海北州', '果洛州', '玉树州', '黄南藏族自治州'],
        '新疆维吾尔自治区': ['新疆', '新疆维吾尔自治区', '乌鲁木齐市', '伊犁州', '昌吉州', '石河子市', '哈密地区', '阿克苏地区', '巴音郭楞州', '喀什地区', '塔城地区', '克拉玛依市', '和田地区', '阿勒泰州', '吐鲁番地区', '阿拉尔市', '博尔塔拉州', '五家渠市',
                     '克孜勒苏州', '图木舒克市'],
        '西藏自治区': ['西藏区', '拉萨市', '山南地区', '林芝地区', '日喀则地区', '阿里地区', '昌都地区', '那曲地区'],
        '吉林省': ['吉林省', '吉林市', '长春市', '白山市', '白城市', '延边州', '松原市', '辽源市', '通化市', '四平市'],
        '宁夏回族自治区': ['宁夏回族自治区', '银川市', '吴忠市', '中卫市', '石嘴山市', '固原市']
    }
    for key, value in areaData.items():
        for i in value:
            if city in i:
                return key

    return "南海诸岛"
class SaleDAO:
    host = "rm-bp1at82o2l9uonoizao.mysql.rds.aliyuncs.com"
    user = "root"
    password = "Password123"
    charset = "utf8"
    database = "car_big_data"

    def insert(self, carModel, saleDatetime, saleRegion, salePrice):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"INSERT INTO `basic_sale_info_table` (`car_model`, `sale_datetime`, `sale_region`, `sale_price`) VALUES ('{carModel}', '{saleDatetime}', '{saleRegion}', {salePrice})")
        db.commit()
        cursor.close()
        db.close()
    def insertAll(self, dataList):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        for item in dataList:
            carModel = item["车型"]
            saleDatetime = item["购买时间"]
            saleRegion = item["购买地点"]
            salePrice = item["价格"]
            cursor.execute(
                F"INSERT INTO `basic_sale_info_table` (`car_model`, `sale_datetime`, `sale_region`, `sale_price`) VALUES ('{carModel}', '{saleDatetime}', '{saleRegion}', {salePrice})")
        db.commit()
        cursor.close()
        db.close()  
    def getAllCarModel(self):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute("select distinct car_model from basic_sale_info_table ")
        carModelTuple = cursor.fetchall()
        carModelList = []
        for item in carModelTuple:
            carModelList.append(item[0])
        cursor.close()
        db.close()
        return carModelList
    def getAllSaleInfo(self, carModel, startDate, endDate):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(
            F"select sale_region from basic_sale_info_table where car_model = '{carModel}' and sale_datetime between '{startDate}' and '{endDate}'")
        resultTuple = cursor.fetchall()
        resultList = []
        for item in resultTuple:
            resultList.append(item[0])
        cursor.close()
        db.close()
        result = {"河北省": 0,
             "山西省": 0,
             "辽宁省": 0,
             "吉林省": 0,
             "黑龙江省": 0,
             "江苏省": 0,
             "浙江省": 0,
             "安徽省": 0,
             "福建省": 0,
             "江西省": 0,
             "山东省": 0,
             "河南省": 0,
             "湖北省": 0,
             "湖南省": 0,
             "广东省": 0,
             "海南省": 0,
             "四川省": 0,
             "贵州省": 0,
             "云南省": 0,
             "陕西省": 0,
             "甘肃省": 0,
             "青海省": 0,
             "台湾省": 0,
             "内蒙古自治区": 0,
             "广西壮族自治区": 0,
             "西藏自治区": 0,
             "宁夏回族自治区": 0,
             "新疆维吾尔自治区": 0,
             "北京市": 0,
             "天津市": 0,
             "上海市": 0,
             "重庆市": 0,
             "香港特别行政区": 0,
             "澳门特别行政区": 0,
             "南海诸岛":0}
        for item in resultList:
            result[tansfromCityToProvince(
                item)] = result[tansfromCityToProvince(item)] + 1
        return result
         

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
    def insertAll(self, dataList):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        for item in dataList:
            carModel = item["车型"]
            carSpace = item["空间"]
            carDecoration = item["内饰"]
            carControl = item["操控"]
            carConfortableness = item["舒适性"]
            carAppearance = item["外观"]
            carValueForMoney = item["性价比"]
            cursor.execute(
                F"INSERT INTO `customer_comment_table` (`car_model`, `car_space`, `car_decoration`, `car_control`, `car_confortableness`, `car_appearance`, `car_value_for_money`) VALUES('{carModel}', '{carSpace}', '{carDecoration}', '{carControl}', '{carConfortableness}', '{carAppearance}', '{carValueForMoney}')")
        db.commit()
        cursor.close()
        db.close()
    def getAllComment(self, carModel):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        cursor.execute(F"SELECT avg(car_space), avg(car_decoration), avg(car_control), avg(car_confortableness), avg(car_appearance), avg(car_value_for_money) from customer_comment_table where car_model='{carModel}'")
        comment = []
        commentList = cursor.fetchall()
        for item in commentList[0]:
            comment.append(int(item * 20))
        cursor.close()
        db.close()
        return comment
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

    def insertAll(self, dataList):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        for item in dataList:
             carModel = item["车型"]
             purchasePurpose = item["购车目的"]
             comment = item["用户评价"]
        cursor.execute(
            F"INSERT INTO `purchasing_purpose_table` (`car_model`, `purchase_purpose`, `comment`) VALUES ('{carModel}', '{purchasePurpose}', '{comment}');")
        db.commit()
        cursor.close()
        db.close()
    def getAllPurchasingPurpose(self, carModel, priceLevel):
        db = pymysql.connect(host=self.host, user=self.user,
                             password=self.password, database=self.database, charset=self.charset)
        cursor = db.cursor()
        carType="有限制"
        if carModel != "无限制":
            if priceLevel == "选项1":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price between 0 and 10000 and car_model = '{carModel}'")
                priceLevelName = "1万以下"
            elif priceLevel == "选项2":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price between 10000 and 50000 and car_model = '{carModel}'")
                priceLevelName = "1万到5万"
            elif priceLevel == "选项3":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price between 50000 and 100000 and car_model = '{carModel}'")
                priceLevelName = "5万到10万"
            elif priceLevel == "选项4":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price between 100000 and 200000 and car_model = '{carModel}'")
                priceLevelName = "10万到20万"
            elif priceLevel == "选项5":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price > 200000 and car_model = '{carModel}'")
                priceLevelName = "20万以上"
            else:
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where car_model = '{carModel}'")
                priceLevelName = "无限制"
        else:
            carType = "无限制"
            if priceLevel == "选项1":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price between 0 and 10000")
                priceLevelName = "1万以下"
            elif priceLevel == "选项2":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price between 10000 and 50000")
                priceLevelName = "1万到5万"
            elif priceLevel == "选项3":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price between 50000 and 100000")
                priceLevelName = "5万到10万"
            elif priceLevel == "选项4":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price between 100000 and 200000")
                priceLevelName = "10万到20万"
            elif priceLevel == "选项5":
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where sale_price > 200000")
                priceLevelName = "无限制"
            else:
                cursor.execute(
                        F"select car_model, purchase_purpose, sale_price from purchasing_purpose_table where car_model = '{carModel}'")
                priceLevelName = "选项0"
        datas = cursor.fetchall()
        purposes = []
        for item in datas:
            if carType != "无限制":
                purposes.append({"carType": item[0], "price": F"{priceLevelName}", "purchaseTarget": item[1]})
            else:
                purposes.append({"carType": "无限制", "price": F"{priceLevelName}", "purchaseTarget": item[1]})
        cursor.close()
        db.close()
        return purposes

    def getAllPurchasingcomment(self, carModel):
        if carModel != "无限制":
            db = pymysql.connect(host=self.host, user=self.user,
                                password=self.password, database=self.database, charset=self.charset)
            cursor = db.cursor()
            print(
                F"select car_model, comment from purchasing_purpose_table where car_model = '{carModel}'")
            cursor.execute(
                    F"select car_model, comment from purchasing_purpose_table where car_model = '{carModel}'")
            datas = cursor.fetchall()
            comments = []
            for item in datas:
                comments.append({"carType": item[0], "userComment": item[1]})
            cursor.close()
            db.close()
        else:
            db = pymysql.connect(host=self.host, user=self.user,
                                 password=self.password, database=self.database, charset=self.charset)
            cursor = db.cursor()
            cursor.execute(
                F"select car_model, comment from purchasing_purpose_table")
            datas = cursor.fetchall()
            comments = []
            for item in datas:
                comments.append({"carType": item[0], "userComment": item[1]})
            cursor.close()
            db.close()
        return comments
    

purchasingPurposeDAO = PurchasingPurposeDAO()
saleDAO = SaleDAO()
customerCommentDAO = CustomerCommentDAO()
class TargetSpider:
    carCount = 1
    pageCount = 0
    itemCount = 0
    data = {"车型": "","价格":0, "配置": "", "空间": 0, "内饰": 0, "操控": 0,
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
            data = {"车型": "","价格":0, "配置": "", "空间": 0, "内饰": 0, "操控": 0,
                    "舒适性": 0, "外观": 0, "性价比": 0, "购买时间": "", "购买地点": "", "购车目的": [], "用户评价": ""}
            try:
                rank[14]
            except:
                print("one line not complete")
                continue
        # 车型爬取
            data["车型"] = self.trim(rank[0].find("a", target="_blank").text)
            self.logItem()
        #配置爬取
            data["配置"] = self.trim(rank[0].find("span", class_="font-arial").text)
            self.logItem()
        #价格爬取
            data["价格"] =float(self.trim(rank[4].find("dd", class_="font-arial bg-blue").text).replace("万元",""))*10000
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
            self.dataList.append(data)
            saleDAO.insert(data["车型"], data["购买时间"], data["购买地点"],data["价格"])
            customerCommentDAO.insert(data["车型"],data["空间"], data["内饰"],data["操控"],data["舒适性"],data["外观"],data["性价比"])
            purchasingPurposeDAO.insert(data["车型"],data["购车目的"],data["用户评价"])
        # count
        self.pageCount = self.pageCount + 1
        self.itemCount = 0
        print("-------------------------------------------")
        print(F"car {self.carCount} page {self.pageCount} is finished")

    def getAllCar(self, webIndex, carNumber):
        for pageIndex in range(1, carNumber, 1):
            self.getCar(webIndex, pageIndex)
        self.pageCount = 0
        self.carCount = self.carCount+1
        print("-------------------------------------------")
        print(F"car {self.carCount} is finished")
        print("uploading to database")
        # saleDAO.insert(self.dataList)
        # customerCommentDAO.insert(self.dataList)
        # purchasingPurposeDAO.insert(self.dataList)
        # self.dataList = []

    def startSpider(self):
        with open('backend/data/temp.json', 'r', encoding='utf8')as fp:
            webList = json.load(fp)
            for webItem in webList:
                self.getAllCar(webItem["index"], webItem["number"])
                


targetSpider=TargetSpider()
# targetSpider.getAllCar(3462, 601)
# targetSpider.startSpider()

# for item in dataList:
#     print(item)
