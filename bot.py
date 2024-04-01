from telegram import Bot, Update, request
from telegram.ext import Updater, CommandHandler
from maim import convert_to_sound
from pathlib import Path
from urllib.request import Request
from sqlalchemy import true
from zmq import CONNECT_TIMEOUT 
from token.env import Token

def changer_of_lang():
    pass

def main():
    req= request(connect_timeout= 0.5)
    my_bot= Bot(token= Token, request=req)
    updater= Updater(bot= my_bot, use_context = True)
    dp= Updater.dispatcher 

#commands
    cmd=[("change_language","change language from the default one")]
    my_bot.set_my_commands(cmd)
    dp.add_handler(CommandHandler(chandge_language, changer_of_lang))
    updater.start_polling()
    updater.idle()
    

if __name__=="__main__":
    main()

