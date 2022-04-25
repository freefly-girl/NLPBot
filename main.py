import telebot
from telebot.async_telebot import AsyncTeleBot
import logging
import asyncio
import requests

logger = telebot.logger
telebot.logger.setLevel(logging.ERROR)  # Outputs debug messages to console.

API_TOKEN = '5187163126:AAHx2de-15z4EWkKUf_RaS9zplpo6gR6ZdI'
bot = AsyncTeleBot(API_TOKEN)

conv_context = {}


@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    conv_context[message.chat.id] = [
        {'speaker': 1, 'text': 'Привет! давай пообщаемся))'}
    ]
    await bot.reply_to(message, "Привет! давай пообщаемся))")

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    inputs = [
        {'speaker': 0, 'text': message.text},
    ]
    if len(conv_context[message.chat.id]) == 5:
        conv_context[message.chat.id] = conv_context[message.chat.id][1:] + inputs
    else:
        conv_context[message.chat.id] = conv_context[message.chat.id] + inputs
    response = requests.post('http://127.0.0.1:6969/get_answer', json={'inputs': inputs}).json()
    resp_text = response['outputs']
    resp = [
        {'speaker': 1, 'text': resp_text}
    ]
    print(f"==> Text input: {message.text}")
    print(f"==> Text output: {resp_text}")
    if len(conv_context[message.chat.id]) == 5:
        conv_context[message.chat.id] = conv_context[message.chat.id][1:] + resp
    else:
        conv_context[message.chat.id] = conv_context[message.chat.id] + resp
    await bot.reply_to(message, resp_text)


asyncio.run(bot.infinity_polling())
