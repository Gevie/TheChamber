from dataclasses import dataclass


@dataclass
class TemperatureFactDto:
    temperature: float
    fact: str