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
    TEMPERATURE_CONVERSION_FACTOR = 1.8
    TEMPERATURE_CONVERSION_OFFSET = 32

    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = os.getenv('WEATHER_API_BASE_URL')
        self.icon_url_template = "https://openweathermap.org/img/wn/{icon_code}@2x.png"
        self.repository = WeatherRepository(JSONDataLoader('src/data/temperature_facts.json'))

    def _create_embed(self, data: Dict[str, Any]) -> discord.Embed:
        country = data.get('sys', {}).get('country', '')
        fact = self.repository.get_temperature_fact(data['main']['temp'])
        is_day = 'd' in data['weather'][0]['icon']
        local_time = self._get_local_time(data['dt'], data['timezone'])

        embed = EmbedService.create_embed(
            f"{data.get('name', 'Unknown')}{', ' + country if country else None}",
            data['weather'][0]['description'].title(),
            self._generate_embed_fields(data, fact, local_time),
            discord.Color.gold() if is_day else discord.Color.dark_gray()
        )

        thumbnail_url = self._get_thumbnail_url(data['weather'][0]['icon'])
        embed.set_thumbnail(url=thumbnail_url)
        return embed

    def _format_temperature(self, temperature_in_celsius: float) -> str:
        temperature_in_fahrenheit = (
            temperature_in_celsius
            * self.TEMPERATURE_CONVERSION_FACTOR
            + self.TEMPERATURE_CONVERSION_OFFSET
        )

        return f"{temperature_in_celsius}°C | {temperature_in_fahrenheit:.1f}°F"

    def _generate_embed_fields(self, data: Dict[str, Any], fact: str, local_time: str) -> list:
        return [
            {
                "name": "Temperature",
                "value": self._format_temperature(data['main']['temp']),
            },
            {
                "name": "Fun Fact",
                "value": fact
            },
            {
                "name": "Feels Like",
                "value": self._format_temperature(data['main']['feels_like'])
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

    @staticmethod
    def _get_local_time(timestamp: int, timezone_offset: int) -> str:
        return datetime.utcfromtimestamp(timestamp + timezone_offset).strftime('%H:%M')

    def _get_thumbnail_url(self, icon_code: str) -> str:
        return self.icon_url_template.format(icon_code=icon_code)

    def get(self, location) -> discord.Embed:
        params = {
            'q': location,
            'appid': self.api_key,
            'units': 'metric'
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return self._create_embed(response.json())

        raise NotFoundException('Could not fetch weather data')