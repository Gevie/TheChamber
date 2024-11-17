from sqlalchemy.orm import Session
from src.models.temperature_fact import TemperatureFact
from src.repositories.base_repository import BaseRepository


class TemperatureFactRepository(BaseRepository[TemperatureFact]):
    def __init__(self, db_session: Session):
        super().__init__(TemperatureFact, db_session)