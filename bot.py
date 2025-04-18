import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import scraper

bot = telebot.TeleBot('7806855925:AAG1GH5V2t26cynQZS0ChTtDOBvsr1o7XiA')
user_selected_currency = {}
@bot.message_handler(commands=['start'])
def start_bot(message):
    inline_markup = InlineKeyboardMarkup()
    inline_USD = InlineKeyboardButton("USD", callback_data='1')
    inline_EUR = InlineKeyboardButton("EUR", callback_data='2')
    inline_RUB = InlineKeyboardButton("RUB", callback_data='3')
    inline_markup.add(inline_USD, inline_EUR, inline_RUB)
    bot.send_message(message.from_user.id, "Choose Rate", reply_markup=inline_markup)
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    user_id = call.from_user.id
    user_selected_currency[user_id] = call.data
    bot.send_message(user_id, "Send value to change")
@bot.message_handler(func=lambda message: message.text.isdigit())
def handle_value(message):
    user_id = message.from_user.id
    if user_id not in user_selected_currency:
        bot.send_message(user_id, "Please select a currency first")
        return
    try:
        amount = float(message.text)
        rate = float(scraper.parse_data(user_selected_currency[user_id]))
        result = amount * rate
        bot.send_message(user_id, f'Result is {result}')
    except ValueError:
        bot.send_message(user_id, "Invalid number or conversion rate. Try again.")
bot.polling(none_stop=True)

