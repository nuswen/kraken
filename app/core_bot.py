import tele_bot_tools as tbt
from os import environ
from app import bot
import random
from tele_bot_tools import *
from app import db
from app import models
import time


@bot.message_handler(commands=['start'])
def hi_msg(message):
    poster(bot, message.chat.id, 'Кракен тут. Ссылка + сколько')

@bot.message_handler(content_types=['text'])
def any_messages(msg):
    message = msg.text
    try:
        int(message)
        u = models.messages(id=2, url=message)
        db.session.add(u)
        db.session.commit()
        try:
            u = models.messages.query.filter_by(id=1).first()
            url = u.url
            u = models.messages.query.filter_by(id=2).first()
            amount = u.url

            pr = models.Product(Url=url, Amount=amount)
            db.session.add(pr)
            #db.session.commit()

            poster(bot, msg.chat.id, 'Ща')
        except Exception as e:
            poster(bot, msg.chat.id, e)#'Сначала ссылку')

    except Exception as e:
        if message.find('ribbble.com') > 0:
            models.messages.query.filter_by(id=1).delete()
            models.messages.query.filter_by(id=2).delete()
            db.session.commit()
            u = models.messages(id=1, url=message)
            db.session.add(u)
            db.session.commit()
            time.sleep(5)
            poster(bot, msg.chat.id, 'Сколько?')
        else:
            poster(bot, msg.chat.id, 'Давай заново!')

    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        pass