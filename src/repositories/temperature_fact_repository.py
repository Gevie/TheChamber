import random

from sqlalchemy import and_
from sqlalchemy.orm import Session
from src.models.temperature_fact import TemperatureFact
from src.repositories.base_repository import BaseRepository


class TemperatureFactRepository(BaseRepository[TemperatureFact]):
    def __init__(self, db_session: Session):
        super().__init__(TemperatureFact, db_session)

    def get_by_temperature(self, temperature_in_celsius: float) -> None|TemperatureFact:
        facts = (
            self._db_session.query(TemperatureFact)
                .filter(
                    and_(
                        TemperatureFact.min_temperature <= temperature_in_celsius,
                        TemperatureFact.max_temperature >= temperature_in_celsius
                    )
                )
                .all()
        )

        if facts:
            return random.choice(facts)

        return None