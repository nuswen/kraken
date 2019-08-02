from os import environ
import telebot
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

bot = telebot.TeleBot(environ['token'])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ['DATABASE_URL']
db = SQLAlchemy(app)

from app import core_bot, models

@app.route("/"+environ['token'], methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return ("!"), 200

@app.route("/zenno/", methods=['GET'])
def zen():
    allPosts = models.product.query.all()
    j = {'Post':[]}
    for p in allPosts:
        j['Post'].append({'Url':p.url, 'Amount':p.amount})
    
    reText = json.dumps(j)
    return (reText), 200

@app.route("/prdct/", methods=['POST'])
def prdct_pst():
    fu = json.loads(request.stream.read().decode("utf-8"))
    for i in fu:
        fPosts = models.product.query.filter_by(url=i).first()
        fPosts.amount = fPosts.amount - 1
        if fPosts.amount <= 0:
            models.messages.query.filter_by(url=i).delete()
            db.session.commit()
        else:
            db.session.add(fPosts)
            db.session.commit()

    return ('ok'), 200

bot.remove_webhook()
bot.set_webhook(url=environ['app_url']+environ['token'])
app.run(host="0.0.0.0", port=environ.get('PORT', 5000))