import discord
import asyncio
from discord.ext import commands

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = 'MTE5Njg5NzI0OTIzODcxNjUwNw.GCDDuc.GLlKnudCUQLfe8QjCNqGDTWkPux1C6dT9FmJnk'

# Define intents
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    # Replace 'SERVER_ID' and 'CHANNEL_ID' with your server and channel IDs
    server_id = '1186820354186948749'
    channel_id = 1202223741145448448

    # Fetch the server and channel
    server = bot.get_guild(int(server_id))
    channel = server.get_channel(int(channel_id))

    # Fetch messages and delete them with a delay
    async for message in channel.history(limit=None):
        await message.delete()
        await asyncio.sleep(0.8)  # Add a delay of 0.5 seconds between deletions

    print(f'All messages in #{channel.name} have been deleted.')
    await bot.close()  # Close the bot after all messages have been deleted

# Run the bot
bot.run(TOKEN)
