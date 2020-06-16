# coding: utf-8

import text_parser as tp
import google_place_extractor
import google_static_map as gm
import wikipedia_extractor as wiki


def ask():
    return input("De quel endroit veux-tu que je te parle ? ")


def say_problem():
    print("mon cerveau Google me joue des tours ! "
          "Reviens quand je serai plus en forme...")


def say_not_understood():
    print("Hmmm, je ne trouve pas de réponse à ta question... ", end="")


def ask_for_choice(list_of_place_objects):
    indexed_options = [f'{k+1}: {item.address}'
                       for k, item in enumerate(list_of_place_objects)]
    choices = (f"A quelle adresse ? {' ou '.join(indexed_options)} ? "
               f"Tape le numéro correspondant : ")
    place = list_of_place_objects[int(input(choices)) - 1]
    return place


def display_infos(place_object):
    print(
        f"Ah, {place_object.name}, je connais cet endroit ! "
        f"C'est situé {place_object.address}."
        f"\nEt à ce sujet, savais-tu que {place_object.text}\n(la suite ici : {place_object.url}, la carte là : {place_object.map})"
    )


def main():
    question_is_valid = False
    while not question_is_valid:
        text = ask()
        relevant_expression = tp.find_relevant_expression(text)
        print(relevant_expression)
        gp = google_place_extractor.GooglePlaceExtractor()
        google_answer = gp.get_api_answer(relevant_expression)
        question_is_valid = True
        if len(google_answer) > 1:
            place = ask_for_choice(google_answer)
        else:
            place = google_answer[0]
        print(place.address)
        we = wiki.WikipediaExtractor()
        page_title = we.get_best_match_title(place.address)
        place.text = we.get_page_extract(page_title)
        place.url = we.get_page_url(page_title)
        place.map = gm.get_map_url(place.address)
        display_infos(place)


if __name__ == "__main__":
    main()
