import os
import sqlite3
import telebot
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')
name = ''

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'], content_types=['text'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome!\nWhat is your name')
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    global name
    name=message.text
    bot.send_message(message.from_user.id, f'Hi, {name}')

bot.polling(none_stop=True, interval=0)
