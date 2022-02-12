import os

from telegram import Bot, ParseMode


TOKEN = str(os.environ.get("TELEGRAM_KEY"))
CHAT_ID = int(os.environ.get("TELEGRAM_CHAT_ID"))

def send_message(data):
    bot = Bot(TOKEN)
    with open(f"./alert/telegram/img/{data['country'].lower()}.png", 'rb') as country_flag:
        caption = f"Olá, Aparentemente as inscrições do <b>{data['name']}</b> para <b>{data['program']}</b> já estão abertas!\nEntre no site do <a href='{data['url']}'>{data['name']}</a> e saiba mais."
        bot.send_photo(
            chat_id=CHAT_ID, 
            photo=country_flag, 
            caption=caption,
            parse_mode=ParseMode.HTML
        )