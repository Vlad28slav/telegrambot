import telebot
from telebot import types
from gtts import gTTS
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.getenv("Token")
bot= telebot.TeleBot(Token)


language = None
tld = None

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(commands=['change_language'])
def change_language(message):

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("English (Australia)", callback_data="Australia")
    button2 = types.InlineKeyboardButton("English (United States)", callback_data="United States")
    keyboard.add(button1, button2)
    bot.send_message(message.chat.id, "Change a language to:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):

    if call.data == "Australia":
        global language, tld
        language = "en"
        tld ="com.au"
        bot.send_message(call.message.chat.id, "You changed language to English (Australia)")

    if call.data == "United States":
        global language, tld
        language = "en"
        tld ="us"
        bot.send_message(call.message.chat.id, "You changed language to English (United States)")




language == "en"
tld == "com.au"

@bot.message_handler(func=lambda message: True)
def convert_and_reply(message):
    text_to_convert= message.text
    tts = gTTS(text_to_convert, lang= language, tld=tld)
    sound = 'sound.ogg'
    tts.save(sound)
    voice = open('sound.ogg', 'rb')
    bot.send_voice(chat_id= message.chat.id, voice= voice)


bot.infinity_polling()