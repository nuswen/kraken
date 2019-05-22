import tele_bot_tools as tbt
from os import environ
from app import bot
import random
from tele_bot_tools import *
                


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
        if message.find('dribbble.com') > 0:
            poster(bot, msg.chat.id, 'Сколько?')
        else:
            poster(bot, msg.chat.id, 'Давай заново!')

    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        pass