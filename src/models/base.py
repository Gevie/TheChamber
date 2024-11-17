from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer, TIMESTAMP, func

@as_declarative()
class Base:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    updated = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now(), nullable=False)