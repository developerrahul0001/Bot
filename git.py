import os
import telebot

token = os.environ.get("9174039546:AAH-Cm7YIqzqFc8WiaderQJdOxWFPT4TkhQ")
if not token:
    raise RuntimeError("BOT_TOKEN secure environment setting mein set nahi hai")

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "GitHub demo bot online hai ✅")

bot.infinity_polling(skip_pending=True)
