# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 21:18:23 2023

@author: akhilrajs
"""

import telebot
from datetime import date
from datetime import datetime
from time import strftime
from os import path
from os import makedirs
from os import getcwd

# create a log folder and file for storing all activities 
date = str(date.today())
print("[#] date : " + str(date))
if not path.exists('log_data'):
    print("[#] creating log_data directory")
    makedirs('log_data')
cd = getcwd() + "\\log_data"
log_folder = (cd + "\\" + (date))
if not path.exists(log_folder):
    print("[#] creating folder with date for logs")
    makedirs(log_folder)
cd = cd + "\\" + date
now = datetime.now()
current_time = strftime("%H_%M_%S")



# defining a function to save logs
def save_log(log):
    log_file = open((log_folder + "\\" + str(current_time) + ".txt"),"a")
    log_file.write(log)
    log_file.close()


# create a new bot using the token provided by the Telegram Bot Father
bot = telebot.TeleBot("5950108813:")

# define a function that will be called when a message is received
@bot.message_handler(content_types=['text'])
def handle_message(message):
    print("Received message:", message.text)
    bot.send_message(message.chat.id, "Thank you for your message!")


# start the bot
bot.polling()