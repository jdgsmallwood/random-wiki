"""
This outlines the basic structure of a Program
"""
import webbrowser
from typing import List, Protocol

import requests
from bs4 import BeautifulSoup

from random_wiki.random_wiki_text import (
    article_declined,
    article_delivery,
    article_success,
    introduction,
    invalid_response,
)


class Program(Protocol):

    program_name: str

    def main(self):
        pass


def get_random_wikipedia_article() -> List[str]:
    """
    This will get the article title and link for a random wikipedia article.
    :return:
    """
    random_link_location = "https://en.wikipedia.org/wiki/Special:Random"
    response = requests.get(random_link_location)
    link = response.url
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.findAll(id="firstHeading")[0].text
    return [title, link]


def validate_response(response: str) -> bool:
    """
    This will validate the response given by the user and raise a ResponseValidationError if the input is incorrect.
    :return:
    """
    if isinstance(response, str):
        if response.lower() in ["yes", "no"]:
            return True
    raise ResponseValidationError("Please try again!")


def open_link(link: str):
    """
    This will pass down a link to be opened by the web browser.
    :return:
    """
    webbrowser.open(link)


class RandomWiki(Program):

    program_name = "random_wiki"

    def main(self):
        print(introduction)
        while True:
            article_title, link = get_random_wikipedia_article()
            print(f"{article_delivery} {article_title}")
            while True:
                try:
                    response = input()
                    validate_response(response)
                    if response.lower() == "yes":
                        open_link(link)
                        print(article_success)
                        exit()
                    else:
                        print(article_declined)
                        break
                except ResponseValidationError:
                    print(invalid_response)


class ResponseValidationError(Exception):
    pass
