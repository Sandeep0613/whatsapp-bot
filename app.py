from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

cluster = MongoClient("mongodb+srv://Sandeep:Khushbo0@cluster0.w8bas.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Foodonaclick"]
users = db["users"]

app = Flask(__name__)
@app.route('/', methods=['get', "post"])
def reply():
    text = request.form.get("message")
    number = request.form.get("sender")
    res = {"reply": ""}
    user = users.find_one({"number": number})
    if bool(user) == False:
        res["reply"] += '\n' + ("Please visit the URL \n foodonaclick.in \n to place order 😊")
        users.insert_one({"number": number, "status": "main", "messages": []})
    else:
        res["reply"] += '\n' + ("Please visit the URL \n foodonaclick.in \n to place order 😊")
        users.update_one({"number": number}, {"$push": {"messages": {"text": text, "date": datetime.now()}}})
    return str(res)

if __name__ == "__main__":
         app.run(port=5000)
