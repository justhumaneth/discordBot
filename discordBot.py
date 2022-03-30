import os
import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
lfg = "https://media.discordapp.net/attachments/899994181982883841/955858688890003466/lfg1.png"
hello = "https://media.discordapp.net/attachments/896685581487210580/955200075611660310/pepe_hello2.png"
ban = "https://media.discordapp.net/attachments/896685581487210580/957806209849774080/BAN1.png"
wenlambo = "https://media.discordapp.net/attachments/899994181982883841/955968441922228224/wen_lambo2.png"

# 2
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    if '!lfg' in message.content.lower():
        await message.channel.send(lfg)
    if '!hello' in message.content.lower():
        await message.channel.send(hello)
    if '!ban' in message.content.lower():
        await message.channel.send(ban)
    if '!wenlambo' in message.content.lower():
        await message.channel.send(wenlambo)

bot.run(TOKEN)

