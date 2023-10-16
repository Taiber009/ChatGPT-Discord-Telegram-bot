from dotenv import load_dotenv
import os
import telebot
from app.openai_chat.connect_openai import chatgpt_response

load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(telegram_token)
print(f"Logged in Telegram as: @{bot.get_me().first_name}")

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    text="Не удалось обработать команду!\nПричина: "
    try:
        # values = message.text.split(' ')
        # if len(values)>3:
        #     raise APIExeption('Слишком много параметров!')
        # if len(values)<3:
        #     raise APIExeption('Слишком мало параметров!')
        # quote, base, amount = values
        text = chatgpt_response(message.text)
    except Exception as e:
        text += str(e)
    finally:
        print(text)
        bot.send_message(message.chat.id, text)
#bot.polling()