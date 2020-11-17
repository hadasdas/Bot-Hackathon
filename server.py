from flask import Flask, Response, request
import requests
from tele_bot import bot_flow
from config import TOKEN, TELEGRAM_INIT_WEBHOOK_URL


app = Flask(__name__)

requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/message', methods=["POST"])
def handle_message():
    req = request.get_json()
    chat_id = req['message']['chat']['id']
    text = str(req['message']['text'])
    bot_answer = bot_flow(text)
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                 .format(TOKEN, chat_id, bot_answer))
    return Response("success")
