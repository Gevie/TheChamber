from datetime import datetime
from typing import Any, Dict

import discord

from src.dtos import EmbedFieldDto
from src.embeds import BaseEmbed


class WeatherEmbed(BaseEmbed):
    ICON_URL_TEMPLATE = "http://openweathermap.org/img/wn/{}@2x.png"
    TEMPERATURE_CONVERSION_FACTOR = 1.8
    TEMPERATURE_CONVERSION_OFFSET = 32

    def __init__(self, fact: str, data: Dict[str, Any]):
        self.fact = fact
        self.data = data
        self.local_time = None

        self.title = self._get_title()
        self.description = self._get_description()
        self.color = self._get_color()

        self.fields = []

        self._set_local_time(self.data['dt'], self.data['timezone'])
        self._set_embed_fields()

    def get(self) -> discord.Embed:
        embed = super()._create()
        embed.set_thumbnail(url=self._get_thumbnail_url(self.data['weather'][0]['icon']))
        return embed

    def _format_temperature(self, temperature_in_celsius: float) -> str:
        temperature_in_fahrenheit = (
                temperature_in_celsius
                * self.TEMPERATURE_CONVERSION_FACTOR
                + self.TEMPERATURE_CONVERSION_OFFSET
        )

        return f"{temperature_in_celsius}°C | {temperature_in_fahrenheit:.1f}°F"

    def _get_color(self) -> discord.Color:
        icon = self._get_weather_icon()
        if icon and 'd' in icon:
            return discord.Color.gold()

        return discord.Color.dark_gray()

    def _get_description(self) -> str:
        weather_list = self.data.get('weather', [])

        if not weather_list or not isinstance(weather_list, list):
            return "No description available"

        return (
            weather_list[0]
            .get('description', "No description available")
            .title()
        )

    def _get_thumbnail_url(self, icon_code: str) -> str:
        return self.ICON_URL_TEMPLATE.format(icon_code=icon_code)

    def _get_title(self) -> str:
        city_name = self.data.get('name', 'Unknown')
        country_code = ''

        if 'sys' in self.data and 'country' in self.data['sys']:
            country_code = self.data['sys']['country']

        if country_code:
            return f"{city_name}, {country_code}"

        return city_name

    def _get_weather_icon(self) -> str:
        weather_list = self.data.get('weather', [])
        if weather_list and isinstance(weather_list, list):
            return weather_list[0].get('icon', '')

        return ''

    def _set_embed_fields(self) -> None:
        self.fields = [
            EmbedFieldDto(name="Temperature", value=self._format_temperature(self.data['main']['temp'])),
            EmbedFieldDto(name="Fun Fact", value=self.fact),
            EmbedFieldDto(name="Feels Like", value=self._format_temperature(self.data['main']['feels_like'])),
            EmbedFieldDto(name="Humidity", value=f"{self.data['main']['humidity']}%"),
            EmbedFieldDto(name="Local Time", value=self.local_time)
        ]

    def _set_local_time(self, timestamp: int, timezone_offset: int) -> None:
        self.local_time = datetime.utcfromtimestamp(timestamp + timezone_offset).strftime('%H:%M')