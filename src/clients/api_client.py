import requests

class ApiClient:
    @staticmethod
    def get(url: str, params=None) -> str:
        response = requests.get(url, params=params)
        response.raise_for_status()

        return response.json()