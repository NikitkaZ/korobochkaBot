import telebot
from telebot import types

bot = telebot.TeleBot("1792550174:AAFdzbCOAwflQsRuNKkZePXaDbY2EVC-qTE")

markup1 = types.InlineKeyboardMarkup()
markup1.add(types.InlineKeyboardButton('Инструкция', callback_data='instruction'))
markup1.add(types.InlineKeyboardButton('Расчёт стоимости', callback_data='cost'))
markup1.add(types.InlineKeyboardButton('Отзывы клиентов', url='https://t.me/BOX_ORDER_FEEDBACK'))

markup_ins = types.InlineKeyboardMarkup()
markup_ins.add(types.InlineKeyboardButton('Работа с POIZON', callback_data='instruction_1'))
markup_ins.add(types.InlineKeyboardButton('Выбор размера', callback_data='instruction_2'))
markup_ins.add(types.InlineKeyboardButton('Ссылка на товар', callback_data='instruction_3'))
markup_ins.add(types.InlineKeyboardButton('Назад', callback_data='markup_back_to_start'))

markup_cost = types.InlineKeyboardMarkup()
markup_cost.add(types.InlineKeyboardButton('Обувь', callback_data='markup_cost1'))
markup_cost.add(types.InlineKeyboardButton('Одежда', callback_data='markup_cost2'))
markup_cost.add(types.InlineKeyboardButton('Аксессуары', callback_data='markup_cost3'))
markup_cost.add(types.InlineKeyboardButton('Назад', callback_data='markup_back_to_start'))

markup_back = types.InlineKeyboardMarkup()
markup_back.add(types.InlineKeyboardButton('На главную', callback_data='markup_back_to_start'))
markup_back.add(types.InlineKeyboardButton('Назад', callback_data='markup_back_to_inst'))

markup_back2 = types.InlineKeyboardMarkup()
markup_back2.add(types.InlineKeyboardButton('На главную', callback_data='markup_back_to_start'))
markup_back2.add(types.InlineKeyboardButton('Назад', callback_data='markup_back_to_cost'))

photo1 = open('1i.png', 'rb')
photo2 = open('2i.png', 'rb')
photo3 = open('3i.png', 'rb')
photo4 = open('4i.png', 'rb')
photo5 = open('5i.png', 'rb')
photo6 = open('6i.png', 'rb')
photo7 = open('7i.png', 'rb')
photo8 = open('8i.png', 'rb')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
    bot.send_message(message.chat.id, f'Выбери необходимый раздел', reply_markup=markup1)


