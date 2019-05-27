from os import environ
import telebot
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

bot = telebot.TeleBot(environ['token'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
db = SQLAlchemy(app)

from app import core_bot, models

@app.route("/"+environ['token'], methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return ("!"), 200

@app.route("/zenno/", methods=['POST'])
def zen():
    ur = models.messages.query.filter_by(id=1).first()
    am = models.messages.query.filter_by(id=2).first()
    re = ur+';'+am
    return (re), 200

bot.remove_webhook()
bot.set_webhook(url=environ['app_url']+environ['token'])
app.run(host="0.0.0.0", port=environ.get('PORT', 5000))