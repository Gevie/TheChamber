import json

from src.data_loaders import BaseDataLoader


class JSONDataLoader(BaseDataLoader):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError) as exception:
            raise ValueError(f"Error loading JSON data from file {self.file_path}: {exception}")