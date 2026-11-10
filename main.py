import os
import telebot
from telebot import types

# توكن البوت الخاص بك
BOT_TOKEN = "9066189502:AAHWnnimTXjyUXTVkXK5NUiWBG4w1BKizzc"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    btn_help = types.InlineKeyboardButton("ℹ️ حول البوت", callback_data="help_info")
    markup.add(btn_help)
    
    welcome_text = (
        f"أهلاً بك يا {message.from_user.first_name}! 👋\n\n"
        "تم تشغيل البوت بنجاح على منصة Render 🚀"
    )
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "help_info":
        bot.send_message(call.message.chat.id, "هذا البوت يعمل 24/7 عبر استضافة Render المجانية.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلت رسالتك: {message.text}")

if __name__ == "__main__":
    print("البوت يعمل الآن...")
    bot.infinity_polling()
