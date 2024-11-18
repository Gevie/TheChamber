from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base
from datetime import datetime


class Ban(Base):
    __tablename__ = 'bans'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship(
        'User',
        back_populates='bans'
    )