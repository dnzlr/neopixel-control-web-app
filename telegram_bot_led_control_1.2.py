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

bot = telebot.TeleBot("yourToken")

p1 = Process(target=yl.rainbowCycle, args=(yl.pixels,))
#p1 = Process(target=rainbowCycle, args=strip)

@bot.message_handler(commands=['bunt', 'rb', 'rainbow', 'colors'])
def rainbow(message):
    glo.isAlive = True
    #p1 = Process(target=yl.rainbowCycle, args=(yl.pixels,mybool==True))
    yl.rainbowCycle(yl.pixels)
    #p1.start()
    #rainbowCycle(strip)

@bot.message_handler(commands=['off', 'k', 'kill'])
def off(message):
    yl.wheelOff()
    print("KILL PROCESS")
    yl.colorWipe(yl.pixels, Color(0,0,0), 10)
    bot.reply_to(message, "Light off")

@bot.message_handler(commands=['onw', 'w', 'white'])
def on(message):
    if p1.is_alive():
        p1.terminate()
        p1.kill()
    yl.ypsCol(yl.pixels, yl.WHITE)

@bot.message_handler(commands=['on', 'ww', 'warmwhite'])
def warmWhite(message):
    if p1.is_alive():
        p1.terminate()
        p1.kill()
    yl.ypsCol(yl.pixels, yl.WARMWHITE)

@bot.message_handler(commands=['brightyellow', 'c', 'citrus'])
def citrus(message):
    if p1.is_alive():
        p1.terminate()
        p1.kill()
    yl.ypsCol(yl.pixels, yl.YELLOW)

@bot.message_handler(commands=['green', 'g', 'weed', 'kush'])
def green(message):
    if p1.is_alive():
        p1.terminate()
        p1.kill()
    yl.ypsCol(yl.pixels, yl.GREEN)

@bot.message_handler(commands=['red', 'r', 'sex'])
def red(message):
    if p1.is_alive():
        p1.terminate()
        p1.kill()
    yl.ypsCol(yl.pixels, yl.RED)

@bot.message_handler(commands=['blue', 'b', 'sad'])
def blue(message):
    if p1.is_alive():
        p1.terminate()
        p1.kill()
    yl.ypsCol(yl.pixels, yl.BLUE)

@bot.message_handler(commands=['yellow', 'y'])
def yellow(message):
    if p1.is_alive():
        p1.terminate()
        p1.kill()
    yl.ypsCol(yl.pixels, yl.ORANGE)

@bot.message_handler(commands=['pink', 'p'])
def pink(message):
    if p1.is_alive():
        p1.terminate()
        p1.kill()
    yl.ypsCol(yl.pixels, yl.PINK)

#@bot.message_handler(commands=['off', '0'])
#def off(message):
#    if p1.is_alive():
#        p1.terminate()
#        p1.kill()
#    print("STOP THREADS = true")
#    yl.ypsCol(yl.OFF)


bot.infinity_polling()
