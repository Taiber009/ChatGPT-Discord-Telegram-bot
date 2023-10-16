from dotenv import load_dotenv
import os
import discord
from app.openai_chat.connect_openai import chatgpt_response

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged in Discord as:", self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        try:
            text = str(chatgpt_response(message.content))
            print(text)
            if len(text)<=1900:
                await message.channel.send(text)
            else:
                chunks = [text[i:i+1900] for i in range(0, len(text), 1900)]
                for chunk in chunks:
                    await message.channel.send(chunk)
        except Exception as e:
            print(f'Ошибка в запросе {message.content}\n\nПричина:{e}')
            await message.channel.send(f'Ошибка в запросе {message.content}\n\nПричина:{e}') 

intents = discord.Intents.default()
#intents.message_content = True
client = MyClient(intents=intents)
#client.run(discord_token)

