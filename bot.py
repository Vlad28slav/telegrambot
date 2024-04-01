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
def echo_all(message):
	bot.reply_to(message, message.text)


bot.infinity_polling()