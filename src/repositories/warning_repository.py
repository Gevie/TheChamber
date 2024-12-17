from sqlalchemy.orm import Session
from src.models import Warning
from src.repositories.base_repository import BaseRepository


class WarningRepository(BaseRepository[Warning]):
    def __init__(self, db_session: Session):
        super().__init__(Warning, db_session)

    def warn(self, user_id: int, issuer_id: int, reason: str) -> Warning:
        warning = Warning()
        warning.issuer_id = issuer_id
        warning.user_id = user_id
        warning.reason = reason

        self.add(warning)

        return warning