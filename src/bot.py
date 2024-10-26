import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import sys

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from commands.weather_command import WeatherCommand

intents = discord.Intents.default()
intents.message_content = True

help_command = commands.DefaultHelpCommand(no_category='Commands')
bot = commands.Bot(command_prefix='c!', intents=intents, help_command=help_command)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

async def load_cogs():
    await bot.add_cog(WeatherCommand(bot))

async def main():
    await load_cogs()
    await bot.start(DISCORD_TOKEN)

if __name__ == '__main__':
    asyncio.run(main())