from datetime import datetime
import os
from typing import Any, Dict

import discord
import requests

from src.data_loaders import JSONDataLoader
from src.exceptions import NotFoundException
from src.repositories import WeatherRepository
from src.services import EmbedService

class WeatherService:
    """Send an API request to retrieve the weather to be returned as an embed"""

    def __init__(self):
        """The initialise method"""

        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = os.getenv('WEATHER_API_BASE_URL')
        self.icon_url_template = "https://openweathermap.org/img/wn/{icon_code}@2x.png"
        self.repository = WeatherRepository(JSONDataLoader('src/data/temperature_facts.json'))

    def get_weather(self, location) -> discord.Embed:
        """
        Get the weather data from the API based on location

        Returns:
            discord.Embed: The formatted weather as a discord embed

        Raises:
            NotFoundException: If the weather data could not be found
        """

        params = {
            'q': location,
            'appid': self.api_key,
            'units': 'metric'
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return self.prepare_embed(data)

        raise NotFoundException('Could not fetch weather data')

    def prepare_embed(self, data: Dict[str, Any]) -> discord.Embed:
        """
        Prepares the weather response data into a discord embed

        Args:
            data (Dict[str, Any]): The json response data from the weather service

        Returns:
            discord.Embed: The discord embed object
        """

        local_time = datetime.utcfromtimestamp(data['dt'] + data['timezone']).strftime('%H:%M')
        fact = self.repository.get_temperature_fact(data['main']['temp'])
        thumbnail_url = self.icon_url_template.format(icon_code=data['weather'][0]['icon'])
        is_day = 'd' in data['weather'][0]['icon']

        fields = [
            {
                "name": "Temperature",
                "value": f"{data['main']['temp']}°C | {data['main']['temp'] * 1.8 + 32:.1f}°F",
            },
            {
                "name": "Fun Fact",
                "value": fact
            },
            {
                "name": "Feels Like",
                "value": f"{data['main']['feels_like']}°C | {data['main']['feels_like'] * 1.8 + 32:.1f}°F"
            },
            {
                "name": "Humidity",
                "value": f"{data['main']['humidity']}%"
            },
            {
                "name": "Local Time",
                "value": local_time
            }
        ]

        country = data.get('sys', {}).get('country', '')
        embed = EmbedService.create_embed(
            f"{data.get('name', 'Unknown')}{', ' + country if country else ''}",
            data['weather'][0]['description'].title(),
            fields,
            discord.Color.gold() if is_day else discord.Color.dark_gray()
        )

        embed.set_thumbnail(url=thumbnail_url)
        return embed