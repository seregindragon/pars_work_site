import requests
from fake_useragent import UserAgent

import settings


class RequestEngine:
    SS = 1

    def get_response_cards_list(self, page: int) -> requests.Response:
        params = {"ss": self.SS, "page": page}
        headers = {"User-Agent": UserAgent().random}
        response = requests.get(settings.HOST + settings.ROOT_PATH, params=params, headers=headers)
        response.raise_for_status()
        return response

    def get_response_card(self, card_link: str) -> requests.Response:
        headers = {"User-Agent": UserAgent().random}
        response = requests.get(card_link, headers=headers)
        response.raise_for_status()
        return response