import telebot
from telebot import types
from gtts import gTTS
from dotenv import load_dotenv
import os

load_dotenv()
Token = os.getenv("Token")
bot= telebot.TeleBot(Token)




language = "en"
tld = "com.au"

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey! Hows it going?")


@bot.message_handler(commands=['change_language'])
def change_language(message):

    keyboard = types.InlineKeyboardMarkup()

    button1 = types.InlineKeyboardButton("English (United Kingdom)", callback_data="England")
    button2 = types.InlineKeyboardButton("English (United States)", callback_data="United States")
    button3 = types.InlineKeyboardButton("French (Canada)", callback_data="Canada")
    button4 = types.InlineKeyboardButton("French (France)", callback_data="France")
    button5 = types.InlineKeyboardButton("Portuguese (Brazil)", callback_data="Brazil")
    button6 = types.InlineKeyboardButton("Portuguese (Portugal)", callback_data="Portugal")
    button7 = types.InlineKeyboardButton("Spanish (Mexico)", callback_data="Mexico")
    button8 = types.InlineKeyboardButton("Spanish (Spain)", callback_data="Spain")

    keyboard.add(button1, button2, button3, button4, button5, button6, button7, button8)
    bot.send_message(message.chat.id, "Change language to:", reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    global language, tld

    if call.data == "England":
        language = "en"
        tld ="co.uk"
        bot.send_message(call.message.chat.id, "You changed language to English (Great Britan)")

    if call.data == "United States":
        language = "en"
        tld ="us"
        bot.send_message(call.message.chat.id, "You changed language to English (United States)")

    if call.data == "Canada":
        language = "fr"
        tld ="ca"
        bot.send_message(call.message.chat.id, "You changed language to French (Canada)")
    
    if call.data == "France":
        language = "fr"
        tld ="fr"
        bot.send_message(call.message.chat.id, "You changed language to French (France)")
    
    if call.data == "Brazil":
        language = "pt"
        tld ="com.br"
        bot.send_message(call.message.chat.id, "You changed language to Portuguese (Brazil))")
    
    if call.data == "Portugal":
        language = "pt"
        tld ="pt"
        bot.send_message(call.message.chat.id, "You changed language to Portuguese (Portugal)")
    
    if call.data == "Mexico":
        language = "es"
        tld ="com.mx"
        bot.send_message(call.message.chat.id, "You changed language to Spanish (Mexico)")
    
    if call.data == "Spain":
        language = "es"
        tld ="es"
        bot.send_message(call.message.chat.id, "You changed language to Spanish (Spain)")




@bot.message_handler(func=lambda message: True)
def convert_and_reply(message):
    text_to_convert= message.text
    tts = gTTS(text_to_convert, lang= language, tld=tld)
    sound = 'sound.ogg'
    tts.save(sound)
    voice = open('sound.ogg', 'rb')
    bot.send_voice(chat_id= message.chat.id, voice= voice)


bot.infinity_polling()