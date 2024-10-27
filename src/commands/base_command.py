from abc import abstractmethod
from discord.ext import commands

class BaseCommand(commands.Cog):
    """The base command interface/abstract class"""

    def __init__(self, bot: commands.Bot):
        """The initialise method"""

        self.bot = bot

    @abstractmethod
    def get_command_name(self) -> str:
        """
        Get the command name

        Returns:
             str: The command name
        """