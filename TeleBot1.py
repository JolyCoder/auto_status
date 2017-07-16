#!/usr/bin/env python 
# -*- coding: utf-8 -*- 


import telebot
import config


bot = telebot.TeleBot(config.token)

captcha = ''
def sendCaptcha(text): # Название функции не играет никакой роли, в принципе
    bot.send_message('331832423', text)
    config.k = 1

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
	if config.k == 1:
		captcha = message.text
		print(captcha)
		config.k = 0
	else:
    	 bot.send_message(message.chat.id, 'Еще не было каптчи дурак!')

if __name__ == '__main__':
     bot.polling(none_stop=True)



