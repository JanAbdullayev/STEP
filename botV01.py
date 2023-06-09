import telebot
import random
token = "5518845198:AAGaGerRgKpslSmQ8i8l_lbY4s_jpUfqO_g"
bot = telebot.TeleBot(token)
global money
money = 100


@bot.message_handler(commands=['start'])
def hello(message):
    global money
    message.from_user.money = int(money)
    bot.send_message(message.chat.id, f"Hi {message.from_user.first_name}")


@bot.message_handler(commands=['randomnum'])
def randomnum(message):
    global money
    message.from_user.money = int(money)
    bot.send_message(message.chat.id, str(random.randint(1,7)))
    bot.send_message(message.chat.id, str(message.from_user.money))


@bot.message_handler(commands=['earn'])
def randomnum(message):
    global money

    message.from_user.money += 1
    bot.send_message(message.chat.id, str(message.from_user.money))

bot.polling(non_stop=True)
