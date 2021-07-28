from flask import Flask, request
from flask_cors import cross_origin, CORS
import json


import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
# 将需要导入模块代码文件相对于当前文件目录的绝对路径加入到sys.path中
sys.path.append(os.path.join(current_dir, ".."))

global feedbackSelectModel
global feedbackSelectPriceLevel
global mainSelectModel
global mainStartDate
global mainEndDate
global userName
feedbackSelectModel = "无限制"
feedbackSelectPriceLevel = "选项0"
mainSelectModel = "卡罗拉"
mainStartDate = "2020-7-1"
mainEndDate = "2021-8-1"
userName = "user name"
from backend.Engineering import Target as target
from backend.Sale import SaleNumber as saleNumber
import User as user
app = Flask(__name__, static_folder="http", static_url_path="/pages")
CORS(app, supports_credentials=True)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, motherfuckdasdasder!</p>"


# router
@app.route('/')
def index():
    return 'Index Page'


# @app.route('/hello')
# def hello():
#     return 'Hello, World'
# app.run()

@app.route("/Login", methods=["get", "post"])
@cross_origin(supports_credentials=True)
def handleLoginRequest():
    global userName
    myForm = request.form
    result = myForm.to_dict()
    if user.userDAO.isAdmin(result["username"], result["password"]):
        userName = result["username"]
        return "admin"
    elif user.userDAO.isUser(result["username"], result["password"]):
        userName = result["username"]
        return "user"
    else:
        return "fail"


@app.route("/UserName", methods=["get", "post"])
@cross_origin(supports_credentials=True)
def handleUserNameRequest():
    global userName
    return userName


