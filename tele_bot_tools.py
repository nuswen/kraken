from telebot import types

def poster(bot, chat_id, text, buttons=None, ed=False, message_id=None):
    if buttons:
        if ed:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text, reply_markup=keyboarder(buttons))
        else:
            bot.send_message(chat_id, text, reply_markup=keyboarder(buttons))
    else:
        if ed:
            bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=text)
        else:
            bot.send_message(chat_id, text)


def keyboarder(keys):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    for key in keys:
        keyboard.add(types.KeyboardButton(text=key))
    return keyboard


def get_phone_number(bot, chat_id, text):
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_phone = types.KeyboardButton(text="Отправить номер телефона", request_contact=True)
    keyboard.add(button_phone)