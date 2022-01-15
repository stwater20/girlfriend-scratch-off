from flask import Flask, render_template,make_response
import random

app = Flask(__name__)

data=[
    {
        'item':"抱抱 10 秒",
        'count':10
    },
    {
        'item':"摸頭 10 秒",
        'count':10
    },
    {
        'item':"按摩 5 分鐘",
        'count':10
    },
    {
        'item':"巧克力 1 盒",
        'count':10
    }
]

count = len(data)
gifts = []
for i in range(0,count):
    for j in range(0,int(data[i]["count"])):
        gifts.append(data[i]["item"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/renew")
def renew():
    randnum = random.randint(0,len(gifts))
    response = make_response(gifts[randnum],200)
    return response
    