import json

from src.data_loaders import BaseDataLoader


class JSONDataLoader(BaseDataLoader):
    """Loads data from json files"""

    def __init__(self, file_path: str):
        """
        Initialize the class

        Args:
            file_path (str): The path to the JSON file
        """

        self.file_path = file_path

    def load(self):
        """
        Loads the data from a JSON file

        Returns:
            Any: Parsed data from the JSON file

        Raises:
            ValueError: If there is an error loading or parsing the JSON file
        """

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError) as exception:
            raise ValueError(f"Error loading JSON data from file {self.file_path}: {exception}")