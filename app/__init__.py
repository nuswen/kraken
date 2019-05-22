from os import environ
import telebot
from flask import Flask, request

bot = telebot.TeleBot(environ['token'])

app = Flask(__name__)

from app import core_bot

@app.route("/"+environ['token'], methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


bot.remove_webhook()
bot.set_webhook(url=environ['app_url']+environ['token'])
app.run(host="0.0.0.0", port=environ.get('PORT', 5000))