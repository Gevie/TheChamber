import random
from typing import List, Dict, Union

from src.data_loaders import JSONDataLoader

TemperatureFact = Dict[str, Union[float, List[str]]]

class WeatherRepository:
    def __init__(self, data_loader: JSONDataLoader):
        self.data_loader = data_loader
        self.facts: List[TemperatureFact] = self._load_temperature_facts()

    def _load_temperature_facts(self) -> List[TemperatureFact]:
        data = self.data_loader.load()
        if not isinstance(data, list):
            raise ValueError('Expected data to be a list of temperature facts.')

        return data

    def get_temperature_fact(self, temperature_in_celsius: float) -> str:
        for entry in self.facts:
            if entry['min_temp'] <= temperature_in_celsius <= entry['max_temp']:
                return random.choice(entry['facts'])

        return (
            "Couldn't find a fact for this temperature. "
            "Something went wrong otherwise that location is dangerously hot or cold x.X"
        )