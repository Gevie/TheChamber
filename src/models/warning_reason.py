from src.models import Base
from sqlalchemy import Column, String


class WarningReason(Base):
    __tablename__ = 'warning_reasons'

    description = Column(String, nullable=False, unique=True)