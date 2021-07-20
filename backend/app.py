from flask import Flask, request
from flask_cors import cross_origin, CORS
import json

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

@app.route("/user.json", methods=["get", "post"])
@cross_origin(supports_credentials=True)
def handleForm():
    myForm = request.form
    result = myForm.to_dict()
    if(result["username"] == "rjx" and result["password"] == "123456"):
        return "success"
    else:
        return "fail"


@app.route("/SellingData.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleSellingDataRequest():
    sellingData = [
        {"name": "北京市", "value": 40000},
        {"name": "山西省", "value": 30000},
        {"name": "内蒙古自治区", "value": 5000},
        {"name": "青海省", "value": 7000},
        {"name": "河北省", "value": 25000},
    ]
    return json.dumps(sellingData)


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


@app.route("/price.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handlePriceRequest():
    price = [
        {"value": "选项1", "label": "1万以下"},
        {"value": "选项2", "label": "1万到5万"},
        {"value": "选项3", "label": "5万到10万"},
        {"value": "选项4", "label": "10万到20万"},
        {"value": "选项5", "label": "20万到50万"},
        {"value": "选项6", "label": "50万到100万"},
        {"value": "选项7", "label": "100万以上"},
    ]
    return json.dumps(price)


@app.route("/comment.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handleCommentRequest():
    comment = [
        {"carType": "兰博基尼", "userComment": "不错，挺好"},
        {"carType": "兰博基尼", "userComment": "不错，挺好"},
        {"carType": "兰博基尼", "userComment": "不错，挺好"},
    ]
    return json.dumps(comment)


@app.route("/purchase.json", methods=["GET", "POST"])
@cross_origin(supports_credentials=True)
def handlePurchaseRequest():
    comment = [
        {"carType": "兰博基尼", "price": "100万以上", "purchaseTarget": "装杯啊"},
        {"carType": "兰博基尼", "price": "100万以上", "purchaseTarget": "装杯啊"},
        {"carType": "兰博基尼", "price": "100万以上", "purchaseTarget": "装杯啊"},
    ]
    return json.dumps(comment)


app.run(port="5000")
