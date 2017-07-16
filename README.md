<h1 align="center"> Auto - status</h1>
<h2 align="center">Что это?</h2>
<p>Auto_Status - это программа которая позволяет переодически менять статус в ВК.</p>
<h2 align="center">Используемые библиотеки :
urllib
vk_api
telebot
</h2>
<h2 align="center">Настройка</h2>
<p>Для того чтобы настроить скрипт, нужно изменить под себя файл TeleBot1.py</p>

```python

	#!/usr/bin/env python 
	# -*- coding: utf-8 -*- 

	# Настройки Telegram #
	k = 'dgfdg'
	token = 'token'
	# Настройки Telegram #

	# Настройки ВК #
	VKlog1 = 'none'
	VKpass1 = 'none'
	VKlog2 = 'VKlogin2'
	VKpass2 = 'VKpassword2'
	VKlog3 = 'VKlogin3'
	VKpass3 = 'VKpassword3'
	# Настройки ВК #
```
<p>В поля VKlog1 и VKpass1 вставляем соответственно логин и пароль. Остальные поля не трогаем. Также выше есть поле token туда вставляем токен нашего бота.

После этих манипуляций сохраняем наш файл и запускаем change_STATUS.py. Наслаждаемся!
</p>
