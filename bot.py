import telebot
from const import TTOKEN

# В качестве сервера использовать Heroku
# https://tproger.ru/translations/telegram-bot-create-and-deploy/


bot = telebot.TeleBot(TTOKEN)


# bot.config['api_key'] = TTOKEN

# bot.send_message(371497788, "Python")
# print(bot.get_updates())

# upd = bot.get_updates()  # ['result'][-1]
# print(1)

# print(upd[-1])
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'a':
        bot.send_message(message.chat.id, 'b')
    elif message.text == 'b':
        bot.send_message(message.chat.id, 'a')
    else:
        bot.send_message(message.chat.id, 'Ты не умеешь играть в эту игру')


bot.polling(none_stop=True, interval=0)
