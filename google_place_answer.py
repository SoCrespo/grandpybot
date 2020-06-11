# coding: utf-8

import requests
import place
import config as c

c.GOOGLE_API_KEY
c.GOOGLE_PLACES_API_URL


class GooglePlaceAnswer():
    '''
    Answer from Google Place API. Attributes:

    .candidates : list of Places objects (attributes : name, address, place_id)

    .status : string
    '''

    def __init__(self, word, auto_launch=True):
        if auto_launch:
            answer = self._get_API_answer(word)
            if answer:
                self.candidates = self._convert_into_place(answer['candidates'])
                self.status = answer['status']
            else:
                self.candidate = []
                self.status = "ERROR"

    def _get_API_answer(self, word):
        '''
        Take a word (string) as argument.
        Return a dict of dicts.
        '''
        url = c.GOOGLE_PLACES_API_URL
        key = c.GOOGLE_API_KEY
        payload = {
            "key": key,
            "input": word,
            "inputtype": "textquery",
            "fields": "formatted_address,place_id,name"
        }
        try:
            r = requests.get(url, params=payload)
        except requests.RequestException:
            return None
        return r.json()

    def _convert_into_place(self, list_of_dicts):
        '''
        Convert list of dicts into list of Place objects.
        '''
        places_list = []
        for item in list_of_dicts:
            places_list.append(place.Place(
                name=item['name'],
                address=item["formatted_address"],
                place_id=item['place_id']
                ))
        return places_list


if __name__ == "__main__":
    pass
