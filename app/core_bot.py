import tele_bot_tools as tbt
from os import environ
from app import bot
import random
from tele_bot_tools import *
from app import db
from app import models


@bot.message_handler(commands=['start'])
def hi_msg(message):
    poster(bot, message.chat.id, 'Кракен тут. Ссылка + сколько')

@bot.message_handler(content_types=['text'])
def any_messages(msg):
    message = msg.text
    try:
        int(message)
        poster(bot, msg.chat.id, 'Ща')
    except:
        if message.find('ribbble.com') > 0:
            models.messages.query.filter_by(id=1).delete()
            db.session.commit()
            u = models.messages(id=1, url=message)
            db.session.add(u)
            db.session.commit()
            poster(bot, msg.chat.id, 'Сколько?')
        else:
            poster(bot, msg.chat.id, 'Давай заново!')

    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        pass