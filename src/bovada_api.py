import requests


class BovadaAPI:
    def __init__(self):
        self._base_url = "https://www.bovada.lv/services/sports/event/v2/events/A/description/basketball/college-basketball"

    def get_status(self):
        return self.request_url(self._base_url).raise_for_status()

    def get_betting_odds(self):
        return self.call(self._base_url)

    def call(self, url):
        result_json = self.request_json(url)
        max_retry = 10
        while result_json is None:
            result_json = self.request_json(url)
            if max_retry <= 0: return
            max_retry -= 1
        return result_json

    def request_json(self, url):
        result_json_string = self.request_url(url)
        try:
            result_json_string.raise_for_status()
        except requests.exceptions.HTTPError:
            return None
        return result_json_string.json()

    @staticmethod
    def request_url(url):
        return requests.get(url)
