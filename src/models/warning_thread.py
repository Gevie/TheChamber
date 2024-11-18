from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class WarningThread(Base):
    __tablename__ = 'warning_threads'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    thread_id = Column(String, nullable=False, unique=True)

    user = relationship(
        'User',
        back_populates='warning_threads'
    )