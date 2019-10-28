import tele_bot_tools as tbt
from os import environ
from app import bot
import random
from tele_bot_tools import *
from app import db
from app import models
import time as sleeper
import datetime


@bot.message_handler(commands=['start'])
def hi_msg(message):
    poster(bot, message.chat.id, 'Кракен тут. Ссылка + сколько')

@bot.message_handler(commands=['time'])
def time(message):
    timeT = models.time.query.filter_by(Id=1).first() 
    value = datetime.datetime.fromtimestamp(timeT.Time+(3600*3))
    print(value.strftime('%H:%M:%S %d-%m-%Y '))
    poster(bot, message.chat.id, 'Я работал - '+value.strftime('%Y-%m-%d %H:%M:%S')+' - отстань!')

@bot.message_handler(content_types=['text'])
def any_messages(msg):
    message = msg.text
    try:
        int(message)
        u = models.messages.query.filter_by(id=msg.chat.id).first()
        u.amount = int(message)
        db.session.commit()
        try:
            url = u.url
            amount = u.amount
            
            if url.find('ribbble.com') > 0:
                pr = models.product(url=url,  amount= int(amount))
            elif url.find('reativemarket.com') > 0:
                pr = models.creprod(url=url,  amount= int(amount))
            db.session.add(pr)
            db.session.commit()

            poster(bot, msg.chat.id, 'Ща')
        except Exception as e:
            print(e)
            poster(bot, msg.chat.id, 'Сначала ссылку')

    except:
        if message.find('ribbble.com') > 0:
            try:
                models.product.query.filter_by(url=message).delete()
            except:
                pass
            try:
                models.messages.query.filter_by(id=msg.chat.id).delete()
            except:
                pass
            db.session.commit()
            u = models.messages(id=msg.chat.id, url=message)
            db.session.add(u)
            db.session.commit()
            sleeper.sleep(5)
            poster(bot, msg.chat.id, 'Сколько?')
        
        elif message.find('reativemarket.com') > 0:
            try:
                models.creprod.query.filter_by(url=message).delete()
            except:
                pass
            try:
                models.messages.query.filter_by(id=msg.chat.id).delete()
            except:
                pass
            db.session.commit()
            u = models.messages(id=msg.chat.id, url=message)
            db.session.add(u)
            db.session.commit()
            sleeper.sleep(5)
            poster(bot, msg.chat.id, 'Сколько?')

        else: 
            poster(bot, msg.chat.id, 'Давай заново!')

    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        pass