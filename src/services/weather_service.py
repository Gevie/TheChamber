import os
from typing import Any, Dict

import discord
import requests

from src.embeds import WeatherEmbed
from src.exceptions import NotFoundException
from src.models import TemperatureFact
from src.repositories import RepositoryFactory


class WeatherService:
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = os.getenv('WEATHER_API_BASE_URL')

        repository_factory = RepositoryFactory()
        self.repository = repository_factory.get_repository(TemperatureFact)

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

    def _create_embed(self, data: Dict[str, Any]) -> discord.Embed:
        temperature_fact = self.repository.get_by_temperature(data['main']['temp'])
        weather_embed = WeatherEmbed(temperature_fact=temperature_fact, data=data)

        return weather_embed.get()