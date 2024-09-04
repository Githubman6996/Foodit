pip install discord.py
import discord
from discord.ext import commands, tasks
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

# Replace 'your_bot_token' with your bot's token
TOKEN = 'MTI4MDI1NDQ4NDc5MDExNjQ2NA.GKhcAr._5Cxw8mY9zpmZkPrcRpUXcKyl5d5PQXqgj9AWM'
# Replace 'your_channel_id' with the ID of the channel where you want to send the message
CHANNEL_ID = 1246092256524374158  # replace with your channel ID

# Intents are required to use the message content and guild data
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

# Set up bot with command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    ping_channel.start()

@tasks.loop(hours=1)
async def ping_channel():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send('@everyone It’s time for a chat revival!')

bot.run(TOKEN)
