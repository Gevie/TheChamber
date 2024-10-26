import os
import requests


class WeatherService:
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = os.getenv('WEATHER_API_BASE_URL')

    def get_weather(self, location) -> str:
        params = {
            'q': location,
            'appid': self.api_key,
            'units': 'metric'
        }

        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return self.format_weather_data(data)

        raise Exception('Could not fetch weather data')

    @staticmethod
    def format_weather_data(data) -> str:
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        return (
            f"Weather in {data['name']}:\n"
            f"Temperature: {main['temp']}°C\n"
            f"Humidity: {main['humidity']}%\n"
            f"Weather: {weather_desc}\n"
            f"Wind Speed: {wind['speed']} m/s"
        )