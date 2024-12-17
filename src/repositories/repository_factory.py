from src.database import SessionLocal
from src.repositories.warning_repository import WarningRepository
from src.repositories.temperature_fact_repository import TemperatureFactRepository
from src.models import TemperatureFact, Warning

class RepositoryFactory:
    def __init__(self):
        self._db_session = SessionLocal()
        self._repository_map = {
            TemperatureFact: TemperatureFactRepository,
            Warning: WarningRepository
        }

    def get_repository(self, model):
        repository_class = self._repository_map.get(model)

        if not repository_class:
            raise ValueError(f"Repository for model {model} does not exist.")

        return repository_class(self._db_session)

    def close_session(self) -> None:
        self._db_session.close()