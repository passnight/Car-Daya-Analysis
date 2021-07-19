from flask import Flask, request, jsonify
from flask.cors import cross_origin
app = Flask("app", static_folder="backend/http", static_url_path="/pages")

@app.route("/index.html") #controller 
def helloWeb():
    return "<font color=red>fuck you </font>"
@app.route("/form.html")
@cross_origin(supports_credentials=True)
def handleForm():
    myForm = request.form
    myData = myForm.to_dict()
    print(myData["username"])
    print(myData["password"])
    return "<h1>okk</h1> {myData['username']}"
app.run()
