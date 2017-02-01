#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This is a simple echo bot using decorators and webhook with flask
# It echoes any incoming text messages and does not use the polling method.

import flask
import telebot
import logging
import os
from flask import Flask
from flask import Flask, request
import requests
import time
import json

# git commit -m 'Handle v.0.0.5'
# git push flask-helloworld master


API_TOKEN = '284335555:AAFFlL8EFucCGKhHgXYgtXZJBC-UK-DiOVU'

WEBHOOK_HOST = 'sheltered-headland-50963.herokuapp.com'
WEBHOOK_PORT = 88           # 443, 80, 88 or 8443 (port need to be 'open')
WEBHOOK_LISTEN = '0.0.0.0'  # In some VPS you may need to put here the IP addr

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (API_TOKEN)


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
bot = telebot.TeleBot(API_TOKEN)
# Отключаем webhook
# bot.remove_webhook()
# Отключть polling
# bot.polling(none_stop = False)


# app = flask.Flask(__name__) - оригинал
app = Flask(__name__)         # исправил


@app.route('/')
def hello():
    return ''


# Empty webserver index, return nothing, just http 200
@app.route('/', methods = ['GET', 'HEAD'])
def index():
    return ''


# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods = ['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


# Handle '/start' and '/help'
@bot.message_handler(commands = ['help', 'start'])
def send_welcome(message):
    print('мы тут3')
    # Приветствие
    hi = ('Hi there, I am EchoBot.\n'
          'I am here to echo your kind words back to you')
    bot.send_message(message.chat.id, hi)

# Handle all other messages
@bot.message_handler(func = lambda message: True, content_types = ['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()
time.sleep(2)


# Set webhook
bot.set_webhook(url = WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)


# Start flask server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", WEBHOOK_PORT))
    app.run(host = WEBHOOK_LISTEN,
            port = port,
            debug = True)

"""
# Запуск через polling
if __name__ == '__main__':
    bot.polling(none_stop = True, interval = 0, timeout = 3)
"""
