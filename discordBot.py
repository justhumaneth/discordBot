import os
import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
# put your DISCORD_TOKEN in 'Secrets'
TOKEN = os.getenv('DISCORD_TOKEN')

# assign image, add more
takeover = "./images/takeover.PNG"

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
# add your own specific command
    if '!takeover' in message.content.lower():
      # add link to image value
        await message.channel.send(file=discord.File(takeover))

bot.run(TOKEN)
