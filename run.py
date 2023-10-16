from app.discord_bot.connect_discord import client, discord_token
from app.telegram_bot.connect_telegram import bot, telegram_token
from app.openai_chat.connect_openai import chatgpt_response
import telebot
import threading

def run_discord_bot():
    client.run(discord_token)


def run_telegram_bot():
    bot.polling()


def run_manual_requests():
    try:
        print("Ручной ввод активирован")
        text = str(input("Напишите вашу команду для ChatGPT:\n"))
        while True:
            print(chatgpt_response(text))
            text = str(input("Напишите вашу команду для ChatGPT:\n"))
    except Exception as e:
        print(f"Ошибка ручного ввода! Консоль упала! Причина: \
            {str(e) if e.args.__len__() else 'Неизвестно, нет Exception'}\n")


if __name__ == "__main__":
    discord_thread = threading.Thread(target=run_discord_bot)
    telegram_thread = threading.Thread(target=run_telegram_bot)
    manual_thread = threading.Thread(target=run_manual_requests)

    discord_thread.start()
    telegram_thread.start()
    manual_thread.start()

    discord_thread.join()
    telegram_thread.join()
    manual_thread.join()
