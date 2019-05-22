import tele_bot_tools as tbt
from os import environ
from app import bot
import random
                


@bot.message_handler(commands=['start'])
def hi_msg(message):
    pass
    
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data:
        pass