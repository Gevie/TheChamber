from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from src.models import Base


class Guild(Base):
    __tablename__ = 'guilds'

    discord_id = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    warning_channel_id = Column(String, nullable=False)
    warning_forum_id = Column(String, nullable=False)

    users = relationship(
        'User',
        back_populates='guild'
    )