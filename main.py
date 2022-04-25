import random
import bs4
import requests
import telebot
from telebot import types
from mg import get_map_cell

bot = telebot.TeleBot('5145230333:AAH-IggKJMLgic6NvoLvSxqriBGWTMadJqM')
first = ["Год для вас будет наполнен сюрпризами. Все они будут приятными, поэтому опасаться их не стоит",
         "Вы откроете в себе скрытые резервы, что позволит решиться на самые безумные поступки."]
second = ["Сейчас удачное время для признания в любви. Вам ответят взаимностью", "Счастье уже стоит за дверью."]
second_2 = [
    "Приготовьтесь, что получаемые вами результаты, успех в делах и яркие отношения с любимыми могут стать предметом зависти",
    "Невозможно отвести глаз от твоей красоты!"]
third = ["Невозможно отвести глаз от твоей красоты!", "Больше нет таких умных и проницательных девушек."]

cols, rows = 8, 8

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(telebot.types.InlineKeyboardButton('←', callback_data='left'),
             telebot.types.InlineKeyboardButton('↑', callback_data='up'),
             telebot.types.InlineKeyboardButton('↓', callback_data='down'),
             telebot.types.InlineKeyboardButton('→', callback_data='right'))

maps = {}


def get_map_str(map_cell, player):
    map_str = ""
    for y in range(rows * 2 - 1):
        for x in range(cols * 2 - 1):
            if map_cell[x + y * (cols * 2 - 1)]:
                map_str += "⬛"
            elif (x, y) == player:
                map_str += "🔴"
            else:
                map_str += "⬜"
        map_str += "\n"

    return map_str


# ----------------------------------------------------------------------
@bot.message_handler(commands=["start"])
def start(message, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Создай свой ник')
    item2 = types.KeyboardButton('Гороскоп')
    item3 = types.KeyboardButton('Анекдоты')
    item4 = types.KeyboardButton('Показать лисичку')
    item5 = types.KeyboardButton('Игра')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Привет,{0.first_name}!'.format(message.from_user), reply_markup=markup)



@bot.message_handler(content_types=['text'])

def play_message(message):
    if message.text == "Игра":
        cols, rows = 8, 8

        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(telebot.types.InlineKeyboardButton('←', callback_data='left'),
                     telebot.types.InlineKeyboardButton('↑', callback_data='up'),
                     telebot.types.InlineKeyboardButton('↓', callback_data='down'),
                     telebot.types.InlineKeyboardButton('→', callback_data='right'))
        map_cell = get_map_cell(cols, rows)

        user_data = {
            'map': map_cell,
            'x': 0,
            'y': 0
            }

        maps[message.chat.id] = user_data

        bot.send_message(message.from_user.id, get_map_str(map_cell, (0, 0)), reply_markup=keyboard)
    elif message.text == 'Гороскоп':
        bot.send_message(message.from_user.id, "сейчас я расскажу тебе гороскоп на сегодня.")
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "zodiac":
                msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
                    second_2) + ' ' + random.choice(third)
                bot.send_message(message.chat.id, msg, )

    elif message.text == "Создай свой ник":
        bot.send_message(message.chat.id, text=get_nickname())
    elif message.text == "Анекдоты":
        bot.send_message(message.chat.id, text=get_anekdot())
    elif message.text == "Показать лисичку":
        contents = requests.get('https://randomfox.ca/floof').json()
        urlCAT = contents['image']
        bot.send_photo(message.chat.id, photo=urlCAT)



@bot.callback_query_handler(func=lambda call: True)
def callback_func(query):
    user_data = maps[query.message.chat.id]
    new_x, new_y = user_data['x'], user_data['y']

    if query.data == 'left':
        new_x -= 1
    if query.data == 'right':
        new_x += 1
    if query.data == 'up':
        new_y -= 1
    if query.data == 'down':
        new_y += 1

    if new_x < 0 or new_x > 2 * cols - 2 or new_y < 0 or new_y > rows * 2 - 2:
        return None
    if user_data['map'][new_x + new_y * (cols * 2 - 1)]:
        return None

    user_data['x'], user_data['y'] = new_x, new_y

    if new_x == cols * 2 - 2 and new_y == rows * 2 - 2:
        bot.edit_message_text(chat_id=query.message.chat.id,
                              message_id=query.message.id,
                              text="Вы выиграли")
        return None

    bot.edit_message_text(chat_id=query.message.chat.id,
                          message_id=query.message.id,
                          text=get_map_str(user_data['map'], (new_x, new_y)),
                          reply_markup=keyboard)


# -----------------------------------------------------------------------
def get_anekdot():
    array_anekdots = []
    req_anek = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(req_anek.text, "html.parser")
    result_find = soup.select('.anekdot_text')
    for result in result_find:
        array_anekdots.append(result.getText().strip())
    return array_anekdots[0]


bot.polling(none_stop=True, interval=0)


def get_nickname():
    array_names = []
    req_names = requests.get("https://ru.nickfinder.com")
    soup = bs4.BeautifulSoup(req_names.text, "html.parser")
    result_find = soup.findAll(class_='one_generated_variant vt_df_bg')
    for result in result_find:
        array_names.append(result.getText())
    return array_names[0]


bot.polling(none_stop=True, interval=0)

print()
