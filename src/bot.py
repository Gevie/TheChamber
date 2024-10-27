import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

help_command = commands.DefaultHelpCommand(no_category='Commands')
bot = commands.Bot(command_prefix='c!', intents=intents, help_command=help_command)


@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')


class BotRunner:
    def __init__(self):
        pass

    @staticmethod
    async def load_cogs():
        from src.commands.weather_command import WeatherCommand
        await bot.add_cog(WeatherCommand(bot))

    async def run(self):
        await self.load_cogs()
        await bot.start(TOKEN)