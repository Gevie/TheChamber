import discord
from pprint import pprint

from src.models import Warning
from src.repositories import RepositoryFactory


class WarningService:
    def __init__(self):
        repository_factory = RepositoryFactory()
        self.repository = repository_factory.get_repository(Warning)

    def clear(self, user_id) -> None:
        """Do nothing"""

    def get(self, user_id) -> None:
        """Do nothing"""

    def remove(self, user_id, warning_id) -> None:
        """Do nothing"""

    def warn(
        self,
        user: discord.Member,
        issuer: discord.Member = None,
        reason: str = None
    ) -> None:
        self.repository.warn(user.id, issuer.id, reason)