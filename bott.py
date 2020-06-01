import telebot
from telebot import types

bot = telebot.TeleBot('1234736153:AAE81T6WeWC0cOTlAU6yKolDLcJg-2rCcxc')

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="БЕРДЯНСК", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "ВАС ПРИВЕТСТВУЕТ НАШ СЕРВИС ПРОДАЖ. ВЫБЕРИТЕ ГОРОД", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "test":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="МАМА", callback_data="mest")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="ПАПА", callback_data="fest")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "ВЫБЕРИТЕ ТОВАР", reply_markup=keyboard)
    if call.data == "mest":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="заплатить", callback_data="fest")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "ЭТО ШВЫР НЕ ПЛАТИТЕ ЕМУ ДЕНЬГИ", reply_markup=keyboard)
    if call.data == "fest":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="заплатить", callback_data="fest")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "ЭТО ШВЫР НЕ ПЛАТИТЕ ЕМУ ДЕНЬГИ", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)
