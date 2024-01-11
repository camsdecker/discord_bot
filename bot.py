import os
import discord
from discord import app_commands
from dotenv import load_dotenv
from YTDLSource import YTDLSource
from random import randint

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


# /pics
# selects a random file in the pics/ directory and sends it to the text channel of
#   whomever used the command
@tree.command(
    name="pics",
    description="Show a random pic",
    guild=discord.Object(id=GUILD_ID)
)
async def pics(interaction: discord.Interaction):
    try:
        path = "/home/cam/discord_bot/discord_bot/pics/"
        pic_list = os.listdir(path)
        chosen_pic_index = randint(0,len(pic_list)-1)
        chosen_pic = pic_list[chosen_pic_index]
        pic_path = path + chosen_pic
        await interaction.response.send_message(file=discord.File(pic_path))
    except:
        print(f"!!!ERROR: Something went wrong when sending file at {pic_path}!!!")
        await interaction.response.send_message("ERROR: Something went wrong, try again")

# /play
# connects to the user's voice channel and plays the song from youtube_url
@tree.command(
    name="play",
    description="play a song from youtube",
    guild=discord.Object(id=GUILD_ID)
)
async def play(interaction: discord.Interaction, youtube_url: str):
    if not interaction.user.voice:
        await interaction.response.send_message("ERROR: user is not in a voice channel")
        return
    try:
        if len(client.voice_clients) == 0:
            bot_voice = await interaction.user.voice.channel.connect()
        else:
            bot_voice = client.voice_clients[0]
        filename = await YTDLSource.from_url(youtube_url)
        bot_voice.play(discord.FFmpegPCMAudio(executable="ffmpeg",source=filename))
        await interaction.response.send_message(f"Now playing {youtube_url}")
    except:
        await interaction.response.send_message("ERROR: Something went wrong, try again")

@tree.command(
        name="pause",
        description="pauses or resumes the music",
        guild=discord.Object(id=GUILD_ID)
)
async def pause(interaction: discord.Interaction):
    if len(client.voice_clients) == 0:
        await interaction.response.send_message("ERROR: bot is not currently in a channel")
        return
    bot_voice = client.voice_clients[0]
    if bot_voice.is_playing(): 
        bot_voice.pause()
        await interaction.response.send_message("Paused...")
    elif bot_voice.is_paused():
        bot_voice.resume()
        await interaction.response.send_message("Resuming...")
    else:
        await interaction.response.send_message("ERROR: Bot is not playing any music")
    

# /leave
# forces the bot to disconnect from the voice channel it's currently in
@tree.command(
    name="leave",
    description="forces the bot to leave the voice channel",
    guild=discord.Object(id=GUILD_ID)
)
async def leave(interaction: discord.Interaction):
    if len(client.voice_clients) == 0:
        await interaction.response.send_message("ERROR: bot is not currently in a channel")
    else:
        await client.voice_clients[0].disconnect()
        await interaction.response.send_message("Cambot out :sunglasses:")

client.run(TOKEN)