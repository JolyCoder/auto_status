#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import change_STATUS
import TeleSettings
import telebot


bot = telebot.TeleBot(TeleSettings.token)


@bot.message_handler(content_types=["text"])
def sendCaptcha(message):
    bot.send_message(message.chat.id, 'fvdvdf')



