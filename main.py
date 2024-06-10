import argparse
from bs4 import BeautifulSoup

import settings
from parser.dto import Vacancy
from parser.request import RequestEngine
from parser.parser import Parser


def main():
    page = settings.START_PAGE

    while True:
        vacancy = Vacancy()
        page_number = f"PAGE: {page}"
        print(page_number)

        request_engine = RequestEngine()
        response = request_engine.get_response_cards_list(page)
        html = response.text

        parser = Parser(BeautifulSoup(html, "html.parser"))
        cards = parser.find_carts(
            class_="card card-hover card-search card-visited wordwrap job-link js-job-link-blank js-hot-block"
        )

        if not cards:
            break

        for card in cards:
            href, id_vac = parser.get_vacancy_id_and_href(card)
            card_link = settings.HOST + href
            print(card_link)

            response = request_engine.get_response_cards_list(card_link)
            html_in_page = response.text

        break
        page += 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parser of work ua site")
    parser.add_argument("-db", default=False, action="store_true", help="DB store opportunity")
    parser.add_argument("-json", default=False, action="store_true", help="JSON store opportunity")
    args = parser.parse_args()
    main()