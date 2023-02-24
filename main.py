import os
import re
import sqlite3
import telebot
from dotenv import load_dotenv

load_dotenv()

con = sqlite3.connect('db.sqlite3', check_same_thread=False)
cur = con.cursor()

API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)

def db_table_user(user_id: int, user_name: str):
    """Creates a User table in the database and fills it with values.
    """
    cur.execute('CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, user_name TEXT)')
    cur.execute('INSERT INTO users (user_id, user_name) VALUES (?, ?);', (user_id, user_name))
    con.commit()

def db_table_voice(voice_id: str, description: str, user_id: int):
    """Creates a Voice table (related with the User table) in the database
    and fills it with values.
    """
    cur.execute('CREATE TABLE IF NOT EXISTS voices(voice_id TEXT NOT NULL, description TEXT NOT NULL, user_id INTEGER NOT NULL, FOREIGN KEY(user_id) REFERENCES users(user_id))')
    cur.execute('INSERT INTO voices (voice_id, description, user_id) VALUES (?, ?, ?);', (voice_id, description, user_id))
    con.commit()

@bot.message_handler(commands=['start'], content_types=['text'])
def start_message(message):
    """If the user is already in the database, the bot greets him.
    If the user is absent, the bot asks for his name, and then
    initializes an entry into the database.
    """
    us_id = message.from_user.id
    try:
        us_name = cur.execute('SELECT user_name FROM users WHERE user_id = ? AND user_name NULL;', (us_id,)).fetchone()
    except:
        bot.send_message(message.chat.id, 'Welcome!\nWhat is your name')
        bot.register_next_step_handler(message, add_user_or_none)
    else:
        us_name = re.sub('[^A-Za-z0-9]+', '', str(us_name))
        bot.send_message(message.chat.id, f'Welcome, {us_name}')

def add_user_or_none(message):
    """Bot gets user's name and writes user's data into the database.
    Then greets him.
    """
    us_id = message.from_user.id
    us_name = message.text
    if us_name is None:
        bot.send_message(message.chat.id, 'Please, introduce yourself')
        bot.register_next_step_handler(message, add_user_or_none)
        return
    db_table_user(user_id=us_id, user_name=us_name)
    bot.send_message(message.from_user.id, f'Hi, {us_name}')


@bot.message_handler(content_types=['voice'])
def voice_processing(message):
    """Bot converts user's voice message to a wav-format 16kHz.
    Saves it to the folder. And relates the voice to the user in the database.
    """
    filename = str(message.voice.file_id)
    filename_full = './voice/' + filename + '.ogg'
    filename_full_converted = './voice/' + filename + '.wav'
    file_info = bot.get_file(message.voice.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open(filename_full, 'wb') as new_file:
        new_file.write(downloaded_file)
    os.system(f'ffmpeg -i {filename_full} -ac 1 -ar 16000 {filename_full_converted}')
    os.remove(filename_full)

    # try:
    #     position = cur.execute('SELECT COUNT(description) FROM voices WHERE voice_id = ?;', (filename,))
    # except:
    #     position = 1
    # else:
    #     if position == 0:
    #         position += 1
    # finally:
    #     user_id = message.from_user.id
    #     description = f'audio_message_{position}'
    #     db_table_voice(voice_id=filename, description=description, user_id=user_id)


bot.polling(none_stop=True, interval=0)
