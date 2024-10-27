from discord.ext import commands

from src.commands import BaseCommand
from src.exceptions import NotFoundException
from src.services import WeatherService

class WeatherCommand(BaseCommand):
    """Provides the weather command"""

    def __init__(self, bot: commands.Bot):
        """The initialise method"""

        super().__init__(bot)
        self.weather_service = WeatherService()

    @commands.command(name='weather')
    async def get_weather(self, ctx, *location) -> None:
        """
        Gets the weather for a specified location and sends to the discord context

        Args:
            ctx: The discord context
            *location (str): The location string to search for

        Returns:
            None
        """

        try:
            weather_embed = self.weather_service.get_weather(' '.join(location))
            await ctx.send(embed=weather_embed)
        except NotFoundException as exception:
            await ctx.send(f"Error fetching weather data: {str(exception)}")

    def get_command_name(self) -> str:
        """
        Get the command name

        Returns:
             str: The command name
        """

        return "weather"