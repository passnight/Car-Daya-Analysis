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


app.run(port="5000")
