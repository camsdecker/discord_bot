# bot.py
import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import bot_methods as bot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client(intents=discord.Intents.all())      #FIXME: limit the scope of the intents
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    #await tree.sync(guild=discord.Object(id=Your guild id))
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == 'test':
        pic = bot.get_random_pic()
        await client.get_user(message.author.id).send(file=discord.File(pic))

@tree.command(
    name="commandname",
    description="My first application Command",
    guild=discord.Object(id=12417128931)
)
async def first_command(interaction):
    await interaction.response.send_message("Hello!")

client.run(TOKEN)