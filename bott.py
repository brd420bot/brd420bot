import telebot
from telebot import types

bot = telebot.TeleBot('1234736153:AAE81T6WeWC0cOTlAU6yKolDLcJg-2rCcxc')

@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="БЕРДЯНСК", callback_data="test")
    keyboard.add(callback_button)
    bot.send_message(message.chat.id, "ВАС ПРИВЕТСТВУЕТ АВТОМАТИЗИРОВАННЫЙ СЕРВИС ПРОДАЖ @brd420bot."
                                      "                                                                                "
                                      "                                                                                "
                                      "Тех. поддержка - @brd420oper."
                                      "                                                                                "
                                      "                                                                                "
                                      "ВЫБЕРИТЕ ГОРОД:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "test":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="1г шишки AMNEZIA🍁 HAZE 250грн", callback_data="mest")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="2г шишки AMNEZIA🍁 HAZE 500грн", callback_data="fest")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Марка НБОМе25🌠 180грн", callback_data="rest")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="АМФ⚡️ СУЛЬФАТ 1Г - 350ГРН", callback_data="qest")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="ДАЛЕЕ>>>", callback_data="next")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Выберите интересующий вас товар:", reply_markup=keyboard)
    if call.data == "next":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="💗💗💗Альфа PVP 0.5 250грн", callback_data="mast")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Methamphetamine hydrochloride 0.25г🧂 - 350грн", callback_data="fast")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="1гр. битая шиха🌿 АК47 230грн", callback_data="rast")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="💊ЭКСТАЗИ 2таблы - 600грн💊", callback_data="qast")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="ДАЛЕЕ>>>", callback_data="fext")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Выберите интересующий вас товар:", reply_markup=keyboard)
    if call.data == "fext":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="🍀🍀🍀Шишки OG KUSH 275грн", callback_data="messt")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="🌈LSD 220МКГ🌅 - 700грн", callback_data="fesst")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="🗯МЕФЕДРОН 0.5 350ГРН", callback_data="resst")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="MDMA🌟 в крист., 0.3 - 400грн", callback_data="qesst")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="ДАЛЕЕ>>>", callback_data="test")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Выберите интересующий вас товар:", reply_markup=keyboard)
    if call.data == "mest":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Слободка", callback_data="sasay")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="test")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "1г шишки AMNEZIA🍁 HAZE 250грн."
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "sasay":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="sasay")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="null")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "1г шишки AMNEZIA🍁 HAZE 250грн."
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Слободка"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "250грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "null":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="sasay")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "reset":
        bot.send_message(call.message.chat.id, "Заказ отменён, чтобы начать покупки заново напишите /start.")
    if call.data == "fest":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Коса", callback_data="sasaya")
        keyboard.add(callback_button)
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Военный городок", callback_data="sasayab")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="test")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "2г шишки AMNEZIA🍁 HAZE 500грн."
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "sasaya":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="sasaya")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="nulla")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "2г шишки AMNEZIA🍁 HAZE 500грн."
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Коса"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "500грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "sasayab":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="sasayab")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="nullb")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "2г шишки AMNEZIA🍁 HAZE 500грн."
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Военный городок"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "500грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "nulla":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="sasaya")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "nullb":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="sasayab")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "rest":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Центр", callback_data="nbom")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="test")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "Марка НБОМе25🌠 180грн"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "nbom":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="nbom")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="nulql")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "Марка НБОМе25🌠 180грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Центр"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "180грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "nulql":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="nbom")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "qest":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Коса", callback_data="sraka")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Центр", callback_data="sraka2")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="АКЗ", callback_data="sraka3")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="test")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар"
                                               "                                                                       "
                                               "АМФ⚡️ СУЛЬФАТ 1Г - 350ГРН "
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "sraka":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="sraka")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="anulla")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "АМФ⚡️ СУЛЬФАТ 1Г - 350ГРН"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Коса"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "350грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "sraka2":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="sraka2")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="anullb")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "АМФ⚡️ СУЛЬФАТ 1Г - 350ГРН"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Центр"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "350грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "sraka3":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="sraka3")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="anullc")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "АМФ⚡️ СУЛЬФАТ 1Г - 350ГРН"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "АКЗ"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "350грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "anulla":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="sraka")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "anullb":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="sraka2")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "anullc":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="sraka3")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "mast":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Стекловолокно", callback_data="alpha")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="next")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар"
                                               "                                                                       "
                                               "💗💗💗Альфа PVP 0.5 250грн"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "alpha":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="alpha")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="alphanull")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "💗💗💗Альфа PVP 0.5 250грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Стекловолокно"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "250грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "alphanull":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="alpha")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "fast":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Лиски", callback_data="liski")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="next")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "Methamphetamine hydrochloride 0.25г🧂 - 350грн"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "liski":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="liski")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="otmena")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "Methamphetamine hydrochloride 0.25г🧂 - 350грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Лиски"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "350грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "otmena":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="liski")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "rast":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Центр", callback_data="centr")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Слободка", callback_data="slobodka")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="next")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "1гр. битая шиха🌿 АК47 230грн"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "slobodka":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="slobodka")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="pidor1")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "1гр. битая шиха🌿 АК47 230грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Слободка"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "230грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "pidor1":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="slobodka")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "centr":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="centr")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="pidor")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "1гр. битая шиха🌿 АК47 230грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Центр"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "230грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "pidor":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="centr")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "qast":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Лиски", callback_data="eshki")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Слободка", callback_data="ssasay")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="next")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "💊ЭКСТАЗИ 2таблы - 600грн💊"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "ssasay":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="ssasay")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="popa1")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "💊ЭКСТАЗИ 2таблы - 600грн💊"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Слободка"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "600грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "popa1":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="ssasay")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "eshki":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="eshki")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="popa")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "💊ЭКСТАЗИ 2таблы - 600грн💊"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Лиски"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "600грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "popa":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="eshki")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "messt":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Центр", callback_data="shish")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Коса", callback_data="shish2")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="АКЗ", callback_data="shish3")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="fext")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "🍀🍀🍀Шишки OG KUSH 275грн"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "shish":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="shish")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="pops")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "🍀🍀🍀Шишки OG KUSH 275грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Центр"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "275грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "pops":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="shish")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "shish2":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="shish2")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="pops1")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "🍀🍀🍀Шишки OG KUSH 275грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Коса"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "275грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "pops1":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="shish2")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "shish3":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="shish3")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="sqs")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "🍀🍀🍀Шишки OG KUSH 275грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "АКЗ"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "275грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "sqs":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="shish3")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "fesst":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Колония", callback_data="acid")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="fext")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "🌈LSD 220МКГ🌅 - 700грн"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "acid":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="acid")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="ssss")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "🌈LSD 220МКГ🌅 - 700грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Колония"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "700грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "ssss":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="acid")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "resst":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Центр", callback_data="mef")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="fext")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "🗯МЕФЕДРОН 0.5 350ГРН"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "mef":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="mef")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="qqq")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "🗯МЕФЕДРОН 0.5 350ГРН"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Центр"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "350грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "qqq":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="mef")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)
    if call.data == "qesst":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Коса", callback_data="mdma")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Назад к ассортименту", callback_data="fext")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы выбрали товар "
                                               "                                                                       "
                                               "MDMA🌟 в крист., 0.3 - 400грн"
                                               "                                                                       "
                                               "Выберите район:", reply_markup=keyboard)
    if call.data == "mdma":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Проверить оплату", callback_data="mdma")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="wert")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Забронирован заказ на 45 минут на товар:"
                                               "                                                                       "
                                               "MDMA🌟 в крист., 0.3 - 400грн"
                                               "                                                                       "
                                               "Район:"
                                               "                                                                       "
                                               "Коса"
                                               "                                                                       "
                                               "К оплате:"
                                               "                                                                       "
                                               "400грн"
                                               "                                                                       "
                                               "Кошелёк EASYPAY:"
                                               "                                                                       "
                                               "13418581", reply_markup=keyboard)
    if call.data == "wert":
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Вернуться к оплате", callback_data="mdma")
        keyboard.add(callback_button)
        callback_button = types.InlineKeyboardButton(text="Отменить заказ", callback_data="reset")
        keyboard.add(callback_button)
        bot.send_message(call.message.chat.id, "Вы действительно хотите отменить заказ?"
                                               "                                                                       "
                                               "При отмене трёх заказов менее чем за 24 часа, "
                                               "ваш аккаунт будет заблокирован", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)
