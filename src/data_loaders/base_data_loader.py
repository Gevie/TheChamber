from abc import ABC, abstractmethod


class BaseDataLoader(ABC):
    @abstractmethod
    def load(self):
        """Load the raw data from the source."""