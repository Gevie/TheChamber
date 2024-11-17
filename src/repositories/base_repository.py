from typing import TypeVar, Generic, Type, List
from sqlalchemy.orm import Session

ModelType = TypeVar('ModelType')


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], db_session: Session):
        self._model = model
        self._db_session = db_session

    def get(self) -> List[ModelType]:
        return (
            self._db_session
                .query(self._model)
                .all()
        )

    def get_by_id(self, model_id: int) -> ModelType:
        return (
            self._db_session
                .query(self._model)
                .filter_by(id=model_id)
                .first()
        )

    def add(self, instance: ModelType) -> ModelType:
        self._db_session.add(instance)
        self._db_session.commit()
        self._db_session.refresh(instance)

        return instance

    def delete(self, model_id: int) -> None:
        instance = self.get_by_id(model_id)

        if instance:
            self._db_session.delete(instance)
            self._db_session.commit()