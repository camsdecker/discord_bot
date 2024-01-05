import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import bot_methods as bot

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f'{client.user} has connected to Discord!')

@tree.command(
    name="pics",
    description="Show a random pic",
    guild=discord.Object(id=GUILD_ID)
)
async def pics(interaction):
    pic_path = bot.get_random_pic()
    await interaction.response.send_message(file=discord.File(pic_path))

client.run(TOKEN)