# if message.text == 'Гороскоп':
#     bot.send_message(message.from_user.id, "сейчас я расскажу тебе гороскоп на сегодня.")
#     keyboard = types.InlineKeyboardMarkup()
#     key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
#     keyboard.add(key_oven)
#     key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
#     keyboard.add(key_telec)
#     key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
#     keyboard.add(key_bliznecy)
#     key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
#     keyboard.add(key_rak)
#     key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
#     keyboard.add(key_lev)
#     key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
#     keyboard.add(key_deva)
#     key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
#     keyboard.add(key_vesy)
#     key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
#     keyboard.add(key_scorpion)
#     key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
#     keyboard.add(key_strelec)
#     key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
#     keyboard.add(key_kozerog)
#     key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
#     keyboard.add(key_vodoley)
#     key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
#     keyboard.add(key_ryby)
#     bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
#
#
#     @bot.callback_query_handler(func=lambda call: True)
#     def callback_worker(call):
#         if call.data == "zodiac":
#             msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
#                 second_2) + ' ' + random.choice(third)
#             bot.send_message(message.chat.id, msg, )
#
# elif message.text == "Создай свой ник":
#     bot.send_message(message.chat.id, text=get_nickname())
# elif message.text == "Анекдоты":
#     bot.send_message(message.chat.id, text=get_anekdot())
# elif message.text == "Показать лисичку":
#     contents = requests.get('https://randomfox.ca/floof').json()
#     urlCAT = contents['image']
#     bot.send_photo(message.chat.id, photo=urlCAT)








# dssfewrrwerrewfewfeds
