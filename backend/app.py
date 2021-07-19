from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS

app = Flask(__name__,static_folder="http",static_url_path="/pages")
CORS(app, supports_credentials=True)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, motherfuckdasdasder!</p>"


#router
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

























app.run(port="5000")
