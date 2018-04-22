import telebot

#В качестве сервера использовать Heroku
# https://tproger.ru/translations/telegram-bot-create-and-deploy/

TOKEN = "577786655:AAGvb_dlp2PYexqbL00UAvrRpdZeAN936vg"

bot = telebot.TeleBot(TOKEN)
bot.config['api_key'] = TOKEN

print(bot.send_message(371497788, "Python"))
# print(bot.get_updates())
