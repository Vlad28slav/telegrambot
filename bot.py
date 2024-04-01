import telebot
from maim import convert_to_sound
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.getenv("Token")
bot= telebot.TeleBot(Token)

@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(func=lambda message: True)
def convert_and_reply(message):
    text_to_convert= message.text
    convert_to_sound(text_to_convert)
    voice = open('sound.ogg', 'rb')
    bot.send_voice(chat_id= message.chat.id, voice= voice)


bot.infinity_polling()