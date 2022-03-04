import requests


class Dictionary(object):
    def __init__(self) -> None:
        self.api_url = "https://api.dictionaryapi.dev/api/v2/entries/en_US/"

    def search(self, word):
        url = f"{self.api_url}{word}"
        return requests.get(url).json()
