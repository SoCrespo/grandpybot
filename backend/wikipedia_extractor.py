# coding: utf-8

import requests
from backend import config as c


class WikipediaExtractor:

    def __init__(self):
        pass

    def get_best_match_title(self, text):
        """
        Take a text as argument.
        Call Wikipedia API to find 1st relevant page for this text.
        Return a string (title of the page).
        """
        url = c.WIKI_ENDPOINT
        payload = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": text,
            "srlimit": 1,
        }
        r = requests.get(url, params=payload).json()
        title = r['query']['search'][0]['title']
        return title

    def get_page_extract(self, page_title):
        """
        Take a wikipedia page title (string) as argument.
        Call Wikipedia API.
        Return the 1st paragraph (string) of the corresponding
        Wikipedia page.
        """
        url = c.WIKI_ENDPOINT
        payload = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "extracts",
            "exchars": 200,
            "exintro": 0,
            "exlimit": 1,
            "explaintext": 1,
            "exsectionformat": "plain",
        }
        r = requests.get(url, params=payload).json()
        return list(r['query']['pages'].values())[0]['extract']

    def get_page_url(self, page_title):
        url = c.WIKI_ENDPOINT
        payload = {
            "action": "query",
            "format": "json",
            "titles": page_title,
            "prop": "info",
            "inprop": "url",
        }
        r = requests.get(url, params=payload).json()
        return list(r['query']['pages'].values())[0]['fullurl']


if __name__ == "__main__":
    pass