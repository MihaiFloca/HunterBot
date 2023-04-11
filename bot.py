import os

import discord
from dotenv import load_dotenv
from file_fetcher import get_file, get_random_image
from discord.ext import tasks

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    send_content.start()
    print(f'{client.user} has connected to Discord!')

def get_image():
    image = None
    while image is None:
        image = get_random_image()

    return image

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hunter'):
        await message.channel.send(get_image())

@tasks.loop(seconds = 3600)
async def send_content():
    channel = client.get_channel(820866752333611038)
    await channel.send(get_image())

client.run(TOKEN)


# TODO Deploy to AWS