import unittest
from unittest.mock import patch
from src.services.weather_service import WeatherService

class TestWeatherCommand(unittest.TestCase):
    @patch('src.services.weather_service.requests.get')
    def test_get_success(self, mock_get):
        """Arrange"""
        mock_response = {
            'main': {'temp': 20, 'humidity': 50},
            'wind': {'speed': 5},
            'weather': [{'description': 'clear sky'}],
            'name': 'Sample City'
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        weather_service = WeatherService()

        """Act"""
        response = weather_service.get('Sample City')

        """Assert"""
        self.assertIn('Weather in Sample City', response)
        self.assertIn('Temperature: 20°C', response)
        self.assertIn('Humidity: 50%', response)
        self.assertIn('Weather: clear sky', response)
        self.assertIn('Wind Speed: 5 m/s', response)

if __name__ == '__main__':
    unittest.main()