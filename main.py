import os
import sqlite3
import telebot
from dotenv import load_dotenv

load_dotenv()

con = sqlite3.connect('db.sqlite', check_same_thread=False)
cur = con.cursor()

def db_table_val(user_id: int, user_name: str):
    cur.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, user_name TEXT);')
    cur.execute('INSERT INTO users (user_id, user_name) VALUES (?, ?)', (user_id, user_name))
    con.commit()

API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'], content_types=['text'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome!\nWhat is your name')
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    us_id = message.from_user.id
    us_name=message.text
    bot.send_message(message.from_user.id, f'Hi, {us_name}')

    db_table_val(user_id=us_id, user_name=us_name)


bot.polling(none_stop=True, interval=0)
