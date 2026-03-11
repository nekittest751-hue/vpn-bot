from flask import Flask
import threading
import requests
import time
import json

config = json.load(open("config.json"))

TOKEN = config["8797991331:AAHqq6Xm-uhj-_Rbom6mrjCgbqAXW_JB2vc"]
API = "https://api.telegram.org/bot"+TOKEN

app = Flask(__name__)

def send(chat,text):

    requests.post(API+"/sendMessage",json={
        "chat_id":chat,
        "text":text
    })

def bot():

    offset=0

    while True:

        try:

            r=requests.get(API+"/getUpdates",params={"offset":offset})
            data=r.json()

            for u in data["result"]:

                offset=u["update_id"]+1

                chat=u["message"]["chat"]["id"]
                text=u["message"].get("text","")

                if text=="/start":

                    send(chat,"🚀 Kirieshka VPN")
                    send(chat,"🆓 /trial")
                    send(chat,"💳 /buy")

        except Exception as e:

            print(e)

        time.sleep(2)

@app.route("/")
def home():
    return "VPN BOT WORKING"

threading.Thread(target=bot).start()

app.run(host="0.0.0.0",port=10000)