@app.route("/Manager/UserList", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleUserListRequest():
    userList = user.userDAO.getAllUser()
    users = []
    for item in userList:
        data = {
            "userID": "1",
            "userName": "路人甲",
            "userPassword": "000000",
            "userStatus": "管理员",
        }
        data["userID"] = item["id"]
        data["userName"] = item["name"]
        data["userPassword"] = item["password"]
        data["userStatus"] = item["status"]
        users.append(data)
    return json.dumps(users)


@app.route("/Manager/AddUser", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleAddUserRequest():
    myForm = request.form
    result = myForm.to_dict()
    print("add user and the info is ", myForm)
    user.userDAO.insert(result["username"], result["password"], 0)
    return "success"


@app.route("/Manager/ChangeUserInfo", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleChangeUserInfoRequest():
    myForm = request.form
    result = myForm.to_dict()
    print("change user info and the parameters are ", myForm)
    user.userDAO.changePassword(result["username"], result["password"])
    return "success"


@app.route("/Manager/DeleteUser", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleDeleteUserRequest():
    myForm = request.form
    result = myForm.to_dict()
    print("delete user and the parameters are ", myForm)
    user.userDAO.deleteUser(result["username"])
    return "success"


@app.route("/Main/CarModel.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleMainCarModelRequest():
    carModelList = target.saleDAO.getAllCarModel()
    carModels = [{"model": "无限制"}]
    for item in carModelList:
        carModels.append({"model": item})
    return json.dumps(carModels)


@app.route("/Main/SellingData.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleSellingDataRequest():

    myForm = request.form
    result = myForm.to_dict()
    print(myForm)
    rowData = target.saleDAO.getAllSaleInfo(
        result["selectedCarModel"], result["startDate"], result["endDate"])
    global mainSelectModel
    global mainStartDate
    global mainEndDate
    mainSelectModel = result["selectedCarModel"]
    mainStartDate = result["startDate"]
    mainEndDate = result["endDate"]
    sellingData = []
    for key, value in rowData.items():
        sellingData.append(
            {"name": key, "value": value}
        )
    return json.dumps(sellingData)


@app.route("/Main/SendParameter.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleSendParameterFromMain():
    myForm = request.form
    result = myForm.to_dict()
    print(myForm)
    global mainSelectModel
    global mainStartDate
    global mainEndDate
    mainSelectModel = result["selectedCarModel"]
    mainStartDate = result["startDate"]
    mainEndDate = result["endDate"]


@app.route("/Main/TopSale", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleTopSaleRequest():
    return json.dumps(saleNumber.priceDAO.getTopSales(10))

@app.route("/Feedback/CarModel.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleFeedbackCarModelRequest():
    carModelList = target.saleDAO.getAllCarModel()
    carModels = [{"model": "无限制"}]
    for item in carModelList:
        carModels.append({"model": item})
    return json.dumps(carModels)
@app.route("/Feedback/price.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handlePriceRequest():
    price = [
        {"value": "选项0", "label": "无限制"},
        {"value": "选项1", "label": "1万以下"},
        {"value": "选项2", "label": "1万到5万"},
        {"value": "选项3", "label": "5万到10万"},
        {"value": "选项4", "label": "10万到20万"},
        {"value": "选项5", "label": "20万以上"},
    ]
    return json.dumps(price)
@app.route("/Feedback/Comment.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleCommentRequest():
    global feedbackSelectModel
    global feedbackSelectPriceLevel
    print(F"get comment about {feedbackSelectModel}")
    # comment = [{"carType": "userComment", "userComment": "userComment"}]
    comment = target.purchasingPurposeDAO.getAllPurchasingcomment(feedbackSelectModel)
    return json.dumps(comment)
@app.route("/Feedback/Purpose.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handlePurposeRequest():
    global feedbackSelectModel
    global feedbackSelectPriceLevel
    print(
        F"get purpose about {feedbackSelectModel} and price in {feedbackSelectPriceLevel}")
    # comment = [{"carType": "userComment", "userComment": "userComment"}]
    comment = target.purchasingPurposeDAO.getAllPurchasingPurpose(feedbackSelectModel, feedbackSelectPriceLevel)
    return json.dumps(comment)
@app.route("/Feedback/SendParameter", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleSendParameter():
    dataForm = request.form
    global feedbackSelectModel
    global feedbackSelectPriceLevel
    feedbackSelectModel = dataForm["chooseModel"]
    feedbackSelectPriceLevel = dataForm["priceLevel"]
    print(
        F"now feedbackSelectModel is set to {feedbackSelectModel}, and feedbackSelectPriceLevel is set to {feedbackSelectPriceLevel}")
    return json.dumps(dataForm)





@app.route("/CarModel.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleCarModelRequest():
    carModels = [
        {"model": "A"},
        {"model": "B"},
        {"model": "C"},
        {"model": "D"},
        {"model": "E"},
    ]
    return json.dumps(carModels)

@app.route("/FChart1.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleFChart1Request():
    data = 66
    print(json.dumps(data))
    return json.dumps(data)

@app.route("/FChart1.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleFChart2Request():
    data = 66
    print(json.dumps(data))
    return json.dumps(data)

@app.route("/PChart1.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handlePChart1Request():
    data = 66
    print(json.dumps(data))
    return json.dumps(data)

@app.route("/PChart1.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handlePChart2Request():
    data = 66
    print(json.dumps(data))
    return json.dumps(data)

@app.route("/TChart1.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleTChart1Request():
    data = 66
    print(json.dumps(data))
    return json.dumps(data)

@app.route("/TChart7.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleTChart7Request():
    data = [66, 23, 52, 77, 37, 90]
    print(json.dumps(data))
    return json.dumps(data)


# @app.route("/purchase.json", methods=["GET", "POST"])
# @cross_origin(supports_credentials=True)
# def handlePurchaseRequest():
#     comment = [
#         {"carType": "兰博基尼", "price": "1万以上", "purchaseTarget": "装杯啊"},
#         {"carType": "兰博基尼", "price": "1万以上", "purchaseTarget": "装杯啊"},
#         {"carType": "兰博基尼", "price": "1万以上", "purchaseTarget": "装杯啊"},
#     ]
#     return json.dumps(comment)
# @app.route("/carSlaePrice.json", methods=["GET", "POST"])
# @cross_origin(supports_credentials=True)
# def handleCarSalePriceRequest():
#     mydata = [
#         {"AName": "甲车型"},
#         {"BName": "乙车型"},
#         {"time": ['一月', '二月', '三月', '四月', '五月', '六月']},
#         {"AData":[120, 132, 101, 134, 90, 230, 210]},
#         {"BData": [220, 182, 191, 234, 290, 330, 310]},
#     ]
#     return json.dumps(mydata)
# @app.route("/carSaleNumber.json", methods=["GET", "POST"])
# @cross_origin(supports_credentials=True)
# def handleCarSaleNumberRequest():
#     mydata = [
#         {"AName": "甲车"},
#         {"BName": "乙车"},
 #          {"time": ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']},
#         {"AData": [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3]},
#         {"BData": [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]},
#         {"totalData": [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]}
#     ]
#     return json.dumps(mydata)
# @app.route("/carSaleTime.json", methods=["GET", "POST"])
# @cross_origin(supports_credentials=True)
# def handleCarSaleTimeRequest():
#     mydata = [
#         {"AName": "甲车型"},
#         {"BName": "乙车型"},
#         {"time": ['一月', '二月', '三月', '四月', '五月', '六月']},
#         {"AData": [50, 40, 45, 60, 90, 75, 55]},
#         {"Bdata": [32, 23, 54, 45, 32, 67, 43]},
#     ]
#     return json.dumps(mydata)
app.run(port="5000")
# print(user.userDAO.getAllUser())


