# coding: utf-8

from backend import google_place_extractor, google_static_map as gm, wikipedia_extractor as wiki, text_parser as tp


class AnswerFetcher:

    def __init__(self):
        pass

    def find_answer(self, text):
        relevant_expression = tp.find_relevant_expression(text)
        gp = google_place_extractor.GooglePlaceExtractor()
        google_answer = gp.get_api_answer(relevant_expression)
        try:
            place = google_answer[0]
            we = wiki.WikipediaExtractor()
            page_title = we.get_best_match_title(place.address)
            place.wiki_text = we.get_page_extract(page_title)
            place.wiki_url = we.get_page_url(page_title)
            place.map = gm.get_map_url(place.address)
            return place
        except:
            return None


