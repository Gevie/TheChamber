from datetime import datetime
from src.models import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship


class Warning(Base):
    __tablename__ = 'warnings'

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    issuer_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    reason_id = Column(Integer, ForeignKey('warning_reasons.id'), nullable=True)
    thread_id = Column(Integer, ForeignKey('warning_threads.id'), nullable=True)
    reason_text = Column(String, nullable=True)

    user = relationship(
        'User',
        back_populates='warnings',
        foreign_keys='[user_id]'
    )

    issuer = relationship(
        'User',
        back_populates='issued_warnings',
        foreign_keys='[issuer_id]'
    )

    reason = relationship(
        'WarningReason',
        back_populates='warnings'
    )

    thread = relationship(
        'WarningThread',
        back_populates='warnings'
    )