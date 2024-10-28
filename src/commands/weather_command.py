from discord.ext import commands

from src.commands import BaseCommand
from src.exceptions import NotFoundException
from src.services import WeatherService

class WeatherCommand(BaseCommand):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)
        self.weather_service = WeatherService()

    @commands.command(name='weather')
    async def get_weather(self, ctx, *location) -> None:
        try:
            weather_embed = self.weather_service.get(' '.join(location))
            await ctx.send(embed=weather_embed)
        except NotFoundException as exception:
            await ctx.send(f"Error fetching weather data: {str(exception)}")

    def get_command_name(self) -> str:
        return "weather"