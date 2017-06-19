import urllib
from datetime import datetime, time, date
import time
import vk_api
import TeleBot

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

key = ""
vk = vk_api.VkApi(login = 'login', password = 'password', captcha_handler=captcha_handler)
vk2 = vk_api.VkApi(login = 'login', password = 'password', captcha_handler=captcha_handler)
vk.auth()
vk2.auth()
a = 1
k = 0






while  a == 1:
	TeleBot.sendCaptcha()
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



