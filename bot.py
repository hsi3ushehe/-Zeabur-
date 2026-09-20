import telebot
import os

# टोकन को Environment Variable से लेंगे (Zeabur पर सेट करेंगे)
TOKEN = os.environ.get('BOT_TOKEN')
if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable set नहीं है!")

bot = telebot.TeleBot(TOKEN)

# /start कमांड हैंडलर
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        f"नमस्ते {message.from_user.first_name}! 👋\n\n"
        f"मैं एक टेस्ट बॉट हूं, Zeabur पर डिप्लॉय हुआ हूं।\n"
        f"अभी मेरे पास कोई और फीचर नहीं है, लेकिन मैं ठीक से काम कर रहा हूं! ✅"
    )
    bot.reply_to(message, welcome_text)

# बाकी सभी मैसेज के लिए (ऑप्शनल)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "मैंने आपका मैसेज पा लिया, लेकिन मैं अभी सिर्फ /start ही समझता हूं।")

if __name__ == '__main__':
    print("बॉट चालू हो रहा है...")
    # Polling मोड में बॉट चलाएं (Zeabur के लिए यही सिंपल है)
    bot.infinity_polling()
