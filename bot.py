import telebot
from const import TTOKEN

#В качестве сервера использовать Heroku
# https://tproger.ru/translations/telegram-bot-create-and-deploy/



bot = telebot.TeleBot(TTOKEN)
bot.config['api_key'] = TTOKEN

print(bot.send_message(371497788, "Python"))
# print(bot.get_updates())
