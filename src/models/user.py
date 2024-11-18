from src.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'

    discord_id = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)
    discriminator = Column(String, nullable=False)
    nickname = Column(String, nullable=True)
    guild_id = Column(Integer, ForeignKey('guilds.id'), nullable=False)

    guild = relationship(
        'Guild',
        back_populates='users'
    )

    warnings = relationship(
        'Warning',
        back_populates='user',
        cascade='all, delete-orphan',
        foreign_keys='[Warning.user_id]'
    )

    issued_warnings = relationship(
        'Warning',
        back_populates='user',
        cascade='all, delete-orphan',
        foreign_keys='[Warning.issuer_id]'
    )

    warning_threads = relationship(
        'WarningThread',
        back_populates='user'
    )

    bans = relationship(
        'Ban',
        back_populates='user'
    )