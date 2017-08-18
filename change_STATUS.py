#!/usr/bin/env python 
# -*- coding: utf-8 -*- 



# Используемые библиотеки и файлы #
import urllib
from datetime import datetime, time, date
import time
import vk_api
import TeleBot1
import json
# Используемые библиотеки и файлы #

# Переменные #
a = 1
vk = ''
# Переменные #

# JSON #

raw_cred = open('config.json').read()
cred = json.loads(raw_cred)

# JSON #


# Функции #
def change_status(text):	
	status = {'text': text}
	vk.method('status.set', status)
	# vk2.method('status.set', status)

def captcha_get(key):
	resource = urllib.urlopen(key)
	out = open("img.jpg", 'wb')
	out.write(resource.read())
	out.close()
	print "CAPTCHA!"

def captcha_handler(captcha):

    key = captcha.get_url()
    captcha_get(key)
    TeleBot1.sendCaptcha(key)
    time.sleep(30)
    print(TeleBot1.captcha)
    return captcha.try_again(TeleBot1.captcha)
# Функции #

# Авторизация #
vk = vk_api.VkApi(login = config.VKlog1, password = config.VKpass1, captcha_handler=captcha_handler)
vk.auth()
# Авторизация #

# Основной код, по изменению статуса #
while  a == 1:	
	#TeleBot.sendCaptcha()
	for x in xrange(1,10):
		d = datetime.today()	
		t = str(d.time())
		tm = ""
		for x in t:
			if x != '.':
				tm = tm + x
			else:	
				break
			 
		tex = 'NOW %s' % tm 
		change_status(tex)
		print "SENDED!"
		time.sleep(5)
# Основной код, по изменению статуса #