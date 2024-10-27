import random
from typing import List, Dict, Union

from src.data_loaders import JSONDataLoader

TemperatureFact = Dict[str, Union[float, List[str]]]

class WeatherRepository:
    """Repository class for managing temperature facts."""

    def __init__(self, data_loader: JSONDataLoader):
        """
        Initialise the repository with a data loader.

        Args:
            data_loader (JSONDataLoader): The data loader instance to load
        """

        self.data_loader = data_loader
        self.facts: List[TemperatureFact] = self._load_temperature_facts()

    def _load_temperature_facts(self) -> List[TemperatureFact]:
        """
        Load and parse temperature facts from the data loader.

        Returns:
            List[TemperatureFact]: A list of temperature facts

        Raises:
            ValueError: If the loaded data is invalid.
        """

        data = self.data_loader.load()
        if not isinstance(data, list):
            raise ValueError('Expected data to be a list of temperature facts.')

        return data

    def get_temperature_fact(self, temperature_in_celsius: float) -> str:
        """
        Get a fact based on the temperature (in Celsius).

        Args:
            temperature_in_celsius (float): The temperature to search in Celsius

        Returns:
            str: A fact corresponding to the temperature, or a notice message if not found
        """

        for entry in self.facts:
            if entry['min_temp'] <= temperature_in_celsius <= entry['max_temp']:
                return random.choice(entry['facts'])

        return "Couldn't find a fact for this temperature, something went wrong otherwise that location is dangerously hot or cold x.x"