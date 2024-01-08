import os
import discord
from discord import app_commands
from dotenv import load_dotenv
import bot_methods as bot
from YTDLSource import YTDLSource

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    #await tree.sync(guild=None)
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f'{client.user} has connected to Discord!')


# /pics
# selects a random file in the pics/ directory and sends it to the text channel of
#   whomever used the command
@tree.command(
    name="pics",
    description="Show a random pic",
    guild=discord.Object(id=GUILD_ID)
)
async def pics(interaction: discord.Interaction):
    pic_path = bot.get_random_pic()
    await interaction.response.send_message(file=discord.File(pic_path))

@tree.command(
    name="play",
    description="play a song from youtube",
    guild=discord.Object(id=GUILD_ID)
)
async def play(interaction: discord.Interaction, youtube_url: str):
    if not interaction.user.voice:
        await interaction.response.send_message("ERROR: user is not in a voice channel")
    else:
        try:
            bot_voice = await interaction.user.voice.channel.connect()
            filename = await YTDLSource.from_url(youtube_url)
            bot_voice.play(discord.FFmpegPCMAudio(executable="ffmpeg",source=filename))
            await interaction.response.send_message(f"Now playing {filename}")
        except:
            await interaction.response.send_message("ERROR: Something went wrong :(")

@tree.command(
    name="leave",
    description="forces the bot to leave the voice channel",
    guild=discord.Object(id=GUILD_ID)
)
async def play(interaction: discord.Interaction):
    if len(client.voice_clients) == 0:
        await interaction.response.send_message("ERROR: bot is not currently in a channel")
    else:
        await client.voice_clients[0].disconnect()
        await interaction.response.send_message("Cam Bot out B)")

client.run(TOKEN)