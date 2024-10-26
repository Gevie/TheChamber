from discord.ext import commands
from src.services.weather_service import WeatherService
from src.commands.base_command import BaseCommand

class WeatherCommand(BaseCommand):
    def __init__(self, bot: commands.Bot):
        super().__init__(bot)
        self.weather_service = WeatherService()

    @commands.command(name='weather')
    async def get_weather(self, ctx, *location) -> None:
        """Gets the weather for a specified location"""

        location = ' '.join(location)
        try:
            weather_data = self.weather_service.get_weather(location)
            await ctx.send(weather_data)
        except Exception as exception:
            await ctx.send(f"Error fetching weather data: {str(exception)}")

    def get_command_name(self) -> str:
        return "weather"