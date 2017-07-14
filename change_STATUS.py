#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import urllib
from datetime import datetime, time, date
import time
import vk_api

# Переменные #
a = 1
# Переменные #

# Функции #
def auth(count, vkLogin1 = '', vkPass1 = '', captchaHandler1 = '', vkLogin2 = '', vkPass2 = '', captchaHandler2 = '', vkLogin3 = '', vkPass3 = '', captchaHandler3 = ''):
	key = ""
	vk = vk_api.VkApi(login = vkLogin1, password = vkPass1, captcha_handler=captchaHandler1)
	if count == 1:
		vk = vk_api.VkApi(login = vkLogin1, password = vkPass1, captcha_handler=captchaHandler1)
		vk.auth()
	elif count == 2:
		vk = vk_api.VkApi(login = vkLogin1, password = vkPass1, captcha_handler=captchaHandler1)
		vk.auth()
		vk2 = vk_api.VkApi(login = vkLogin2, password = vkPass2, captcha_handler=captchaHandler2)
		vk2.auth()
	elif count == 3:
		vk = vk_api.VkApi(login = vkLogin1, password = vkPass1, captcha_handler=captchaHandler1)
		vk.auth()
		vk2 = vk_api.VkApi(login = vkLogin2, password = vkPass2, captcha_handler=captchaHandler2)
		vk2.auth()
		vk3= vk_api.VkApi(login = vkLogin3, password = vkPass3, captcha_handler=captchaHandler3)
		vk3.auth()
	k = 0

def change_status(text):	
	status = {'text': text}
	vk.method('status.set', status)
	vk2.method('status.set', status)

def captcha_get(key):
	resource = urllib.urlopen(key)
	out = open("img.jpg", 'wb')
	out.write(resource.read())
	out.close()
	print "CAPTCHA!"

def captcha_handler(captcha):

    key = captcha.get_url()
    captcha_get(key)

    return captcha.try_again(key)
# Функции #

# Авторизация #
auth(3, 'login1', 'password1', captcha_handler)
# Авторизация #

# Основной код, по изменению статуса #
while  a == 1:	
	#TeleBot.sendCaptcha()
	k = k + 1
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
		time.sleep(20)
# Основной код, по изменению статуса #