@bot.callback_query_handler(func=lambda call: True)
def main(message):
    if message.data == 'instruction':
        bot.send_message(message.message.chat.id, f'Что именно вы хотите узнать?', reply_markup=markup_ins)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Выбери необходимый раздел", reply_markup=None)
    elif message.data == 'cost':
        bot.send_message(message.message.chat.id, f'К какой категории относиться ваш товар?', reply_markup=markup_cost)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Выбери необходимый раздел", reply_markup=None)
    elif message.data == 'instruction_1':
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Что именно вы хотите узнать?", reply_markup=None)
        bot.send_photo(message.message.chat.id, open('1i.png', 'rb'))
        bot.send_message(message.message.chat.id,
                         f'Чтобы скачать приложение на IOS, перейдите в AppStore и в поиске введите Poizon')
        bot.send_photo(message.message.chat.id, open('2i.png', 'rb'))
        bot.send_message(message.message.chat.id,
                         f'Чтобы скачать приложение на Android, необходимо перейти по ссылке https://www.25pp.com/xiazai/6696712/history_v727/ и нажать на зелёную кнопку загрузки.')
        bot.send_message(message.message.chat.id,
                         'Для возможности выбирать размеры необходимо подтвердить номер телефона по смс-коду, иногда он приходит не с первой попытки (Это не обязательно, но если не подтверждать номер, то некоторые функции приложения будут недоступны).')
        bot.send_photo(message.message.chat.id, open('3i.png', 'rb'))
        bot.send_message(message.message.chat.id, """
        Интерфейс приложения:

1 - На нижней панели выбираем вторую слева кнопку. Это раздел магазина
2 - Поиск товара по названию модели или бренда
3 - Подборка товаров по вашим интересам
4 - Вкладка с обувью
""")
        bot.send_message(message.message.chat.id, f'Cледующее действие', reply_markup=markup_back)
    elif message.data == 'instruction_2':
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Что именно вы хотите узнать?", reply_markup=None)
        bot.send_photo(message.message.chat.id, open('4i.png', 'rb'))
        bot.send_message(message.message.chat.id,
                         f'Перейдите в карточку понравившегося товара и нажмите на бирюзовую кнопку.')
        bot.send_photo(message.message.chat.id, open('5i.png', 'rb'))
        bot.send_message(message.message.chat.id,
                         """1 - Размерная сетка по длине стопы (рекомендуем сверять размер именно по размеру стопы, т.к. размерные сетки у каждого бренда могут отличаться)

2 - Доступные к заказу размеры

3 - И их цена! Именно эту цену вводим при расчёте стоимости!


Важно: Смотрим цену на бирюзовой кнопке""")
        bot.send_photo(message.message.chat.id, open('6i.png', 'rb'))
        bot.send_message(message.message.chat.id,
                         """Размерная сетка

1 - Размер обуви в стандарте EU (именно в этом стандарте представлена обувь в приложении)

2 - Размер обуви по длине стопы""")
        bot.send_photo(message.message.chat.id, open('7i.png', 'rb'))
        bot.send_message(message.message.chat.id,
                         """Важное примечание:

1 - Мы НЕ сможем заказать товар, который имеет знак "приблизительно равно"

2 - Кнопка 95 отражает стоимость б/у товара (отличная возможность сэкономить для тех, кто не гонится за новыми вещами)""")
        bot.send_message(message.message.chat.id, f'Cледующее действие', reply_markup=markup_back)
    elif message.data == 'instruction_3':
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Что именно вы хотите узнать?", reply_markup=None)
        bot.send_photo(message.message.chat.id, open('8i.png', 'rb'))
        bot.send_message(message.message.chat.id,
                         """Ссылка на понравившийся товар:

Чтобы не было ошибок при оформлении заказа, советуем вместе со скрином товара отправлять и ссылку на товар)

Для этого в карточке товара нажимаем кнопку (1) и после кнопку (2)""")
        bot.send_message(message.message.chat.id, f'Cледующее действие', reply_markup=markup_back)
    elif message.data == 'markup_cost1':
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Обувь", reply_markup=None)
        bot.send_message(message.message.chat.id, f'Введите стоимость в ¥')
        bot.register_next_step_handler(message.message, process_text1)
    elif message.data == 'markup_cost2':
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Одежда", reply_markup=None)
        bot.send_message(message.message.chat.id, f'Введите стоимость в ¥')
        bot.register_next_step_handler(message.message, process_text2)
    elif message.data == 'markup_cost3':
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Аксессуары", reply_markup=None)
        bot.send_message(message.message.chat.id, f'Введите стоимость в ¥')
        bot.register_next_step_handler(message.message, process_text3)
    elif message.data == 'markup_back_to_inst':
        bot.send_message(message.message.chat.id, f'Что именно вы хотите узнать?', reply_markup=markup_ins)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Назад", reply_markup=None)
    elif message.data == 'markup_back_to_start':
        bot.send_message(message.message.chat.id, f'Выбери необходимый раздел', reply_markup=markup1)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Назад", reply_markup=None)
    elif message.data == 'markup_back_to_cost':
        bot.send_message(message.message.chat.id, f'К какой категории относиться ваш товар?', reply_markup=markup_cost)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message.message_id,
                              text="Назад", reply_markup=None)


def process_text1(message):
    cost = message.text
    if not cost.isdigit():
        bot.send_message(message.chat.id, f'Неверные данные')
        bot.send_message(message.chat.id, f'Введите число')
        bot.register_next_step_handler(message, process_text1)
    else:
        bot.send_message(message.chat.id, f'Полная стоимость товара:\n'
                                          f'{round(int(cost) * 1.1 * 13.2 + 1500)}₽')
        bot.send_message(message.chat.id, f'Для заказа напишите @yarchi1i или @Nik_z_z_z')
        bot.send_message(message.chat.id, f'Cледующее действие', reply_markup=markup_back2)


def process_text2(message):
    cost = message.text
    if not cost.isdigit():
        bot.send_message(message.chat.id, f'Неверные данные')
        bot.send_message(message.chat.id, f'Введите число')
        bot.register_next_step_handler(message, process_text1)
    else:
        bot.send_message(message.chat.id, f'Полная стоимость товара:\n'
                                          f'{round(int(cost) * 1.1 * 13.2 + 1200)}₽')
        bot.send_message(message.chat.id, f'Cледующее действие', reply_markup=markup_back2)


def process_text3(message):
    cost = message.text
    if not cost.isdigit():
        bot.send_message(message.chat.id, f'Неверные данные')
        bot.send_message(message.chat.id, f'Введите число')
        bot.register_next_step_handler(message, process_text1)
    else:
        bot.send_message(message.chat.id, f'Полная стоимость товара:\n'
                                          f'{round(int(cost) * 1.1 * 13.2 + 1000)}₽')
        bot.send_message(message.chat.id, f'Cледующее действие', reply_markup=markup_back2)


bot.polling(none_stop=True)
