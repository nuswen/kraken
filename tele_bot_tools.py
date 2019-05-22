from telebot import types


def order_row_keyboard(keys):
    markup = types.ReplyKeyboardMarkup()
    for key in keys:
        markup.row(key)
    return markup
