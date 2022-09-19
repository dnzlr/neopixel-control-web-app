# HOW TO RUN THIS SCRIPT
# nohup sudo python3 telegram_bot_led_control.py &

import telebot
from telebot import types
import yps_led as yl
from rpi_ws281x import *
import argparse
import time
import random
from multiprocessing import Process

# create a file called ".telegramToken.txt" and store your
# telegram token inside
# TODO(Y):explain how to retrieve the token
# read token from .telegramToken.txt file
f = open('.telegramToken.txt', 'r')
telegramToken = f.read().strip()
f.close()
bot = telebot.TeleBot(str(telegramToken))

# TODO(Y): Problem: Not able to effectively turn off this function yet!
@bot.message_handler(commands=['bunt', 'rb', 'rainbow', 'colors'])
def rainbow(message):
    glo.isAlive = True
    #p1 = Process(target=yl.rainbowCycle, args=(yl.ledObject,mybool==True))
    yl.rainbowCycle(yl.ledObject)
    #p1.start()
    #rainbowCycle(strip)

@bot.message_handler(commands=['off', 'k', 'kill'])
def off(message):
    yl.wheelOff()
    #yl.colorWipe(yl.ledObject, Color(0,0,0), 10)
    bot.reply_to(message, "Light off")

@bot.message_handler(commands=['onw', 'w', 'white'])
def on(message):
    yl.ypsCol(yl.ledObject, yl.WHITE)

@bot.message_handler(commands=['on', 'ww', 'warmwhite'])
def warmWhite(message):
    yl.ypsCol(yl.ledObject, yl.WARMWHITE)

@bot.message_handler(commands=['brightyellow', 'c', 'citrus'])
def citrus(message):
    yl.ypsCol(yl.ledObject, yl.YELLOW)

@bot.message_handler(commands=['green', 'g', 'weed', 'kush'])
def green(message):
    yl.ypsCol(yl.ledObject, yl.GREEN)

@bot.message_handler(commands=['red', 'r', 'sex'])
def red(message):
    yl.ypsCol(yl.ledObject, yl.RED)

@bot.message_handler(commands=['blue', 'b', 'sad'])
def blue(message):
    yl.ypsCol(yl.ledObject, yl.BLUE)

@bot.message_handler(commands=['yellow', 'y'])
def yellow(message):
    yl.ypsCol(yl.ledObject, yl.ORANGE)

@bot.message_handler(commands=['pink', 'p'])
def pink(message):
    yl.ypsCol(yl.ledObject, yl.PINK)

#@bot.message_handler(commands=['off', '0'])
#def off(message):
#    print("STOP THREADS = true")
#    yl.ypsCol(yl.OFF)

bot.infinity_polling()
