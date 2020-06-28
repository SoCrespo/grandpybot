# coding: utf-8

import requests
from backend import place, config as c

c.GOOGLE_API_KEY
c.GOOGLE_PLACES_API_URL


class GooglePlaceExtractor:
    """
    Manage connexion to Google Place API.
    """

    def __init__(self):
        pass

    def get_api_answer(self, text):
        """
        Take a wiki_text (string) as argument.
        Return a list of Places objects.
        """
        url = c.GOOGLE_PLACES_API_URL
        key = c.GOOGLE_API_KEY
        payload = {
            "key": key,
            "input": text,
            "inputtype": "textquery",
            "fields": "formatted_address,place_id,name"
        }
        r = requests.get(url, params=payload).json()['candidates']
        places_list = self._convert_into_place(r)
        return places_list

    def _convert_into_place(self, list_of_dicts):
        """
        Convert list of dicts into list of Place objects.
        """
        places_list = []
        for item in list_of_dicts:
            places_list.append(place.Place(
                name=item['name'],
                address=item["formatted_address"]
                ))
        return places_list


if __name__ == "__main__":
    pass
