import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ.get('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, для команд кнопок нажми /button, для просмотра исходного кода нажми /code')

@bot.message_handler(commands=['code'])
def code_message(message):
    bot.send_message(message.chat.id, 'https://github.com/EgorLiutov22/telegram_bot')


@bot.message_handler(commands=['button'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Селфи из школы")
    markup.add(item1)
    item2 = types.KeyboardButton("Селфи сейчас")
    markup.add(item2)
    item3 = types.KeyboardButton("О увлечении")
    markup.add(item3)
    item4 = types.KeyboardButton("Что такое GPT")
    markup.add(item4)
    item5 = types.KeyboardButton("SQL vs NoSQL")
    markup.add(item5)
    item6 = types.KeyboardButton("История первой любви")
    markup.add(item6)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    chat_id = message.chat.id
    match message.text:
        case "Селфи из школы":
            send_photo(chat_id, '../media/school.jpg')
        case "Селфи сейчас":
            send_photo(chat_id, '../media/now.jpg')
        case "О увлечении":
            send_text(chat_id, '../media/hobby.txt')
        case "Что такое GPT":
            send_audio(chat_id, '../media/gpt.ogg')
        case "SQL vs NoSQL":
            send_audio(chat_id, '../media/sql.ogg')
        case "История первой любви":
            send_audio(chat_id, '../media/love.ogg')

def send_photo(chat_id, file):
    with open(file) as f:
        bot.send_photo(chat_id, f)

def send_text(chat_id, file):
    with open(file, encoding='utf-8') as f:
        bot.send_message(chat_id, f.readline())

def send_audio(chat_id, file):
    with open(file) as f:
        bot.send_voice(chat_id, f)



bot.infinity_polling()
