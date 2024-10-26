from abc import ABC, abstractmethod
from discord.ext import commands

class BaseCommand(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @abstractmethod
    def get_command_name(self) -> str:
        pass