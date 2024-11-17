from sqlalchemy import Column, Float, Text
from src.models import Base

class TemperatureFact(Base):
    __tablename__ = 'temperature_facts'

    min_temperature = Column(Float, nullable=False)
    max_temperature = Column(Float, nullable=False)
    fact = Column(Text, nullable=False)

    def __repr__(self):
        return (
            f"<TemperatureFact("
                f"id={self.id}, "
                f"min_temperature={self.min_temperature}, "
                f"max_temperature={self.max_temperature}, "
                f"fact='{self.fact}', "
                f"created={self.created}, "
                f"updated={self.updated}"
            f")>"
        )