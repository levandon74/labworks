import telebot

bot = telebot.TeleBot('1819734300:AAG32EJHEvUYFoogAl9uLsRS7ULy9DWJ1ug')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши /start")
    elif message.text == "/joke":
        bot.send_message(message.from_user.id, "Шутка про Петьку")
    elif message.text == "/picture":
        bot.send_photo(message.from_user.id, photo='http://t0.gstatic.com/licensed-image?q=tbn:ANd9GcQz_psdKOAl4hDRt53K2BgQnDysEKS2PA6rr4NdbVWMtev41FCNroL4hcTFAZZe')
    else:
        bot.send_message(message.from_user.id, "Напиши /help")
bot.polling(none_stop=True, interval=0)